import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
RED      = "#E74C3C"

# ── Core plagiarism logic ──────────────────────────────────────────────────────
def vectorize(texts):
    # Fix: create a fresh TfidfVectorizer each call to avoid state issues
    return TfidfVectorizer().fit_transform(texts).toarray()

def similarity(doc1, doc2):
    return cosine_similarity([doc1, doc2])[0][1]

def check_plagiarism(file_names, file_texts):
    """
    Returns list of (file_a, file_b, score) tuples sorted by score descending.
    Fix: use list instead of set so results are ordered and reproducible.
    """
    if len(file_texts) < 2:
        return []

    vectors    = vectorize(file_texts)
    s_vectors  = list(zip(file_names, vectors))
    results    = set()

    for i, (name_a, vec_a) in enumerate(s_vectors):
        for name_b, vec_b in s_vectors[i + 1:]:   # Fix: only forward pairs, no duplicates
            sim_score    = similarity(vec_a, vec_b)
            student_pair = sorted((name_a, name_b))
            results.add((student_pair[0], student_pair[1], round(float(sim_score), 4)))

    return sorted(results, key=lambda x: x[2], reverse=True)

def score_color(score):
    if score >= 0.8:  return RED
    if score >= 0.5:  return YELLOW
    return GREEN

def score_label(score):
    if score >= 0.8:  return "HIGH"
    if score >= 0.5:  return "MEDIUM"
    return "LOW"

