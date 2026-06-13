import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import os

# ── Colour palette (matches translator style) ──────────────────────────────────
BG       = "#1A1A2E"
PANEL    = "#16213E"
ACCENT   = "#E94560"
ACCENT2  = "#0F3460"
TEXT     = "#EAEAEA"
SUBTEXT  = "#8892A4"
ENTRY_BG = "#0D1B2A"
BTN_HV   = "#FF6B81"

# ── Markov chain logic ────────────────────────────────────────────────────────
lexicon = {}

def update_lexicon(current: str, next_word: str) -> None:
    """Add or increment transition count for current→next_word."""
    if current not in lexicon:
        lexicon[current] = {next_word: 1}
        return
    options = lexicon[current]
    options[next_word] = options.get(next_word, 0) + 1

def build_lexicon(text: str) -> int:
    """Build lexicon from raw text string. Returns word count."""
    lexicon.clear()
    words = text.split()
    for i in range(len(words) - 1):
        # Fix: normalise to lowercase so 'The' and 'the' merge
        update_lexicon(words[i].lower(), words[i + 1].lower())
    # Normalise counts → probabilities
    for word, transitions in lexicon.items():
        total = sum(transitions.values())
        lexicon[word] = {k: v / total for k, v in transitions.items()}
    return len(words)

def predict_next(sentence: str, n: int = 5) -> list[str]:
    """
    Return up to n predicted next words for the last word in sentence.
    Fix: sort by probability so top suggestions show first.
    """
    word = sentence.strip().split()[-1].lower() if sentence.strip() else ""
    if word not in lexicon:
        return []
    options = lexicon[word]
    # Sort by probability descending
    sorted_opts = sorted(options.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_opts[:n]]

def generate_sentence(seed: str, length: int = 8) -> str:
    """
    Fix: generate a full sentence by chaining predictions.
    Stops early if a word has no known successor.
    """
    words = seed.strip().lower().split()
    for _ in range(length):
        last = words[-1]
        if last not in lexicon:
            break
        options = lexicon[last]
        next_w = np.random.choice(list(options.keys()), p=list(options.values()))
        words.append(next_w)
    return " ".join(words)

