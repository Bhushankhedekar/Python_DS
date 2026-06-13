import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# ── Language data ─────────────────────────────────────────────────────────────
LANGUAGES = {
    "Bengali":    "bn",
    "English":    "en",
    "Korean":     "ko",
    "French":     "fr",
    "German":     "de",
    "Hebrew":     "he",
    "Hindi":      "hi",
    "Italian":    "it",
    "Japanese":   "ja",
    "Latin":      "la",
    "Malay":      "ms",
    "Nepali":     "ne",
    "Russian":    "ru",
    "Arabic":     "ar",
    "Chinese":    "zh-CN",
    "Spanish":    "es",
}
LANG_NAMES = list(LANGUAGES.keys())

# ── Colour palette ─────────────────────────────────────────────────────────────
BG        = "#1A1A2E"   # deep navy
PANEL     = "#16213E"   # slightly lighter panel
ACCENT    = "#E94560"   # vivid red-pink
ACCENT2   = "#0F3460"   # mid-blue
TEXT      = "#EAEAEA"
SUBTEXT   = "#8892A4"
ENTRY_BG  = "#0D1B2A"
BTN_HV    = "#FF6B81"

class TranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Translator")
        self.geometry("700x560")
        self.resizable(False, False)
        self.configure(bg=BG)

        self._build_header()
        self._build_lang_row()
        self._build_text_area()
        self._build_button()
        self._build_output()
        self._build_footer()

    # ── Header ────────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self, bg=ACCENT2, pady=14)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🌐  Language Translator",
                 font=("Georgia", 20, "bold"),
                 fg=TEXT, bg=ACCENT2).pack()
        tk.Label(hdr, text="Powered by Google Translate",
                 font=("Georgia", 9), fg=SUBTEXT, bg=ACCENT2).pack()

    # ── Language selector row ─────────────────────────────────────────────────
    def _build_lang_row(self):
        row = tk.Frame(self, bg=BG, pady=14)
        row.pack(fill="x", padx=30)

        # Source language
        tk.Label(row, text="FROM", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).grid(row=0, column=0, sticky="w")
        self.src_var = tk.StringVar(value="Auto Detect")
        src_choices = ["Auto Detect"] + LANG_NAMES
        self.src_cb = ttk.Combobox(row, textvariable=self.src_var,
                                   values=src_choices, state="readonly",
                                   width=20, font=("Courier", 11))
        self.src_cb.grid(row=1, column=0, sticky="w")

        # Arrow
        tk.Label(row, text="  →  ", font=("Arial", 18),
                 fg=ACCENT, bg=BG).grid(row=1, column=1, padx=8)

        # Target language
        tk.Label(row, text="TO", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).grid(row=0, column=2, sticky="w")
        self.tgt_var = tk.StringVar(value="French")
        self.tgt_cb = ttk.Combobox(row, textvariable=self.tgt_var,
                                   values=LANG_NAMES, state="readonly",
                                   width=20, font=("Courier", 11))
        self.tgt_cb.grid(row=1, column=2, sticky="w")

        # Swap button
        swap_btn = tk.Button(row, text="⇄ Swap", font=("Courier", 10, "bold"),
                             fg=TEXT, bg=ACCENT2, relief="flat",
                             activebackground=BTN_HV, cursor="hand2",
                             command=self._swap_languages, padx=10, pady=4)
        swap_btn.grid(row=1, column=3, padx=(20, 0))

        # Style comboboxes
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox",
                        fieldbackground=ENTRY_BG, background=ACCENT2,
                        foreground=TEXT, selectbackground=ACCENT,
                        borderwidth=0, relief="flat")

    # ── Input text area ───────────────────────────────────────────────────────
    def _build_text_area(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="x", padx=30, pady=(6, 0))

        tk.Label(frm, text="INPUT TEXT", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        box = tk.Frame(frm, bg=ACCENT, padx=1, pady=1)   # accent border
        box.pack(fill="x")
        self.input_text = tk.Text(box, height=5, font=("Georgia", 12),
                                  bg=ENTRY_BG, fg=TEXT, insertbackground=ACCENT,
                                  relief="flat", padx=10, pady=8, wrap="word",
                                  bd=0)
        self.input_text.pack(fill="x")
        self.input_text.bind("<Control-Return>", lambda e: self._translate())

        tk.Label(frm, text="Ctrl+Enter to translate",
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(anchor="e")

    # ── Translate button ──────────────────────────────────────────────────────
    def _build_button(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(pady=10)

        self.trans_btn = tk.Button(
            frm, text="TRANSLATE  ➜",
            font=("Courier", 13, "bold"),
            fg=TEXT, bg=ACCENT, activebackground=BTN_HV,
            relief="flat", cursor="hand2",
            padx=28, pady=10,
            command=self._translate
        )
        self.trans_btn.pack()
        self.trans_btn.bind("<Enter>", lambda e: self.trans_btn.config(bg=BTN_HV))
        self.trans_btn.bind("<Leave>", lambda e: self.trans_btn.config(bg=ACCENT))

        # Clear button
        clr = tk.Button(frm, text="Clear", font=("Courier", 9),
                        fg=SUBTEXT, bg=BG, relief="flat", cursor="hand2",
                        activeforeground=TEXT, command=self._clear)
        clr.pack(pady=(4, 0))

    # ── Output area ───────────────────────────────────────────────────────────
    def _build_output(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="x", padx=30)

        tk.Label(frm, text="TRANSLATION", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        box = tk.Frame(frm, bg=ACCENT2, padx=1, pady=1)
        box.pack(fill="x")
        self.output_text = tk.Text(box, height=5, font=("Georgia", 12),
                                   bg=PANEL, fg=ACCENT,
                                   insertbackground=ACCENT,
                                   relief="flat", padx=10, pady=8, wrap="word",
                                   state="disabled", bd=0)
        self.output_text.pack(fill="x")

        # Copy button
        self.copy_btn = tk.Button(frm, text="📋 Copy", font=("Courier", 9),
                                  fg=SUBTEXT, bg=BG, relief="flat",
                                  cursor="hand2", activeforeground=TEXT,
                                  command=self._copy)
        self.copy_btn.pack(anchor="e", pady=(3, 0))

    # ── Footer ────────────────────────────────────────────────────────────────
    def _build_footer(self):
        tk.Label(self, text="16 languages supported",
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(pady=(6, 0))

    # ── Actions ───────────────────────────────────────────────────────────────
    def _translate(self):
        text = self.input_text.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Empty Input", "Please enter text to translate.")
            return

        src_name = self.src_var.get()
        src_code = "auto" if src_name == "Auto Detect" else LANGUAGES[src_name]
        tgt_code = LANGUAGES[self.tgt_var.get()]

        try:
            self.trans_btn.config(text="Translating…", state="disabled")
            self.update_idletasks()
            result = GoogleTranslator(source=src_code, target=tgt_code).translate(text)
            self._set_output(result)
        except Exception as err:
            messagebox.showerror("Translation Error", str(err))
        finally:
            self.trans_btn.config(text="TRANSLATE  ➜", state="normal")

    def _set_output(self, text):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", text)
        self.output_text.config(state="disabled")

    def _clear(self):
        self.input_text.delete("1.0", "end")
        self._set_output("")

    def _swap_languages(self):
        src = self.src_var.get()
        tgt = self.tgt_var.get()
        if src == "Auto Detect":
            return
        self.src_var.set(tgt)
        self.tgt_var.set(src)

    def _copy(self):
        result = self.output_text.get("1.0", "end").strip()
        if result:
            self.clipboard_clear()
            self.clipboard_append(result)
            self.copy_btn.config(text="✅ Copied!")
            self.after(1500, lambda: self.copy_btn.config(text="📋 Copy"))


if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()