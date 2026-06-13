import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import threading
import datetime
import os

# ── Colour palette ─────────────────────────────────────────────────────────────
BG       = "#1A1A2E"
PANEL    = "#16213E"
ACCENT   = "#E94560"
ACCENT2  = "#0F3460"
TEXT     = "#EAEAEA"
SUBTEXT  = "#8892A4"
ENTRY_BG = "#0D1B2A"
BTN_HV   = "#FF6B81"
USER_CLR = "#E94560"
BOT_CLR  = "#2ECC71"
SYS_CLR  = "#8892A4"

# ── Bot command logic (ported from wechaty bot) ────────────────────────────────
contacts   = {}   # simulated contact list
room_members = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
aliases    = {}
login_user = "Me"

def handle_command(text: str) -> str:
    """
    Process commands exactly as the original wechaty bot did.
    Returns bot response string.
    """
    text = text.strip()

    # ── ding → dong (original core feature) ───────────────────────────────────
    if text.lower() == "ding":
        return "dong 🔔"

    # ── get room members ───────────────────────────────────────────────────────
    if text.lower() == "get room members":
        return "Room members:\n" + "\n".join(f"• {m}" for m in room_members)

    # ── remove room member ─────────────────────────────────────────────────────
    if text.lower().startswith("remove room member:"):
        name = text[len("remove room member:"):].strip()
        if name in room_members:
            room_members.remove(name)
            return f'✅ Removed "{name}" from the room.'
        return f'❌ Could not find room member "{name}".'

    # ── get room topic ─────────────────────────────────────────────────────────
    if text.lower().startswith("get room topic"):
        return "📌 Current room topic: Wechaty Python Bot Demo"

    # ── rename room topic ──────────────────────────────────────────────────────
    if text.lower().startswith("rename room topic:"):
        new_topic = text[len("rename room topic:"):].strip()
        return f'✅ Room topic renamed to: "{new_topic}"'

    # ── add new friend ─────────────────────────────────────────────────────────
    if text.lower().startswith("add new friend:"):
        info = text[len("add new friend:"):].strip()
        contacts[info] = info
        return f'✅ Friend request sent to "{info}" with message: "hello world ..."'

    # ── at me ──────────────────────────────────────────────────────────────────
    if text.lower().startswith("at me"):
        return f"@{login_user} hello 👋"

    # ── my alias ───────────────────────────────────────────────────────────────
    if text.lower() == "my alias":
        alias = aliases.get(login_user, "")
        return f"Your alias is: {alias or '(none set)'}"

    # ── set alias ──────────────────────────────────────────────────────────────
    if text.lower().startswith("set alias:"):
        new_alias = text[len("set alias:"):].strip()
        aliases[login_user] = new_alias
        return f'✅ Your new alias is: "{new_alias}"'

    # ── find friends ───────────────────────────────────────────────────────────
    if text.lower().startswith("find friends:"):
        name = text[len("find friends:"):].strip()
        found = [c for c in room_members if name.lower() in c.lower()]
        if found:
            return f"Found {len(found)} friend(s):\n" + "\n".join(f"• {f}" for f in found)
        return f'❌ No friends found matching "{name}".'

    # ── help ───────────────────────────────────────────────────────────────────
    if text.lower() in ("help", "commands", "?"):
        return (
            "📋 Available commands:\n"
            "• ding → replies dong\n"
            "• get room members\n"
            "• remove room member: <name>\n"
            "• get room topic\n"
            "• rename room topic: <new topic>\n"
            "• add new friend: <name/phone>\n"
            "• at me\n"
            "• my alias\n"
            "• set alias: <alias>\n"
            "• find friends: <name>\n"
            "• clear  — clear chat\n"
            "• save   — save chat log"
        )

    # ── clear / save handled in GUI ────────────────────────────────────────────
    if text.lower() == "clear":
        return "__CLEAR__"
    if text.lower() == "save":
        return "__SAVE__"

    # ── default: echo with timestamp ───────────────────────────────────────────
    return f'🤖 I received: "{text}"\nType "help" to see available commands.'


