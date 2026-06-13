import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import datetime
import os
import io
import numpy as np
import sounddevice as sd
import speech_recognition as sr

# ── Colour palette ─────────────────────────────────────────────────────────────
BG       = "#1A1A2E"
PANEL    = "#16213E"
ACCENT   = "#E94560"
ACCENT2  = "#0F3460"
TEXT     = "#EAEAEA"
SUBTEXT  = "#8892A4"
ENTRY_BG = "#0D1B2A"
BTN_HV   = "#FF6B81"
GREEN    = "#2ECC71"
YELLOW   = "#F39C12"

# ── Supported languages ────────────────────────────────────────────────────────
LANGUAGES = {
    "English (US)":  "en-US",  "English (UK)":  "en-GB",
    "Hindi":         "hi-IN",  "French":         "fr-FR",
    "German":        "de-DE",  "Spanish":        "es-ES",
    "Italian":       "it-IT",  "Portuguese":     "pt-BR",
    "Russian":       "ru-RU",  "Japanese":       "ja-JP",
    "Korean":        "ko-KR",  "Chinese":        "zh-CN",
    "Arabic":        "ar-SA",  "Turkish":        "tr-TR",
    "Dutch":         "nl-NL",  "Polish":         "pl-PL",
    "Swedish":       "sv-SE",  "Bengali":        "bn-BD",
    "Nepali":        "ne-NP",  "Marathi":        "mr-IN",
}
LANG_NAMES = list(LANGUAGES.keys())

SAMPLE_RATE = 16000   # Hz — good quality for speech recognition

# ── Core recording using sounddevice ──────────────────────────────────────────
def record_voice(language_code: str, duration: int = 8,
                 status_callback=None) -> str:
    """
    Record audio via sounddevice, convert to AudioData,
    then send to Google Speech Recognition.
    """
    try:
        if status_callback:
            status_callback("🎙 Listening… speak now!", GREEN)

        # Record raw audio as numpy array
        audio_np = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='int16'
        )
        sd.wait()   # block until recording is done

        if status_callback:
            status_callback("⏳ Recognising speech…", YELLOW)

        # Convert numpy array → bytes → sr.AudioData
        audio_bytes = audio_np.tobytes()
        audio_data  = sr.AudioData(audio_bytes, SAMPLE_RATE, 2)

        recognizer = sr.Recognizer()
        phrase = recognizer.recognize_google(audio_data, language=language_code)
        return phrase

    except sr.UnknownValueError:
        return "__UNKNOWN__"
    except sr.RequestError as e:
        return f"__ERROR__Could not reach Google Speech API: {e}"
    except sd.PortAudioError as e:
        return f"__NOMIC__No microphone found: {e}"
    except Exception as e:
        return f"__ERROR__{e}"


