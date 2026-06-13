import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import os.path as osp
import threading
import numpy as np
import cv2

# ── Colour palette ─────────────────────────────────────────────────────────────
BG       = "#1A1A2E"
PANEL    = "#16213E"
ACCENT   = "#E94560"
ACCENT2  = "#0F3460"
TEXT     = "#EAEAEA"
SUBTEXT  = "#8892A4"
ENTRY_BG = "#0D1B2A"
BTN_HV   = "#FF6B81"

# ── Constants (fixed typo: RIGHT_EYE_RABGE → RIGHT_EYE_RANGE) ─────────────────
OUT_SIZE        = (224, 224)
LEFT_EYE_RANGE  = (36, 42)
RIGHT_EYE_RANGE = (42, 48)          # ← typo fixed
LEFT_EYE_POS    = (0.35, 0.3815)
DAT_PATH        = "./dat/shape_predictor_68_face_landmarks.dat"

# ── Core face detection & alignment logic ─────────────────────────────────────
def shape_to_pos(shape):
    parts = [(p.x, p.y) for p in shape.parts()]
    left  = np.array(parts[LEFT_EYE_RANGE[0]:  LEFT_EYE_RANGE[1]])
    right = np.array(parts[RIGHT_EYE_RANGE[0]: RIGHT_EYE_RANGE[1]])
    return left, right

def detect_align_faces(detector, sp, img):
    """
    Detect and align faces in a numpy RGB image.
    Returns list of aligned face images (RGB).
    Fix: use float division for center calculation, not integer //
    """
    faces = detector(img, 1)
    res   = []
    for face in faces:
        shape = sp(img, face)
        left, right = shape_to_pos(shape)

        left_center  = np.mean(left,  axis=0)
        right_center = np.mean(right, axis=0)

        dx    = right_center[0] - left_center[0]
        dy    = right_center[1] - left_center[1]
        angle = np.degrees(np.arctan2(dy, dx))
        dist  = np.sqrt(dy**2 + dx**2)

        out_dist = OUT_SIZE[0] * (1 - 2 * LEFT_EYE_POS[0])
        scale    = out_dist / dist if dist != 0 else 1.0

        # Fix: use float division (/ 2.0) not integer // which caused offset errors
        center = ((left_center + right_center) / 2.0).tolist()

        mat = cv2.getRotationMatrix2D(tuple(center), angle, scale)
        mat[0, 2] += (0.5 * OUT_SIZE[0]          - center[0])
        mat[1, 2] += (LEFT_EYE_POS[1] * OUT_SIZE[1] - center[1])

        aligned = cv2.warpAffine(img, mat, OUT_SIZE, flags=cv2.INTER_CUBIC)
        res.append(aligned)
    return res

