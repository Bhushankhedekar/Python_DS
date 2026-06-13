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
GREEN    = "#2ECC71"
YELLOW   = "#F39C12"

# ── Steganography core (original logic preserved, bugs fixed) ──────────────────
FLAG    = '%'
LOC_MAX = (4, 1)
LOC_MIN = (3, 2)
ALPHA   = 1

TABLE = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
], dtype=np.float32)


def encode_char(blocks, data):
    data = ord(data)
    for idx in range(len(blocks)):
        bit_val = (data >> idx) & 1
        max_val = max(blocks[idx][LOC_MAX], blocks[idx][LOC_MIN])
        min_val = min(blocks[idx][LOC_MAX], blocks[idx][LOC_MIN])
        if max_val - min_val <= ALPHA:
            max_val = min_val + ALPHA + 1e-3
        if bit_val == 1:
            blocks[idx][LOC_MAX] = max_val
            blocks[idx][LOC_MIN] = min_val
        else:
            blocks[idx][LOC_MAX] = min_val
            blocks[idx][LOC_MIN] = max_val


def decode_char(blocks):
    val = 0
    for idx in range(len(blocks)):
        if blocks[idx][LOC_MAX] > blocks[idx][LOC_MIN]:
            val |= 1 << idx
    return chr(val)


