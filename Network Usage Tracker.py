import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import socket
import time

# ================= COLORS =================
BG = "#1A1A2E"
PANEL = "#16213E"
ACCENT = "#E94560"
ACCENT2 = "#0F3460"
TEXT = "#EAEAEA"
SUBTEXT = "#8892A4"
GREEN = "#2ECC71"
RED = "#E74C3C"

# ================= APP =================
class NetworkTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Network Usage Tracker")
        self.geometry("900x650")
        self.configure(bg=BG)
        self.resizable(False, False)

        self.old_sent = psutil.net_io_counters().bytes_sent
        self.old_recv = psutil.net_io_counters().bytes_recv

        self.monitoring = True
        self.max_limit_mb = 1

        self.build_header()
        self.build_dashboard()
        self.build_footer()

        self.update_network()

    # =====================================
    # HEADER
    # =====================================
    def build_header(self):
        header = tk.Frame(self, bg=ACCENT2, pady=15)
        header.pack(fill="x")

        tk.Label(
            header,
            text="🌐 NETWORK USAGE TRACKER",
            font=("Georgia", 22, "bold"),
            fg=TEXT,
            bg=ACCENT2
        ).pack()

        tk.Label(
            header,
            text="Monitor Upload, Download Speed and Connection Status",
            font=("Arial", 10),
            fg=SUBTEXT,
            bg=ACCENT2
        ).pack()

    # =====================================
    # DASHBOARD
    # =====================================
    def build_dashboard(self):

        dashboard = tk.Frame(self, bg=BG)
        dashboard.pack(fill="both", expand=True, padx=20, pady=20)

        # ---------- Upload Card ----------
        upload_frame = tk.Frame(
            dashboard,
            bg=PANEL,
            width=400,
            height=150
        )
        upload_frame.grid(row=0, column=0, padx=10, pady=10)
        upload_frame.grid_propagate(False)

        tk.Label(
            upload_frame,
            text="⬆ Upload Speed",
            font=("Arial", 16, "bold"),
            bg=PANEL,
            fg=TEXT
        ).pack(pady=15)

        self.upload_label = tk.Label(
            upload_frame,
            text="0 KB/s",
            font=("Arial", 24, "bold"),
            fg=GREEN,
            bg=PANEL
        )
        self.upload_label.pack()

        # ---------- Download Card ----------
        download_frame = tk.Frame(
            dashboard,
            bg=PANEL,
            width=400,
            height=150
        )
        download_frame.grid(row=0, column=1, padx=10, pady=10)
        download_frame.grid_propagate(False)

        tk.Label(
            download_frame,
            text="⬇ Download Speed",
            font=("Arial", 16, "bold"),
            bg=PANEL,
            fg=TEXT
        ).pack(pady=15)

        self.download_label = tk.Label(
            download_frame,
            text="0 KB/s",
            font=("Arial", 24, "bold"),
            fg=GREEN,
            bg=PANEL
        )
        self.download_label.pack()

        # ---------- Progress Card ----------
        usage_frame = tk.Frame(
            dashboard,
            bg=PANEL,
            width=820,
            height=150
        )
        usage_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )
        usage_frame.grid_propagate(False)

        tk.Label(
            usage_frame,
            text="Bandwidth Usage",
            font=("Arial", 16, "bold"),
            bg=PANEL,
            fg=TEXT
        ).pack(pady=10)

        self.progress = ttk.Progressbar(
            usage_frame,
            orient="horizontal",
            length=700,
            mode="determinate"
        )
        self.progress.pack(pady=10)

        self.usage_label = tk.Label(
            usage_frame,
            text="Usage: 0 KB/s",
            font=("Arial", 14),
            fg=TEXT,
            bg=PANEL
        )
        self.usage_label.pack()

        # ---------- Connection Status ----------
        status_frame = tk.Frame(
            dashboard,
            bg=PANEL,
            width=820,
            height=170
        )
        status_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )
        status_frame.grid_propagate(False)

        tk.Label(
            status_frame,
            text="Connection Status",
            font=("Arial", 16, "bold"),
            fg=TEXT,
            bg=PANEL
        ).pack(pady=10)

        self.status_label = tk.Label(
            status_frame,
            text="Checking...",
            font=("Arial", 18),
            fg=GREEN,
            bg=PANEL
        )
        self.status_label.pack()

        # ---------- Buttons ----------
        btn_frame = tk.Frame(dashboard, bg=BG)
        btn_frame.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=15
        )

        self.start_btn = tk.Button(
            btn_frame,
            text="▶ Start",
            font=("Arial", 12, "bold"),
            bg=GREEN,
            fg="white",
            relief="flat",
            padx=20,
            command=self.start_monitoring
        )
        self.start_btn.pack(side="left", padx=10)

        self.stop_btn = tk.Button(
            btn_frame,
            text="⏹ Stop",
            font=("Arial", 12, "bold"),
            bg=ACCENT,
            fg="white",
            relief="flat",
            padx=20,
            command=self.stop_monitoring
        )
        self.stop_btn.pack(side="left", padx=10)

        self.exit_btn = tk.Button(
            btn_frame,
            text="❌ Exit",
            font=("Arial", 12, "bold"),
            bg=RED,
            fg="white",
            relief="flat",
            padx=20,
            command=self.exit_app
        )
        self.exit_btn.pack(side="left", padx=10)

    # =====================================
    # FOOTER
    # =====================================
    def build_footer(self):
        tk.Label(
            self,
            text="Maximum Recommended Limit : 1 MB/s",
            bg=BG,
            fg=SUBTEXT,
            font=("Arial", 9)
        ).pack(pady=5)

    # =====================================
    # START
    # =====================================
    def start_monitoring(self):
        self.monitoring = True

    # =====================================
    # STOP
    # =====================================
    def stop_monitoring(self):
        self.monitoring = False

    # =====================================
    # EXIT
    # =====================================
    def exit_app(self):
        if messagebox.askyesno(
            "Exit",
            "Do you want to exit?"
        ):
            self.destroy()

    # =====================================
    # UPDATE NETWORK
    # =====================================
    def update_network(self):

        if self.monitoring:

            counters = psutil.net_io_counters()

            new_sent = counters.bytes_sent
            new_recv = counters.bytes_recv

            upload_speed = (new_sent - self.old_sent) / 1024
            download_speed = (new_recv - self.old_recv) / 1024

            total_usage = upload_speed + download_speed

            self.upload_label.config(
                text=f"{upload_speed:.2f} KB/s"
            )

            self.download_label.config(
                text=f"{download_speed:.2f} KB/s"
            )

            self.usage_label.config(
                text=f"Usage : {total_usage:.2f} KB/s"
            )

            # Progress Bar
            percent = min(
                (total_usage / 1024) * 100,
                100
            )

            self.progress["value"] = percent

            # Connection Status
            try:
                ip = socket.gethostbyname(
                    socket.gethostname()
                )

                self.status_label.config(
                    text=f"🟢 Connected\nIP Address : {ip}",
                    fg=GREEN
                )

            except:
                self.status_label.config(
                    text="🔴 No Internet Connection",
                    fg=RED
                )

            # Alert
            if total_usage > 1024:
                messagebox.showwarning(
                    "Bandwidth Alert",
                    "Usage exceeded 1 MB/s"
                )

            self.old_sent = new_sent
            self.old_recv = new_recv

        self.after(1000, self.update_network)


# ================= RUN =================
if __name__ == "__main__":
    app = NetworkTrackerApp()
    app.protocol(
        "WM_DELETE_WINDOW",
        app.exit_app
    )
    app.mainloop()