import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import threading

# ── Colour palette ─────────────────────────────────────────────────────────────
BG       = "#1A1A2E"
PANEL    = "#16213E"
ACCENT   = "#E94560"
ACCENT2  = "#0F3460"
TEXT     = "#EAEAEA"
SUBTEXT  = "#8892A4"
ENTRY_BG = "#0D1B2A"
BTN_HV   = "#FF6B81"

# ── EasyOCR language codes ─────────────────────────────────────────────────────
# EasyOCR uses different codes than agentocr
LANGUAGES = {
    "English":               ["en"],
    "Chinese Simplified":    ["ch_sim", "en"],
    "Chinese Traditional":   ["ch_tra", "en"],
    "French":                ["fr"],
    "German":                ["de"],
    "Japanese":              ["ja"],
    "Korean":                ["ko"],
    "Italian":               ["it"],
    "Spanish":               ["es"],
    "Portuguese":            ["pt"],
    "Russian":               ["ru"],
    "Arabic":                ["ar"],
    "Hindi":                 ["hi"],
    "Bengali":               ["bn"],
    "Tamil":                 ["ta"],
    "Telugu":                ["te"],
    "Thai":                  ["th"],
    "Vietnamese":            ["vi"],
    "Turkish":               ["tr"],
    "Polish":                ["pl"],
    "Dutch":                 ["nl"],
    "Swedish":               ["sv"],
    "Norwegian":             ["no"],
    "Danish":                ["da"],
    "Finnish":               ["fi"],
    "Czech":                 ["cs"],
    "Slovak":                ["sk"],
    "Hungarian":             ["hu"],
    "Romanian":              ["ro"],
    "Bulgarian":             ["bg"],
    "Ukrainian":             ["uk"],
    "Croatian":              ["hr"],
    "Serbian (Latin)":       ["rs_latin"],
    "Serbian (Cyrillic)":    ["rs_cyrillic"],
    "Slovenian":             ["sl"],
    "Estonian":              ["et"],
    "Latvian":               ["lv"],
    "Lithuanian":            ["lt"],
    "Indonesian":            ["id"],
    "Malay":                 ["ms"],
    "Tagalog":               ["tl"],
    "Nepali":                ["ne"],
    "Urdu":                  ["ur"],
    "Persian":               ["fa"],
    "Mongolian":             ["mn"],
    "Uzbek":                 ["uz"],
    "Azerbaijani":           ["az"],
    "Kazakh":                ["ka"],
    "Albanian":              ["sq"],
    "Afrikaans":             ["af"],
    "Swahili":               ["sw"],
    "Welsh":                 ["cy"],
    "Irish":                 ["ga"],
    "Icelandic":             ["is"],
    "Maltese":               ["mt"],
    "Bosnian":               ["bs"],
    "Macedonian":            ["mk"],
    "Belarusian":            ["be"],
}
LANG_NAMES = sorted(LANGUAGES.keys())

# ── Cached OCR reader ──────────────────────────────────────────────────────────
reader_instance  = None
reader_languages = None

def get_reader(lang_list: list):
    global reader_instance, reader_languages
    if reader_instance is None or reader_languages != lang_list:
        import easyocr
        reader_instance  = easyocr.Reader(lang_list, gpu=False)
        reader_languages = lang_list
    return reader_instance