def insert(path: str, txt: str) -> str:
    """
    Embed txt into image at path using DCT steganography.
    Fix: use ValueError instead of assert for friendlier error messages.
    Returns path of output image.
    """
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
    if img is None:
        raise ValueError("Could not read image file.")

    txt = "{}{}{}".format(len(txt), FLAG, txt)
    row, col = img.shape[:2]
    max_bytes = (row // 8) * (col // 8) // 8

    if max_bytes < len(txt):
        raise ValueError(
            f"Message too long! Max capacity: {max_bytes - 10} characters "
            f"for this image size ({col}×{row}).")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(img)
    y = y.astype(np.float32)

    blocks = []
    for r_idx in range(0, 8 * (row // 8), 8):
        for c_idx in range(0, 8 * (col // 8), 8):
            quantized = cv2.dct(y[r_idx:r_idx+8, c_idx:c_idx+8]) / TABLE
            blocks.append(quantized)

    for idx in range(len(txt)):
        encode_char(blocks[idx*8:(idx+1)*8], txt[idx])

    idx = 0
    for r_idx in range(0, 8 * (row // 8), 8):
        for c_idx in range(0, 8 * (col // 8), 8):
            y[r_idx:r_idx+8, c_idx:c_idx+8] = cv2.idct(blocks[idx] * TABLE)
            idx += 1

    y = np.clip(y, 0, 255).astype(np.uint8)   # Fix: clip before cast to avoid overflow
    img = cv2.cvtColor(cv2.merge((y, u, v)), cv2.COLOR_YUV2BGR)

    filename, _ = osp.splitext(path)
    out_path = filename + '_dct_embedded.jpg'
    cv2.imwrite(out_path, img)
    return out_path


def extract(path: str) -> str:
    """
    Extract hidden message from a DCT-embedded image.
    Fix: raise ValueError instead of assert for user-friendly errors.
    """
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
    if img is None:
        raise ValueError("Could not read image file.")

    row, col = img.shape[:2]
    max_bytes = (row // 8) * (col // 8) // 8

    img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(img)
    y = y.astype(np.float32)

    blocks = []
    for r_idx in range(0, 8 * (row // 8), 8):
        for c_idx in range(0, 8 * (col // 8), 8):
            quantized = cv2.dct(y[r_idx:r_idx+8, c_idx:c_idx+8]) / TABLE
            blocks.append(quantized)

    res = ''
    idx = 0
    while idx < max_bytes:
        ch = decode_char(blocks[idx*8:(idx+1)*8])
        idx += 1
        if ch == FLAG:
            break
        res += ch

    # Fix: validate length string before int() conversion
    if not res.isdigit():
        raise ValueError("No hidden message found in this image, "
                         "or image was not embedded with this tool.")

    end = int(res) + idx
    if end > max_bytes:
        raise ValueError("Image doesn't appear to contain a valid hidden message.")

    result = ''
    while idx < end:
        result += decode_char(blocks[idx*8:(idx+1)*8])
        idx += 1
    return result


def get_capacity(path: str) -> int:
    """Return max characters this image can hold."""
    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR)
    if img is None:
        return 0
    row, col = img.shape[:2]
    return (row // 8) * (col // 8) // 8 - 10  # subtract header overhead


# ── GUI ────────────────────────────────────────────────────────────────────────
class SteganographyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DCT Image Steganography")
        self.geometry("780x680")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.img_path = None

        self._build_header()
        self._build_tabs()
        self._build_footer()

    # ── Header ─────────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self, bg=ACCENT2, pady=14)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🔐  DCT Image Steganography",
                 font=("Georgia", 20, "bold"), fg=TEXT, bg=ACCENT2).pack()
        tk.Label(hdr, text="Hide secret messages inside images using DCT frequency manipulation",
                 font=("Georgia", 9), fg=SUBTEXT, bg=ACCENT2).pack()

    # ── Tabs: Embed / Extract ──────────────────────────────────────────────────
    def _build_tabs(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook",           background=BG, borderwidth=0)
        style.configure("TNotebook.Tab",       background=ACCENT2, foreground=TEXT,
                        font=("Courier", 11, "bold"), padding=(20, 8))
        style.map("TNotebook.Tab",
                  background=[("selected", ACCENT)],
                  foreground=[("selected", TEXT)])

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True, padx=0, pady=0)

        self.embed_tab  = tk.Frame(nb, bg=BG)
        self.extract_tab = tk.Frame(nb, bg=BG)
        nb.add(self.embed_tab,   text="  🔒 Embed Message  ")
        nb.add(self.extract_tab, text="  🔓 Extract Message  ")

        self._build_embed_tab()
        self._build_extract_tab()

    # ── EMBED TAB ──────────────────────────────────────────────────────────────
    def _build_embed_tab(self):
        frm = self.embed_tab

        # Image selector
        img_frm = tk.Frame(frm, bg=BG)
        img_frm.pack(fill="x", padx=30, pady=(16, 0))

        tk.Label(img_frm, text="COVER IMAGE", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        self.embed_preview = tk.Label(img_frm, bg=ENTRY_BG,
                                      text="No image selected\nClick Browse to choose a PNG or BMP",
                                      font=("Courier", 10), fg=SUBTEXT,
                                      width=80, height=8, justify="center")
        self.embed_preview.pack(fill="x")
        tk.Frame(img_frm, bg=ACCENT, height=2).pack(fill="x")

        btn_row = tk.Frame(img_frm, bg=BG)
        btn_row.pack(fill="x", pady=(6, 0))
        tk.Button(btn_row, text="📂 Browse Image",
                  font=("Courier", 10, "bold"), fg=TEXT, bg=ACCENT2,
                  relief="flat", activebackground=BTN_HV, cursor="hand2",
                  padx=12, pady=6,
                  command=self._browse_embed).pack(side="left")
        self.embed_path_label = tk.Label(btn_row, text="", font=("Courier", 9),
                                         fg=SUBTEXT, bg=BG)
        self.embed_path_label.pack(side="left", padx=10)
        self.capacity_label = tk.Label(btn_row, text="", font=("Courier", 9),
                                       fg=ACCENT, bg=BG)
        self.capacity_label.pack(side="right")

        # Message input
        msg_frm = tk.Frame(frm, bg=BG)
        msg_frm.pack(fill="x", padx=30, pady=(14, 0))

        tk.Label(msg_frm, text="SECRET MESSAGE", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        box = tk.Frame(msg_frm, bg=ACCENT, padx=1, pady=1)
        box.pack(fill="x")
        self.embed_msg = tk.Text(box, height=5, font=("Georgia", 12),
                                 bg=ENTRY_BG, fg=TEXT, insertbackground=ACCENT,
                                 relief="flat", padx=10, pady=8, wrap="word", bd=0)
        self.embed_msg.pack(fill="x")
        self.embed_msg.bind("<KeyRelease>", self._update_char_count)

        self.char_count_var = tk.StringVar(value="0 characters")
        tk.Label(msg_frm, textvariable=self.char_count_var,
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(anchor="e")

        # Embed button
        btn_frm = tk.Frame(frm, bg=BG)
        btn_frm.pack(pady=14)
        self.embed_btn = tk.Button(btn_frm, text="🔒 EMBED MESSAGE  ➜",
                                   font=("Courier", 13, "bold"),
                                   fg=TEXT, bg=ACCENT, activebackground=BTN_HV,
                                   relief="flat", cursor="hand2",
                                   padx=24, pady=10,
                                   command=self._run_embed)
        self.embed_btn.pack()
        self.embed_btn.bind("<Enter>", lambda e: self.embed_btn.config(bg=BTN_HV))
        self.embed_btn.bind("<Leave>", lambda e: self.embed_btn.config(bg=ACCENT))

        self.embed_status = tk.StringVar(value="Select an image and enter your message")
        tk.Label(btn_frm, textvariable=self.embed_status,
                 font=("Courier", 9), fg=SUBTEXT, bg=BG).pack(pady=(4, 0))

    # ── EXTRACT TAB ────────────────────────────────────────────────────────────
    def _build_extract_tab(self):
        frm = self.extract_tab

        img_frm = tk.Frame(frm, bg=BG)
        img_frm.pack(fill="x", padx=30, pady=(16, 0))

        tk.Label(img_frm, text="EMBEDDED IMAGE", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        self.extract_preview = tk.Label(img_frm, bg=ENTRY_BG,
                                        text="No image selected\nClick Browse to choose an embedded image",
                                        font=("Courier", 10), fg=SUBTEXT,
                                        width=80, height=8, justify="center")
        self.extract_preview.pack(fill="x")
        tk.Frame(img_frm, bg=ACCENT2, height=2).pack(fill="x")

        btn_row = tk.Frame(img_frm, bg=BG)
        btn_row.pack(fill="x", pady=(6, 0))
        tk.Button(btn_row, text="📂 Browse Image",
                  font=("Courier", 10, "bold"), fg=TEXT, bg=ACCENT2,
                  relief="flat", activebackground=BTN_HV, cursor="hand2",
                  padx=12, pady=6,
                  command=self._browse_extract).pack(side="left")
        self.extract_path_label = tk.Label(btn_row, text="", font=("Courier", 9),
                                           fg=SUBTEXT, bg=BG)
        self.extract_path_label.pack(side="left", padx=10)

        # Extract button
        btn_frm = tk.Frame(frm, bg=BG)
        btn_frm.pack(pady=14)
        self.extract_btn = tk.Button(btn_frm, text="🔓 EXTRACT MESSAGE  ➜",
                                     font=("Courier", 13, "bold"),
                                     fg=TEXT, bg=ACCENT2, activebackground=BTN_HV,
                                     relief="flat", cursor="hand2",
                                     padx=24, pady=10,
                                     command=self._run_extract)
        self.extract_btn.pack()
        self.extract_btn.bind("<Enter>", lambda e: self.extract_btn.config(bg=BTN_HV))
        self.extract_btn.bind("<Leave>", lambda e: self.extract_btn.config(bg=ACCENT2))

        # Output
        out_frm = tk.Frame(frm, bg=BG)
        out_frm.pack(fill="both", expand=True, padx=30)

        tk.Label(out_frm, text="EXTRACTED MESSAGE", font=("Courier", 9, "bold"),
                 fg=SUBTEXT, bg=BG).pack(anchor="w")

        box = tk.Frame(out_frm, bg=ACCENT2, padx=1, pady=1)
        box.pack(fill="both", expand=True)
        self.extract_output = tk.Text(box, font=("Georgia", 12),
                                      bg=PANEL, fg=GREEN,
                                      insertbackground=ACCENT,
                                      relief="flat", padx=10, pady=8,
                                      wrap="word", state="disabled", bd=0)
        self.extract_output.pack(fill="both", expand=True)

        copy_row = tk.Frame(out_frm, bg=BG)
        copy_row.pack(fill="x", pady=(4, 0))
        self.copy_btn = tk.Button(copy_row, text="📋 Copy", font=("Courier", 9),
                                  fg=SUBTEXT, bg=BG, relief="flat",
                                  cursor="hand2", activeforeground=TEXT,
                                  command=self._copy_extracted)
        self.copy_btn.pack(side="right")

        self.extract_status = tk.StringVar(value="Select an embedded image and click Extract")
        tk.Label(out_frm, textvariable=self.extract_status,
                 font=("Courier", 9), fg=SUBTEXT, bg=BG).pack(anchor="w", pady=(4, 0))

    # ── Footer ─────────────────────────────────────────────────────────────────
    def _build_footer(self):
        tk.Label(self,
                 text="Use PNG or BMP for embedding — JPG compression may reduce accuracy",
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(pady=(2, 6))

    # ── Browse helpers ─────────────────────────────────────────────────────────
    def _browse_embed(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.bmp *.jpg *.jpeg"),
                       ("All files", "*.*")])
        if not path:
            return
        self.embed_img_path = path
        self.embed_path_label.config(text=os.path.basename(path))
        cap = get_capacity(path)
        self.capacity_label.config(text=f"Capacity: ~{cap} chars")
        self._show_preview(path, self.embed_preview)

    def _browse_extract(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.bmp *.jpg *.jpeg"),
                       ("All files", "*.*")])
        if not path:
            return
        self.extract_img_path = path
        self.extract_path_label.config(text=os.path.basename(path))
        self._show_preview(path, self.extract_preview)

    def _show_preview(self, path, label_widget):
        try:
            img = Image.open(path)
            img.thumbnail((720, 140))
            photo = ImageTk.PhotoImage(img)
            label_widget.config(image=photo, text="")
            label_widget.image = photo
        except Exception:
            label_widget.config(image="", text="Preview unavailable")

    def _update_char_count(self, _=None):
        n = len(self.embed_msg.get("1.0", "end").strip())
        self.char_count_var.set(f"{n} character{'s' if n != 1 else ''}")

    # ── Embed ──────────────────────────────────────────────────────────────────
    def _run_embed(self):
        if not hasattr(self, 'embed_img_path'):
            messagebox.showwarning("No Image", "Please select a cover image first.")
            return
        msg = self.embed_msg.get("1.0", "end").strip()
        if not msg:
            messagebox.showwarning("No Message", "Please enter a secret message.")
            return
        self.embed_btn.config(text="Processing…", state="disabled")
        self.embed_status.set("Embedding message…")
        threading.Thread(target=self._do_embed, args=(msg,), daemon=True).start()

    def _do_embed(self, msg):
        try:
            out_path = insert(self.embed_img_path, msg)
            self.after(0, self.embed_status.set,
                       f"✅ Saved: {os.path.basename(out_path)}")
            self.after(0, messagebox.showinfo, "Done",
                       f"Message embedded successfully!\n\nSaved to:\n{out_path}")
        except ValueError as e:
            self.after(0, messagebox.showerror, "Error", str(e))
            self.after(0, self.embed_status.set, f"❌ {e}")
        except Exception as e:
            self.after(0, messagebox.showerror, "Unexpected Error", str(e))
        finally:
            self.after(0, self.embed_btn.config,
                       {"text": "🔒 EMBED MESSAGE  ➜", "state": "normal"})

    # ── Extract ────────────────────────────────────────────────────────────────
    def _run_extract(self):
        if not hasattr(self, 'extract_img_path'):
            messagebox.showwarning("No Image", "Please select an embedded image first.")
            return
        self.extract_btn.config(text="Processing…", state="disabled")
        self.extract_status.set("Extracting message…")
        threading.Thread(target=self._do_extract, daemon=True).start()

    def _do_extract(self):
        try:
            result = extract(self.extract_img_path)
            self.after(0, self._set_extracted, result)
            self.after(0, self.extract_status.set,
                       f"✅ Extracted {len(result)} character(s).")
        except ValueError as e:
            self.after(0, messagebox.showerror, "Error", str(e))
            self.after(0, self.extract_status.set, f"❌ {e}")
        except Exception as e:
            self.after(0, messagebox.showerror, "Unexpected Error", str(e))
        finally:
            self.after(0, self.extract_btn.config,
                       {"text": "🔓 EXTRACT MESSAGE  ➜", "state": "normal"})

    def _set_extracted(self, text):
        self.extract_output.config(state="normal")
        self.extract_output.delete("1.0", "end")
        self.extract_output.insert("end", text)
        self.extract_output.config(state="disabled")

    def _copy_extracted(self):
        content = self.extract_output.get("1.0", "end").strip()
        if content:
            self.clipboard_clear()
            self.clipboard_append(content)
            self.copy_btn.config(text="✅ Copied!")
            self.after(1500, lambda: self.copy_btn.config(text="📋 Copy"))


if __name__ == "__main__":
    app = SteganographyApp()
    app.mainloop()