# ── GUI ────────────────────────────────────────────────────────────────────────
class SpeechToTextApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Speech to Text")
        self.geometry("680x600")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.is_recording   = False
        self.transcript_lines = []

        self._build_header()
        self._build_controls()
        self._build_mic_button()
        self._build_output()
        self._build_footer()

    # ── Header ─────────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self, bg=ACCENT2, pady=14)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🎙  Speech to Text",
                 font=("Georgia", 20, "bold"), fg=TEXT, bg=ACCENT2).pack()
        tk.Label(hdr, text="Google Speech Recognition  •  sounddevice  •  20 languages",
                 font=("Georgia", 9), fg=SUBTEXT, bg=ACCENT2).pack()

    # ── Language + duration controls ───────────────────────────────────────────
    def _build_controls(self):
        row = tk.Frame(self, bg=BG, pady=14)
        row.pack(fill="x", padx=30)

        # Language
        lang_col = tk.Frame(row, bg=BG)
        lang_col.pack(side="left")
        tk.Label(lang_col, text="LANGUAGE", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        self.lang_var = tk.StringVar(value="English (US)")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox",
                        fieldbackground=ENTRY_BG, background=ACCENT2,
                        foreground=TEXT, selectbackground=ACCENT,
                        borderwidth=0, relief="flat")
        cb = ttk.Combobox(lang_col, textvariable=self.lang_var,
                          values=LANG_NAMES, state="readonly",
                          width=22, font=("Courier", 11))
        cb.pack()
        cb.bind("<<ComboboxSelected>>",
                lambda e: self.code_label.config(
                    text=LANGUAGES.get(self.lang_var.get(), "en-US")))

        self.code_label = tk.Label(lang_col, text="en-US",
                                   font=("Courier", 9), fg=ACCENT, bg=BG)
        self.code_label.pack(anchor="w")

        # Duration
        dur_col = tk.Frame(row, bg=BG)
        dur_col.pack(side="left", padx=(30, 0))
        tk.Label(dur_col, text="DURATION (seconds)",
                 font=("Courier", 9, "bold"), fg=SUBTEXT, bg=BG).pack(anchor="w")

        self.duration_var = tk.IntVar(value=8)
        sb = tk.Spinbox(dur_col, from_=3, to=60,
                        textvariable=self.duration_var,
                        width=5, font=("Courier", 12),
                        bg=ENTRY_BG, fg=TEXT,
                        buttonbackground=ACCENT2,
                        relief="flat", insertbackground=ACCENT)
        sb.pack(anchor="w")
        tk.Label(dur_col, text="(3–60 sec)",
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(anchor="w")

    # ── Mic button ─────────────────────────────────────────────────────────────
    def _build_mic_button(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(pady=10)

        self.mic_btn = tk.Button(
            frm, text="🎙  START RECORDING",
            font=("Courier", 14, "bold"),
            fg=TEXT, bg=ACCENT, activebackground=BTN_HV,
            relief="flat", cursor="hand2",
            padx=30, pady=14,
            command=self._start_recording
        )
        self.mic_btn.pack()
        self.mic_btn.bind("<Enter>",
            lambda e: self.mic_btn.config(bg=BTN_HV) if not self.is_recording else None)
        self.mic_btn.bind("<Leave>",
            lambda e: self.mic_btn.config(bg=ACCENT) if not self.is_recording else None)

        self.status_var = tk.StringVar(value="Press the button and speak")
        self.status_label = tk.Label(frm, textvariable=self.status_var,
                                     font=("Courier", 10), fg=SUBTEXT,
                                     bg=BG, pady=6)
        self.status_label.pack()

        # Progress bar shown while recording
        self.progress = ttk.Progressbar(frm, mode="indeterminate", length=300)

    # ── Output ─────────────────────────────────────────────────────────────────
    def _build_output(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="both", expand=True, padx=30)

        tk.Label(frm, text="TRANSCRIPT", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        box = tk.Frame(frm, bg=ACCENT2, padx=1, pady=1)
        box.pack(fill="both", expand=True)

        scroll = tk.Scrollbar(box)
        scroll.pack(side="right", fill="y")

        self.output_text = tk.Text(
            box, font=("Georgia", 12),
            bg=PANEL, fg=ACCENT,
            insertbackground=ACCENT,
            relief="flat", padx=10, pady=8,
            wrap="word", state="disabled", bd=0,
            yscrollcommand=scroll.set
        )
        self.output_text.pack(fill="both", expand=True)
        scroll.config(command=self.output_text.yview)

        btn_row = tk.Frame(frm, bg=BG)
        btn_row.pack(fill="x", pady=(6, 0))

        tk.Button(btn_row, text="🗑 Clear", font=("Courier", 9),
                  fg=SUBTEXT, bg=BG, relief="flat", cursor="hand2",
                  activeforeground=TEXT,
                  command=self._clear).pack(side="left")

        tk.Button(btn_row, text="💾 Save .txt", font=("Courier", 9),
                  fg=SUBTEXT, bg=BG, relief="flat", cursor="hand2",
                  activeforeground=TEXT,
                  command=self._save).pack(side="right", padx=(0, 8))

        tk.Button(btn_row, text="📋 Copy All", font=("Courier", 9),
                  fg=SUBTEXT, bg=BG, relief="flat", cursor="hand2",
                  activeforeground=TEXT,
                  command=self._copy).pack(side="right")

    # ── Footer ─────────────────────────────────────────────────────────────────
    def _build_footer(self):
        tk.Label(self,
                 text="Requires internet  •  Each recording appends to transcript",
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(pady=(4, 6))

    # ── Logic ──────────────────────────────────────────────────────────────────
    def _start_recording(self):
        if self.is_recording:
            return
        self.is_recording = True
        self.mic_btn.config(text="⏹  RECORDING…", bg="#8B0000", state="disabled")
        self.progress.pack(pady=(0, 4))
        self.progress.start(10)
        threading.Thread(target=self._record, daemon=True).start()

    def _record(self):
        lang_code = LANGUAGES.get(self.lang_var.get(), "en-US")
        duration  = self.duration_var.get()
        result    = record_voice(lang_code, duration,
                                 status_callback=self._set_status)

        if result == "__UNKNOWN__":
            self._set_status("❌ Couldn't understand. Try again.", ACCENT)
        elif result == "__TIMEOUT__":
            self._set_status("⏱ Timeout. Try again.", YELLOW)
        elif result.startswith("__NOMIC__"):
            self.after(0, messagebox.showerror, "No Microphone",
                       "No microphone detected. Please connect one.")
            self._set_status("❌ No microphone.", ACCENT)
        elif result.startswith("__ERROR__"):
            self._set_status(f"❌ {result[9:]}", ACCENT)
        else:
            ts   = datetime.datetime.now().strftime("%H:%M:%S")
            line = f"[{ts}] {result}"
            self.transcript_lines.append(line)
            self.after(0, self._append_text, line)
            self._set_status(
                f"✅ Done! Recognised {len(result.split())} word(s).", GREEN)

        self.is_recording = False
        self.after(0, self.progress.stop)
        self.after(0, self.progress.pack_forget)
        self.after(0, self.mic_btn.config,
                   {"text": "🎙  START RECORDING",
                    "bg": ACCENT, "state": "normal"})

    def _set_status(self, msg, color=SUBTEXT):
        self.after(0, self.status_var.set, msg)
        self.after(0, self.status_label.config, {"fg": color})

    def _append_text(self, line):
        self.output_text.config(state="normal")
        self.output_text.insert("end", line + "\n")
        self.output_text.config(state="disabled")
        self.output_text.see("end")

    def _copy(self):
        content = self.output_text.get("1.0", "end").strip()
        if content:
            self.clipboard_clear()
            self.clipboard_append(content)

    def _save(self):
        if not self.transcript_lines:
            messagebox.showwarning("Nothing to save", "Record something first.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="you_said_this.txt",
            filetypes=[("Text file", "*.txt")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(self.transcript_lines))
            messagebox.showinfo("Saved",
                f"Transcript saved to:\n{os.path.basename(path)}")

    def _clear(self):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.config(state="disabled")
        self.transcript_lines.clear()
        self._set_status("Transcript cleared. Press the button to record.")


if __name__ == "__main__":
    app = SpeechToTextApp()
    app.mainloop()