# ── GUI ───────────────────────────────────────────────────────────────────────
class WordPredictorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Word Predictor — Markov Chain")
        self.geometry("700x620")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.dataset_loaded = False

        self._build_header()
        self._build_dataset_row()
        self._build_input()
        self._build_suggestions()
        self._build_buttons()
        self._build_output()
        self._build_footer()

        # Load built-in sample text so app works without a file
        self._load_sample()

    # ── Header ────────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self, bg=ACCENT2, pady=14)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🔮  Word Predictor",
                 font=("Georgia", 20, "bold"), fg=TEXT, bg=ACCENT2).pack()
        tk.Label(hdr, text="Markov Chain next-word prediction",
                 font=("Georgia", 9), fg=SUBTEXT, bg=ACCENT2).pack()

    # ── Dataset row ───────────────────────────────────────────────────────────
    def _build_dataset_row(self):
        row = tk.Frame(self, bg=BG, pady=10)
        row.pack(fill="x", padx=30)

        tk.Label(row, text="DATASET", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        inner = tk.Frame(row, bg=BG)
        inner.pack(fill="x")

        self.dataset_label = tk.Label(inner, text="Using built-in sample text",
                                      font=("Courier", 10), fg=ACCENT,
                                      bg=ENTRY_BG, anchor="w", padx=8, pady=6)
        self.dataset_label.pack(side="left", fill="x", expand=True)

        load_btn = tk.Button(inner, text="📂 Load .txt",
                             font=("Courier", 10, "bold"),
                             fg=TEXT, bg=ACCENT2, relief="flat",
                             activebackground=BTN_HV, cursor="hand2",
                             padx=10, pady=6, command=self._load_file)
        load_btn.pack(side="right", padx=(8, 0))

    # ── Input ─────────────────────────────────────────────────────────────────
    def _build_input(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="x", padx=30, pady=(10, 0))

        tk.Label(frm, text="TYPE YOUR TEXT", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        box = tk.Frame(frm, bg=ACCENT, padx=1, pady=1)
        box.pack(fill="x")
        self.input_text = tk.Text(box, height=4, font=("Georgia", 12),
                                  bg=ENTRY_BG, fg=TEXT, insertbackground=ACCENT,
                                  relief="flat", padx=10, pady=8, wrap="word", bd=0)
        self.input_text.pack(fill="x")
        # Live suggestions as user types
        self.input_text.bind("<KeyRelease>", self._on_key)
        tk.Label(frm, text="Suggestions update as you type",
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(anchor="e")

    # ── Suggestion chips ──────────────────────────────────────────────────────
    def _build_suggestions(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="x", padx=30, pady=(8, 0))

        tk.Label(frm, text="SUGGESTIONS  (click to append)",
                 font=("Courier", 9, "bold"), fg=SUBTEXT, bg=BG).pack(anchor="w")

        self.chip_frame = tk.Frame(frm, bg=BG)
        self.chip_frame.pack(fill="x", pady=(4, 0))
        self.chips = []

    def _refresh_chips(self, suggestions):
        for c in self.chips:
            c.destroy()
        self.chips = []
        for word in suggestions:
            btn = tk.Button(self.chip_frame, text=word,
                            font=("Courier", 10), fg=TEXT, bg=ACCENT2,
                            relief="flat", cursor="hand2", padx=10, pady=4,
                            activebackground=BTN_HV,
                            command=lambda w=word: self._append_word(w))
            btn.pack(side="left", padx=(0, 6))
            self.chips.append(btn)

    def _append_word(self, word):
        current = self.input_text.get("1.0", "end").strip()
        self.input_text.delete("1.0", "end")
        self.input_text.insert("end", current + " " + word)
        self._on_key(None)

    # ── Action buttons ────────────────────────────────────────────────────────
    def _build_buttons(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(pady=12)

        self.gen_btn = tk.Button(frm, text="GENERATE SENTENCE  ➜",
                                 font=("Courier", 13, "bold"),
                                 fg=TEXT, bg=ACCENT, activebackground=BTN_HV,
                                 relief="flat", cursor="hand2",
                                 padx=24, pady=10, command=self._generate)
        self.gen_btn.pack(side="left", padx=(0, 10))
        self.gen_btn.bind("<Enter>", lambda e: self.gen_btn.config(bg=BTN_HV))
        self.gen_btn.bind("<Leave>", lambda e: self.gen_btn.config(bg=ACCENT))

        clr = tk.Button(frm, text="Clear", font=("Courier", 9),
                        fg=SUBTEXT, bg=BG, relief="flat", cursor="hand2",
                        activeforeground=TEXT, command=self._clear)
        clr.pack(side="left")

        # Word count spinner
        tk.Label(frm, text="  Words:", font=("Courier", 10),
                 fg=SUBTEXT, bg=BG).pack(side="left", padx=(16, 4))
        self.word_count = tk.IntVar(value=8)
        sb = tk.Spinbox(frm, from_=1, to=50, textvariable=self.word_count,
                        width=4, font=("Courier", 10),
                        bg=ENTRY_BG, fg=TEXT, buttonbackground=ACCENT2,
                        relief="flat", insertbackground=ACCENT)
        sb.pack(side="left")

    # ── Output ────────────────────────────────────────────────────────────────
    def _build_output(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="x", padx=30)

        tk.Label(frm, text="GENERATED TEXT", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        box = tk.Frame(frm, bg=ACCENT2, padx=1, pady=1)
        box.pack(fill="x")
        self.output_text = tk.Text(box, height=5, font=("Georgia", 12),
                                   bg=PANEL, fg=ACCENT,
                                   insertbackground=ACCENT,
                                   relief="flat", padx=10, pady=8,
                                   wrap="word", state="disabled", bd=0)
        self.output_text.pack(fill="x")

        self.copy_btn = tk.Button(frm, text="📋 Copy", font=("Courier", 9),
                                  fg=SUBTEXT, bg=BG, relief="flat",
                                  cursor="hand2", activeforeground=TEXT,
                                  command=self._copy)
        self.copy_btn.pack(anchor="e", pady=(3, 0))

    # ── Footer ────────────────────────────────────────────────────────────────
    def _build_footer(self):
        self.footer_var = tk.StringVar(value="")
        tk.Label(self, textvariable=self.footer_var,
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(pady=(6, 0))

    # ── Logic ─────────────────────────────────────────────────────────────────
    def _load_sample(self):
        sample = (
            "the cat sat on the mat the cat ate the rat "
            "the dog ran in the park the dog saw the cat "
            "she said hello to the world the world said hello back "
            "once upon a time there was a cat who sat on a mat "
            "the quick brown fox jumps over the lazy dog "
            "to be or not to be that is the question "
            "all that glitters is not gold the gold was hidden "
            "it was a dark and stormy night the night was long "
        )
        count = build_lexicon(sample)
        self.footer_var.set(f"Sample text loaded — {len(lexicon)} unique words, {count} total tokens")

    def _load_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not path:
            return
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
            count = build_lexicon(text)
            name = os.path.basename(path)
            self.dataset_label.config(text=name)
            self.footer_var.set(f"Loaded '{name}' — {len(lexicon)} unique words, {count} total tokens")
        except Exception as e:
            messagebox.showerror("Load Error", str(e))

    def _on_key(self, _event):
        text = self.input_text.get("1.0", "end").strip()
        if text:
            suggestions = predict_next(text, n=5)
            self._refresh_chips(suggestions)
        else:
            self._refresh_chips([])

    def _generate(self):
        seed = self.input_text.get("1.0", "end").strip()
        if not seed:
            messagebox.showwarning("Empty Input", "Type some text first.")
            return
        last_word = seed.strip().split()[-1].lower()
        if last_word not in lexicon:
            self._set_output(f'Word "{last_word}" not found in dataset.')
            return
        result = generate_sentence(seed, length=self.word_count.get())
        self._set_output(result)

    def _set_output(self, text):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", text)
        self.output_text.config(state="disabled")

    def _clear(self):
        self.input_text.delete("1.0", "end")
        self._set_output("")
        self._refresh_chips([])

    def _copy(self):
        result = self.output_text.get("1.0", "end").strip()
        if result:
            self.clipboard_clear()
            self.clipboard_append(result)
            self.copy_btn.config(text="✅ Copied!")
            self.after(1500, lambda: self.copy_btn.config(text="📋 Copy"))


if __name__ == "__main__":
    app = WordPredictorApp()
    app.mainloop()