# ── GUI ────────────────────────────────────────────────────────────────────────
class FaceAlignApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Face Detection & Alignment")
        self.geometry("820x720")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.img_path      = None
        self.aligned_faces = []   # list of PIL images

        self._build_header()
        self._build_image_panel()
        self._build_run_button()
        self._build_results()
        self._build_footer()

    # ── Header ─────────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self, bg=ACCENT2, pady=14)
        hdr.pack(fill="x")
        tk.Label(hdr, text="👤  Face Detection & Alignment",
                 font=("Georgia", 20, "bold"), fg=TEXT, bg=ACCENT2).pack()
        tk.Label(hdr, text="Detects faces and aligns them by eye position using dlib 68-point landmarks",
                 font=("Georgia", 9), fg=SUBTEXT, bg=ACCENT2).pack()

    # ── Image input panel ──────────────────────────────────────────────────────
    def _build_image_panel(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="x", padx=30, pady=(14, 0))

        tk.Label(frm, text="INPUT IMAGE", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        self.preview_frame = tk.Frame(frm, bg=ENTRY_BG, width=760, height=180)
        self.preview_frame.pack(fill="x")
        self.preview_frame.pack_propagate(False)

        self.preview_label = tk.Label(
            self.preview_frame,
            text="No image selected\nClick 'Browse' to choose a photo",
            font=("Courier", 11), fg=SUBTEXT, bg=ENTRY_BG, justify="center")
        self.preview_label.place(relx=0.5, rely=0.5, anchor="center")

        tk.Frame(frm, bg=ACCENT, height=2).pack(fill="x")

        btn_row = tk.Frame(frm, bg=BG)
        btn_row.pack(fill="x", pady=(8, 0))

        tk.Button(btn_row, text="📂 Browse Image",
                  font=("Courier", 10, "bold"),
                  fg=TEXT, bg=ACCENT2, relief="flat",
                  activebackground=BTN_HV, cursor="hand2",
                  padx=12, pady=6, command=self._browse).pack(side="left")

        self.path_label = tk.Label(btn_row, text="", font=("Courier", 9),
                                   fg=SUBTEXT, bg=BG, anchor="w")
        self.path_label.pack(side="left", padx=10, fill="x", expand=True)

    def _browse(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff"),
                       ("All files", "*.*")])
        if not path:
            return
        self.img_path = path
        self.path_label.config(text=os.path.basename(path))
        self._show_preview(path)

    def _show_preview(self, path):
        try:
            img = Image.open(path)
            img.thumbnail((760, 175))
            photo = ImageTk.PhotoImage(img)
            self.preview_label.config(image=photo, text="")
            self.preview_label.image = photo
        except Exception:
            self.preview_label.config(image="", text="Preview unavailable")

    # ── Run button ─────────────────────────────────────────────────────────────
    def _build_run_button(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(pady=12)

        self.run_btn = tk.Button(frm, text="DETECT & ALIGN FACES  ➜",
                                 font=("Courier", 13, "bold"),
                                 fg=TEXT, bg=ACCENT, activebackground=BTN_HV,
                                 relief="flat", cursor="hand2",
                                 padx=24, pady=10,
                                 command=self._run_thread)
        self.run_btn.pack(side="left")
        self.run_btn.bind("<Enter>", lambda e: self.run_btn.config(bg=BTN_HV))
        self.run_btn.bind("<Leave>", lambda e: self.run_btn.config(bg=ACCENT))

        tk.Button(frm, text="💾 Save All Faces",
                  font=("Courier", 10, "bold"),
                  fg=TEXT, bg=ACCENT2, relief="flat",
                  activebackground=BTN_HV, cursor="hand2",
                  padx=12, pady=10,
                  command=self._save_all).pack(side="left", padx=(10, 0))

    # ── Results grid ───────────────────────────────────────────────────────────
    def _build_results(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="both", expand=True, padx=30)

        tk.Label(frm, text="ALIGNED FACES", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        container = tk.Frame(frm, bg=ACCENT2, padx=1, pady=1)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg=PANEL, bd=0, highlightthickness=0)
        scroll = tk.Scrollbar(container, orient="horizontal",
                              command=canvas.xview)
        canvas.configure(xscrollcommand=scroll.set)
        scroll.pack(side="bottom", fill="x")
        canvas.pack(fill="both", expand=True)

        self.face_frame = tk.Frame(canvas, bg=PANEL)
        self.canvas_window = canvas.create_window((0, 0), window=self.face_frame,
                                                   anchor="nw")
        self.face_frame.bind("<Configure>",
                             lambda e: canvas.configure(
                                 scrollregion=canvas.bbox("all")))
        self.canvas = canvas

        self.no_face_label = tk.Label(self.face_frame,
                                      text="Aligned faces will appear here",
                                      font=("Courier", 11), fg=SUBTEXT, bg=PANEL,
                                      pady=40)
        self.no_face_label.pack()

    def _show_faces(self, faces):
        """Render aligned face thumbnails in the scrollable panel."""
        for w in self.face_frame.winfo_children():
            w.destroy()

        if not faces:
            tk.Label(self.face_frame, text="No faces detected in this image.",
                     font=("Courier", 11), fg=SUBTEXT, bg=PANEL,
                     pady=40).pack()
            return

        for i, pil_img in enumerate(faces):
            cell = tk.Frame(self.face_frame, bg=PANEL, padx=8, pady=8)
            cell.pack(side="left")

            thumb = pil_img.copy()
            thumb.thumbnail((150, 150))
            photo = ImageTk.PhotoImage(thumb)

            lbl = tk.Label(cell, image=photo, bg=ENTRY_BG)
            lbl.image = photo
            lbl.pack()

            tk.Label(cell, text=f"Face {i+1}",
                     font=("Courier", 9), fg=SUBTEXT, bg=PANEL).pack()

    # ── Footer ─────────────────────────────────────────────────────────────────
    def _build_footer(self):
        self.status_var = tk.StringVar(value="Ready — browse an image and click Detect")
        tk.Label(self, textvariable=self.status_var,
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(pady=(4, 6))

    # ── Processing ─────────────────────────────────────────────────────────────
    def _run_thread(self):
        if not self.img_path or not os.path.exists(self.img_path):
            messagebox.showwarning("No Image", "Please select an image file first.")
            return
        if not os.path.exists(DAT_PATH):
            messagebox.showerror(
                "Missing Model File",
                f"Landmark model not found at:\n{DAT_PATH}\n\n"
                "Download it from:\n"
                "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2\n\n"
                "Extract and place in a 'dat/' folder next to this script.")
            return
        self.run_btn.config(text="Processing…", state="disabled")
        self.status_var.set("Detecting and aligning faces…")
        threading.Thread(target=self._process, daemon=True).start()

    def _process(self):
        try:
            import dlib
            detector = dlib.get_frontal_face_detector()
            sp       = dlib.shape_predictor(DAT_PATH)

            img = cv2.imread(self.img_path, cv2.IMREAD_ANYCOLOR)
            if img is None:
                raise ValueError("Could not read image file.")
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            aligned = detect_align_faces(detector, sp, img_rgb)

            # Convert to PIL
            pil_faces = [Image.fromarray(f) for f in aligned]
            self.aligned_faces = pil_faces

            self.after(0, self._show_faces, pil_faces)
            self.after(0, self.status_var.set,
                       f"Done — {len(pil_faces)} face(s) detected and aligned.")

        except ImportError:
            self.after(0, messagebox.showerror, "Missing Package",
                "dlib is not installed.\n\nRun:\n  python.exe -m pip install dlib")
            self.after(0, self.status_var.set, "Error: dlib not installed.")
        except Exception as e:
            self.after(0, messagebox.showerror, "Error", str(e))
            self.after(0, self.status_var.set, f"Error: {e}")
        finally:
            self.after(0, self.run_btn.config,
                       {"text": "DETECT & ALIGN FACES  ➜", "state": "normal"})

    def _save_all(self):
        if not self.aligned_faces:
            messagebox.showwarning("No Faces", "Run detection first.")
            return
        folder = filedialog.askdirectory(title="Select folder to save aligned faces")
        if not folder:
            return
        base = osp.splitext(osp.basename(self.img_path))[0] if self.img_path else "face"
        for i, face in enumerate(self.aligned_faces):
            out_path = osp.join(folder, f"{base}_face_{i+1:03}.jpg")
            face.save(out_path)
        self.status_var.set(f"Saved {len(self.aligned_faces)} face(s) to {folder}")
        messagebox.showinfo("Saved", f"{len(self.aligned_faces)} face(s) saved to:\n{folder}")


if __name__ == "__main__":
    app = FaceAlignApp()
    app.mainloop()