# ── GUI ────────────────────────────────────────────────────────────────────────
class ChatbotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wechaty-Style Chatbot")
        self.geometry("700x620")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.chat_log = []   # stores (sender, text, time) for saving

        self._build_header()
        self._build_chat_area()
        self._build_input_area()
        self._build_footer()

        # Welcome message
        self._post_message("System",
            "🟢 Bot online. Type 'help' for commands or just chat!", SYS_CLR)

    # ── Header ─────────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self, bg=ACCENT2, pady=12)
        hdr.pack(fill="x")

        left = tk.Frame(hdr, bg=ACCENT2)
        left.pack(side="left", padx=16)

        # Avatar circle
        canvas = tk.Canvas(left, width=40, height=40, bg=ACCENT2,
                           highlightthickness=0)
        canvas.pack(side="left")
        canvas.create_oval(2, 2, 38, 38, fill=ACCENT, outline="")
        canvas.create_text(20, 20, text="🤖", font=("Arial", 16))

        info = tk.Frame(left, bg=ACCENT2)
        info.pack(side="left", padx=10)
        tk.Label(info, text="Wechaty Bot",
                 font=("Georgia", 14, "bold"), fg=TEXT, bg=ACCENT2).pack(anchor="w")
        self.status_label = tk.Label(info, text="● Online",
                                     font=("Courier", 9), fg=BOT_CLR, bg=ACCENT2)
        self.status_label.pack(anchor="w")

        # Save button in header
        tk.Button(hdr, text="💾 Save Chat",
                  font=("Courier", 9, "bold"),
                  fg=TEXT, bg=ACCENT2, relief="flat",
                  activebackground=BTN_HV, cursor="hand2",
                  padx=10, pady=4,
                  command=self._save_chat).pack(side="right", padx=16)

        tk.Button(hdr, text="🗑 Clear",
                  font=("Courier", 9, "bold"),
                  fg=TEXT, bg=ACCENT2, relief="flat",
                  activebackground=BTN_HV, cursor="hand2",
                  padx=10, pady=4,
                  command=self._clear_chat).pack(side="right")

    # ── Chat display ───────────────────────────────────────────────────────────
    def _build_chat_area(self):
        frm = tk.Frame(self, bg=BG)
        frm.pack(fill="both", expand=True, padx=0, pady=0)

        self.chat_area = scrolledtext.ScrolledText(
            frm, font=("Georgia", 11),
            bg=PANEL, fg=TEXT,
            insertbackground=ACCENT,
            relief="flat", bd=0,
            padx=16, pady=12,
            wrap="word", state="disabled",
            cursor="arrow"
        )
        self.chat_area.pack(fill="both", expand=True)

        # Text tags for colours
        self.chat_area.tag_config("user",   foreground=USER_CLR, font=("Georgia", 11, "bold"))
        self.chat_area.tag_config("bot",    foreground=BOT_CLR,  font=("Georgia", 11, "bold"))
        self.chat_area.tag_config("system", foreground=SYS_CLR,  font=("Courier", 9, "italic"))
        self.chat_area.tag_config("time",   foreground=SUBTEXT,  font=("Courier", 8))
        self.chat_area.tag_config("body",   foreground=TEXT,     font=("Georgia", 11))

    # ── Input area ─────────────────────────────────────────────────────────────
    def _build_input_area(self):
        frm = tk.Frame(self, bg=ACCENT2, pady=10, padx=16)
        frm.pack(fill="x", side="bottom")

        self.input_var = tk.StringVar()
        self.input_box = tk.Entry(frm, textvariable=self.input_var,
                                  font=("Georgia", 12),
                                  bg=ENTRY_BG, fg=TEXT,
                                  insertbackground=ACCENT,
                                  relief="flat", bd=0)
        self.input_box.pack(side="left", fill="x", expand=True,
                            ipady=10, padx=(0, 10))
        self.input_box.bind("<Return>", lambda e: self._send())
        self.input_box.focus()

        send_btn = tk.Button(frm, text="Send ➜",
                             font=("Courier", 11, "bold"),
                             fg=TEXT, bg=ACCENT, activebackground=BTN_HV,
                             relief="flat", cursor="hand2",
                             padx=16, pady=8, command=self._send)
        send_btn.pack(side="right")

    # ── Footer ─────────────────────────────────────────────────────────────────
    def _build_footer(self):
        tk.Label(self, text='Tip: type "help" for all commands  •  Press Enter to send',
                 font=("Courier", 8), fg=SUBTEXT, bg=BG).pack(pady=(2, 4))

    # ── Message rendering ──────────────────────────────────────────────────────
    def _post_message(self, sender: str, text: str, color: str):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.chat_log.append((sender, text, now))

        self.chat_area.config(state="normal")
        self.chat_area.insert("end", f"\n{sender}  ", "user" if sender == "You" else
                              ("system" if sender == "System" else "bot"))
        self.chat_area.insert("end", f"[{now}]\n", "time")
        self.chat_area.insert("end", f"{text}\n", "body")
        self.chat_area.config(state="disabled")
        self.chat_area.see("end")

    # ── Send ───────────────────────────────────────────────────────────────────
    def _send(self):
        text = self.input_var.get().strip()
        if not text:
            return
        self.input_var.set("")
        self._post_message("You", text, USER_CLR)

        # Run bot response in thread so UI doesn't freeze
        threading.Thread(target=self._bot_reply, args=(text,), daemon=True).start()

    def _bot_reply(self, text: str):
        response = handle_command(text)
        if response == "__CLEAR__":
            self.after(0, self._clear_chat)
            return
        if response == "__SAVE__":
            self.after(0, self._save_chat)
            return
        self.after(0, self._post_message, "Bot", response, BOT_CLR)

    # ── Utility ────────────────────────────────────────────────────────────────
    def _clear_chat(self):
        self.chat_area.config(state="normal")
        self.chat_area.delete("1.0", "end")
        self.chat_area.config(state="disabled")
        self.chat_log.clear()
        self._post_message("System", "🗑 Chat cleared.", SYS_CLR)

    def _save_chat(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text file", "*.txt")])
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            f.write("=== Wechaty Bot Chat Log ===\n\n")
            for sender, msg, ts in self.chat_log:
                f.write(f"[{ts}] {sender}: {msg}\n")
        messagebox.showinfo("Saved", f"Chat saved to:\n{os.path.basename(path)}")


if __name__ == "__main__":
    app = ChatbotApp()
    app.mainloop()