# ── GUI ────────────────────────────────────────────────────────────────────────
class PlagiarismApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plagiarism Checker")
        self.geometry("820x680")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.loaded_files = {}   # filename → content

        self._build_header()
        self._build_file_panel()
        self._build_run_button()
        self._build_results()
        self._build_footer()

    # ── Header ─────────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self, bg=ACCENT2, pady=14)
        hdr.pack(fill="x")
        tk.Label(hdr, text="📄  Plagiarism Checker",
                 font=("Georgia", 20, "bold"), fg=TEXT, bg=ACCENT2).pack()
        tk.Label(hdr, text="TF-IDF cosine similarity across text documents",
                 font=("Georgia", 9), fg=SUBTEXT, bg=ACCENT2).pack()

    # ── File loader panel ──────────────────────────────────────────────────────
    def _build_file_panel(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="x", padx=30, pady=(14, 0))

        tk.Label(frm, text="DOCUMENTS", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        # File list box
        box = tk.Frame(frm, bg=ACCENT2, padx=1, pady=1)
        box.pack(fill="x")

        scroll = tk.Scrollbar(box)
        scroll.pack(side="right", fill="y")

        self.file_listbox = tk.Listbox(box, height=7,
                                       font=("Courier", 10),
                                       bg=ENTRY_BG, fg=TEXT,
                                       selectbackground=ACCENT,
                                       activestyle="none",
                                       relief="flat", bd=0,
                                       yscrollcommand=scroll.set)
        self.file_listbox.pack(fill="x", side="left", expand=True)
        scroll.config(command=self.file_listbox.yview)

        # Buttons row
        btn_row = tk.Frame(frm, bg=BG)
        btn_row.pack(fill="x", pady=(8, 0))

        tk.Button(btn_row, text="📂 Add Files",
                  font=("Courier", 10, "bold"),
                  fg=TEXT, bg=ACCENT2, relief="flat",
                  activebackground=BTN_HV, cursor="hand2",
                  padx=12, pady=6,
                  command=self._add_files).pack(side="left")

        tk.Button(btn_row, text="📁 Add Folder",
                  font=("Courier", 10, "bold"),
                  fg=TEXT, bg=ACCENT2, relief="flat",
                  activebackground=BTN_HV, cursor="hand2",
                  padx=12, pady=6,
                  command=self._add_folder).pack(side="left", padx=(8, 0))

        tk.Button(btn_row, text="🗑 Remove Selected",
                  font=("Courier", 10),
                  fg=SUBTEXT, bg=BG, relief="flat",
                  cursor="hand2", activeforeground=TEXT,
                  command=self._remove_selected).pack(side="left", padx=(8, 0))

        tk.Button(btn_row, text="Clear All",
                  font=("Courier", 10),
                  fg=SUBTEXT, bg=BG, relief="flat",
                  cursor="hand2", activeforeground=TEXT,
                  command=self._clear_all).pack(side="right")

        self.file_count_var = tk.StringVar(value="No files loaded")
        tk.Label(btn_row, textvariable=self.file_count_var,
                 font=("Courier", 9), fg=SUBTEXT, bg=BG).pack(side="right", padx=10)

    # ── Run button ─────────────────────────────────────────────────────────────
    def _build_run_button(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(pady=12)

        self.run_btn = tk.Button(frm, text="CHECK PLAGIARISM  ➜",
                                 font=("Courier", 13, "bold"),
                                 fg=TEXT, bg=ACCENT, activebackground=BTN_HV,
                                 relief="flat", cursor="hand2",
                                 padx=24, pady=10,
                                 command=self._run_check)
        self.run_btn.pack()
        self.run_btn.bind("<Enter>", lambda e: self.run_btn.config(bg=BTN_HV))
        self.run_btn.bind("<Leave>", lambda e: self.run_btn.config(bg=ACCENT))

    # ── Results table ──────────────────────────────────────────────────────────
    def _build_results(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="both", expand=True, padx=30)

        tk.Label(frm, text="RESULTS", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        # Legend
        legend = tk.Frame(frm, bg=BG)
        legend.pack(anchor="w", pady=(2, 6))
        for color, label, rng in [(GREEN, "LOW", "< 50%"),
                                   (YELLOW, "MEDIUM", "50–80%"),
                                   (RED,    "HIGH",   "≥ 80%")]:
            tk.Label(legend, text="█", font=("Courier", 12),
                     fg=color, bg=BG).pack(side="left")
            tk.Label(legend, text=f" {label} ({rng})   ",
                     font=("Courier", 9), fg=SUBTEXT, bg=BG).pack(side="left")

        # Treeview table
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview",
                        background=PANEL, foreground=TEXT,
                        fieldbackground=PANEL, rowheight=28,
                        font=("Courier", 10))
        style.configure("Custom.Treeview.Heading",
                        background=ACCENT2, foreground=TEXT,
                        font=("Courier", 10, "bold"), relief="flat")
        style.map("Custom.Treeview",
                  background=[("selected", ACCENT)],
                  foreground=[("selected", TEXT)])

        cols = ("doc_a", "doc_b", "score", "level")
        self.tree = ttk.Treeview(frm, columns=cols, show="headings",
                                 style="Custom.Treeview")
        self.tree.heading("doc_a",  text="Document A")
        self.tree.heading("doc_b",  text="Document B")
        self.tree.heading("score",  text="Similarity")
        self.tree.heading("level",  text="Risk Level")
        self.tree.column("doc_a",  width=270, anchor="w")
        self.tree.column("doc_b",  width=270, anchor="w")
        self.tree.column("score",  width=100, anchor="center")
        self.tree.column("level",  width=100, anchor="center")

        # Tag colours for rows
        self.tree.tag_configure("high",   foreground=RED)
        self.tree.tag_configure("medium", foreground=YELLOW)
        self.tree.tag_configure("low",    foreground=GREEN)

        vsb = ttk.Scrollbar(frm, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

    # ── Footer ─────────────────────────────────────────────────────────────────
    def _build_footer(self):
        self.status_var = tk.StringVar(value="Add at least 2 documents and click Check")
        tk.Label(self, textvariable=self.status_var,
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(pady=(4, 6))

    # ── File management ────────────────────────────────────────────────────────
    def _add_files(self):
        paths = filedialog.askopenfilenames(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        for path in paths:
            name = os.path.basename(path)
            if name not in self.loaded_files:
                try:
                    with open(path, encoding='utf-8', errors='ignore') as f:
                        self.loaded_files[name] = f.read()
                    self.file_listbox.insert("end", name)
                except Exception as e:
                    messagebox.showerror("Read Error", f"Could not read {name}:\n{e}")
        self._update_count()

    def _add_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return
        added = 0
        for fname in os.listdir(folder):
            if fname.endswith('.txt') and fname not in self.loaded_files:
                path = os.path.join(folder, fname)
                try:
                    with open(path, encoding='utf-8', errors='ignore') as f:
                        self.loaded_files[fname] = f.read()
                    self.file_listbox.insert("end", fname)
                    added += 1
                except Exception:
                    pass
        self.status_var.set(f"Added {added} file(s) from folder.")
        self._update_count()

    def _remove_selected(self):
        selected = self.file_listbox.curselection()
        for i in reversed(selected):
            name = self.file_listbox.get(i)
            self.file_listbox.delete(i)
            self.loaded_files.pop(name, None)
        self._update_count()

    def _clear_all(self):
        self.file_listbox.delete(0, "end")
        self.loaded_files.clear()
        self._clear_results()
        self._update_count()

    def _update_count(self):
        n = len(self.loaded_files)
        self.file_count_var.set(f"{n} file{'s' if n != 1 else ''} loaded")

    # ── Check ──────────────────────────────────────────────────────────────────
    def _run_check(self):
        if len(self.loaded_files) < 2:
            messagebox.showwarning("Not Enough Files",
                                   "Please load at least 2 text files to compare.")
            return

        self._clear_results()
        self.status_var.set("Analysing…")
        self.update_idletasks()

        try:
            names  = list(self.loaded_files.keys())
            texts  = list(self.loaded_files.values())
            results = check_plagiarism(names, texts)

            for (a, b, score) in results:
                pct   = f"{score * 100:.1f}%"
                level = score_label(score)
                tag   = level.lower()
                self.tree.insert("", "end",
                                 values=(a, b, pct, level),
                                 tags=(tag,))

            high = sum(1 for _, _, s in results if s >= 0.8)
            self.status_var.set(
                f"{len(results)} pair(s) compared — {high} high-similarity pair(s) found.")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Error during analysis.")

    def _clear_results(self):
        for row in self.tree.get_children():
            self.tree.delete(row)


if __name__ == "__main__":
    app = PlagiarismApp()
    app.mainloop()