import cv2
import numpy as np
import os
import winsound
import threading

# ── Alarm ─────────────────────────────────────────────────────────────────────
alarm_playing = False

def play_alarm():
    global alarm_playing
    alarm_playing = True
    if os.path.exists('alarm.wav'):
        winsound.PlaySound('alarm.wav', winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
    else:
        for _ in range(3):
            winsound.Beep(1000, 500)
    alarm_playing = False

def stop_alarm():
    global alarm_playing
    alarm_playing = False
    winsound.PlaySound(None, winsound.SND_PURGE)

# ── Load OpenCV built-in Haar cascades (no external files needed) ─────────────
cascade_dir = cv2.data.haarcascades  # built-in path inside opencv package

face_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_frontalface_alt.xml')
leye_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_lefteye_2splits.xml')
reye_cascade = cv2.CascadeClassifier(cascade_dir + 'haarcascade_righteye_2splits.xml')

# ── EAR using eye bounding box (simple open/close ratio) ─────────────────────
def eye_open_ratio(eye_img):
    """
    Detects if eye is open using pixel intensity variance.
    Open eye has higher contrast than closed eye.
    """
    if eye_img is None or eye_img.size == 0:
        return 0
    gray = cv2.cvtColor(eye_img, cv2.COLOR_BGR2GRAY) if len(eye_img.shape) == 3 else eye_img
    gray = cv2.resize(gray, (24, 24))
    gray = cv2.equalizeHist(gray)
    # Closed eyes → dark uniform region; open eyes → higher variance
    return np.std(gray)

# ── Thresholds ────────────────────────────────────────────────────────────────
OPEN_THRESHOLD = 30    # std dev below this → eye likely closed
DROWSY_FRAMES  = 20    # frames before alert

# ── State ─────────────────────────────────────────────────────────────────────
score = 0
thicc = 2
font  = cv2.FONT_HERSHEY_COMPLEX_SMALL
path  = os.getcwd()
rpred = 1   # 1=open, 0=closed
lpred = 1

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Drowsiness Detection started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Camera read failed. Exiting.")
        break

    height, width = frame.shape[:2]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # ── Detect face ───────────────────────────────────────────────────────────
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                          minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 100, 100), 1)

    # ── Detect right eye ──────────────────────────────────────────────────────
    right_eyes = reye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in right_eyes:
        r_eye = frame[y:y+h, x:x+w]
        ratio = eye_open_ratio(r_eye)
        rpred = 0 if ratio < OPEN_THRESHOLD else 1
        color = (0, 255, 0) if rpred == 1 else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 1)
        break

    # ── Detect left eye ───────────────────────────────────────────────────────
    left_eyes = leye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in left_eyes:
        l_eye = frame[y:y+h, x:x+w]
        ratio = eye_open_ratio(l_eye)
        lpred = 0 if ratio < OPEN_THRESHOLD else 1
        color = (0, 255, 0) if lpred == 1 else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 1)
        break

    # ── Status bar ────────────────────────────────────────────────────────────
    cv2.rectangle(frame, (0, height-50), (250, height), (0, 0, 0), cv2.FILLED)

    # ── Score logic ───────────────────────────────────────────────────────────
    if rpred == 0 and lpred == 0:
        score += 1
        cv2.putText(frame, "Closed", (10, height-20),
                    font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    else:
        score = max(0, score - 1)
        if alarm_playing:
            stop_alarm()
        cv2.putText(frame, "Open", (10, height-20),
                    font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.putText(frame, f"Score: {score}", (100, height-20),
                font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    # ── Drowsiness alert ──────────────────────────────────────────────────────
    if score > DROWSY_FRAMES:
        cv2.imwrite(os.path.join(path, 'drowsy_capture.jpg'), frame)

        if not alarm_playing:
            threading.Thread(target=play_alarm, daemon=True).start()

        if thicc < 16:
            thicc += 2
        else:
            thicc -= 2
            if thicc < 2:
                thicc = 2

        cv2.rectangle(frame, (0, 0), (width, height), (0, 0, 255), thicc)
        cv2.putText(frame, "DROWSINESS ALERT!", (width//2 - 130, 40),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    else:
        thicc = 2

    cv2.imshow('Drowsiness Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stop_alarm()
cap.release()
cv2.destroyAllWindows()
print("Session ended.")