# ── App ────────────────────────────────────────────────────────────────────────
class OCRApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Language OCR")
        self.geometry("780x700")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.img_path = None

        self._build_header()
        self._build_lang_row()
        self._build_image_panel()
        self._build_run_button()
        self._build_output()
        self._build_footer()

    # ── Header ─────────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self, bg=ACCENT2, pady=14)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🔍  Multi-Language OCR",
                 font=("Georgia", 20, "bold"), fg=TEXT, bg=ACCENT2).pack()
        tk.Label(hdr, text="Powered by EasyOCR  •  60+ languages supported",
                 font=("Georgia", 9), fg=SUBTEXT, bg=ACCENT2).pack()

    # ── Language selector ──────────────────────────────────────────────────────
    def _build_lang_row(self):
        row = tk.Frame(self, bg=BG, pady=12)
        row.pack(fill="x", padx=30)

        tk.Label(row, text="RECOGNITION LANGUAGE", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).grid(row=0, column=0, sticky="w")

        self.lang_var = tk.StringVar(value="English")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox",
                        fieldbackground=ENTRY_BG, background=ACCENT2,
                        foreground=TEXT, selectbackground=ACCENT,
                        borderwidth=0, relief="flat")

        cb = ttk.Combobox(row, textvariable=self.lang_var,
                          values=LANG_NAMES, state="readonly",
                          width=30, font=("Courier", 11))
        cb.grid(row=1, column=0, sticky="w")

        self.code_label = tk.Label(row, text="code: en",
                                   font=("Courier", 10), fg=ACCENT,
                                   bg=BG, padx=12)
        self.code_label.grid(row=1, column=1, sticky="w")
        cb.bind("<<ComboboxSelected>>", self._on_lang_change)

    def _on_lang_change(self, _=None):
        codes = LANGUAGES.get(self.lang_var.get(), ["en"])
        self.code_label.config(text=f"code: {', '.join(codes)}")
        # Reset cached reader when language changes
        global reader_instance, reader_languages
        reader_instance = None

    # ── Image panel ────────────────────────────────────────────────────────────
    def _build_image_panel(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="x", padx=30, pady=(4, 0))

        tk.Label(frm, text="INPUT IMAGE", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        self.preview_frame = tk.Frame(frm, bg=ENTRY_BG,
                                      width=720, height=180, relief="flat")
        self.preview_frame.pack(fill="x")
        self.preview_frame.pack_propagate(False)

        self.preview_label = tk.Label(
            self.preview_frame,
            text="No image selected\nClick 'Browse' to choose an image file",
            font=("Courier", 11), fg=SUBTEXT, bg=ENTRY_BG, justify="center")
        self.preview_label.place(relx=0.5, rely=0.5, anchor="center")

        tk.Frame(frm, bg=ACCENT, height=2).pack(fill="x")

        btn_row = tk.Frame(frm, bg=BG)
        btn_row.pack(fill="x", pady=(6, 0))

        browse_btn = tk.Button(btn_row, text="📂 Browse Image",
                               font=("Courier", 10, "bold"),
                               fg=TEXT, bg=ACCENT2, relief="flat",
                               activebackground=BTN_HV, cursor="hand2",
                               padx=12, pady=6, command=self._browse)
        browse_btn.pack(side="left")

        self.path_label = tk.Label(btn_row, text="", font=("Courier", 9),
                                   fg=SUBTEXT, bg=BG, anchor="w")
        self.path_label.pack(side="left", padx=10, fill="x", expand=True)

    def _browse(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff *.webp"),
                       ("All files", "*.*")])
        if not path:
            return
        self.img_path = path
        self.path_label.config(text=os.path.basename(path))
        self._show_preview(path)

    def _show_preview(self, path):
        try:
            img = Image.open(path)
            img.thumbnail((720, 175))
            photo = ImageTk.PhotoImage(img)
            self.preview_label.config(image=photo, text="")
            self.preview_label.image = photo
        except Exception:
            self.preview_label.config(image="", text="Preview unavailable")

    # ── Run button ─────────────────────────────────────────────────────────────
    def _build_run_button(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(pady=12)

        self.run_btn = tk.Button(frm, text="RUN OCR  ➜",
                                 font=("Courier", 13, "bold"),
                                 fg=TEXT, bg=ACCENT, activebackground=BTN_HV,
                                 relief="flat", cursor="hand2",
                                 padx=28, pady=10, command=self._run_ocr_thread)
        self.run_btn.pack()
        self.run_btn.bind("<Enter>", lambda e: self.run_btn.config(bg=BTN_HV))
        self.run_btn.bind("<Leave>", lambda e: self.run_btn.config(bg=ACCENT))

    # ── Output area ────────────────────────────────────────────────────────────
    def _build_output(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="both", expand=True, padx=30)

        tk.Label(frm, text="EXTRACTED TEXT", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        box = tk.Frame(frm, bg=ACCENT2, padx=1, pady=1)
        box.pack(fill="both", expand=True)

        scroll = tk.Scrollbar(box)
        scroll.pack(side="right", fill="y")

        self.output_text = tk.Text(box, font=("Georgia", 12),
                                   bg=PANEL, fg=ACCENT,
                                   insertbackground=ACCENT,
                                   relief="flat", padx=10, pady=8,
                                   wrap="word", state="disabled", bd=0,
                                   yscrollcommand=scroll.set)
        self.output_text.pack(fill="both", expand=True)
        scroll.config(command=self.output_text.yview)

        btn_row = tk.Frame(frm, bg=BG)
        btn_row.pack(fill="x", pady=(4, 0))

        self.copy_btn = tk.Button(btn_row, text="📋 Copy",
                                  font=("Courier", 9), fg=SUBTEXT, bg=BG,
                                  relief="flat", cursor="hand2",
                                  activeforeground=TEXT, command=self._copy)
        self.copy_btn.pack(side="right")

        save_btn = tk.Button(btn_row, text="💾 Save as .txt",
                             font=("Courier", 9), fg=SUBTEXT, bg=BG,
                             relief="flat", cursor="hand2",
                             activeforeground=TEXT, command=self._save)
        save_btn.pack(side="right", padx=(0, 10))

    # ── Footer ─────────────────────────────────────────────────────────────────
    def _build_footer(self):
        self.status_var = tk.StringVar(value="Ready — select an image and click RUN OCR")
        tk.Label(self, textvariable=self.status_var,
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(pady=(4, 6))

    # ── OCR logic (runs in thread so UI stays responsive) ─────────────────────
    def _run_ocr_thread(self):
        if not self.img_path or not os.path.exists(self.img_path):
            messagebox.showwarning("No Image", "Please select an image file first.")
            return
        self.run_btn.config(text="Processing…", state="disabled")
        self.status_var.set("Loading OCR model… (first run downloads ~100MB)")
        self.update_idletasks()
        threading.Thread(target=self._run_ocr, daemon=True).start()

    def _run_ocr(self):
        try:
            lang_list = LANGUAGES.get(self.lang_var.get(), ["en"])
            self._set_status(f"Initialising EasyOCR for {self.lang_var.get()}…")
            reader  = get_reader(lang_list)

            self._set_status("Running OCR on image…")
            results = reader.readtext(self.img_path)

            # results: list of (bbox, text, confidence)
            lines = []
            for (_, text, confidence) in results:
                lines.append(f"{text}   [{confidence:.1%}]")

            output = "\n".join(lines) if lines else "No text detected."
            self.after(0, self._set_output, output)
            self.after(0, self._set_status,
                       f"Done — {len(lines)} text region(s) found.")

        except ImportError:
            self.after(0, messagebox.showerror, "Missing Package",
                "easyocr is not installed.\n\nRun:\n"
                "  python.exe -m pip install easyocr Pillow")
            self.after(0, self._set_status, "Error: easyocr not installed.")
        except Exception as e:
            self.after(0, messagebox.showerror, "OCR Error", str(e))
            self.after(0, self._set_status, f"Error: {e}")
        finally:
            self.after(0, self.run_btn.config,
                       {"text": "RUN OCR  ➜", "state": "normal"})

    def _set_status(self, msg):
        self.status_var.set(msg)

    def _set_output(self, text):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", text)
        self.output_text.config(state="disabled")

    def _copy(self):
        result = self.output_text.get("1.0", "end").strip()
        if result:
            self.clipboard_clear()
            self.clipboard_append(result)
            self.copy_btn.config(text="✅ Copied!")
            self.after(1500, lambda: self.copy_btn.config(text="📋 Copy"))

    def _save(self):
        result = self.output_text.get("1.0", "end").strip()
        if not result:
            messagebox.showwarning("Nothing to save", "Run OCR first.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text file", "*.txt")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(result)
            self.status_var.set(f"Saved to {os.path.basename(path)}")


if __name__ == "__main__":
    app = OCRApp()
    app.mainloop()