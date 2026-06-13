import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import socket
import threading
import time

# ================= COLORS =================
BG = "#1A1A2E"
PANEL = "#16213E"
ACCENT = "#E94560"
ACCENT2 = "#0F3460"
TEXT = "#EAEAEA"
SUBTEXT = "#8892A4"
GREEN = "#2ECC71"

# ================= APP =================
class PortScannerApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Port Scanner")
        self.geometry("850x650")
        self.configure(bg=BG)
        self.resizable(False, False)

        self.open_ports = []

        self.build_header()
        self.build_body()

    # =====================================
    # HEADER
    # =====================================
    def build_header(self):

        header = tk.Frame(self, bg=ACCENT2, pady=15)
        header.pack(fill="x")

        tk.Label(
            header,
            text="🔍 PORT SCANNER",
            font=("Georgia", 22, "bold"),
            bg=ACCENT2,
            fg=TEXT
        ).pack()

        tk.Label(
            header,
            text="Scan hosts and discover open ports",
            font=("Arial", 10),
            bg=ACCENT2,
            fg=SUBTEXT
        ).pack()

    # =====================================
    # BODY
    # =====================================
    def build_body(self):

        container = tk.Frame(self, bg=BG)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Target
        tk.Label(
            container,
            text="Target Host/IP",
            bg=BG,
            fg=TEXT,
            font=("Arial", 11, "bold")
        ).pack(anchor="w")

        self.host_entry = tk.Entry(
            container,
            font=("Arial", 12),
            bg=PANEL,
            fg=TEXT,
            insertbackground=TEXT
        )
        self.host_entry.pack(fill="x", pady=5)

        # Port range
        port_frame = tk.Frame(container, bg=BG)
        port_frame.pack(fill="x", pady=10)

        tk.Label(
            port_frame,
            text="Start Port",
            bg=BG,
            fg=TEXT
        ).pack(side="left")

        self.start_port = tk.Entry(port_frame, width=10)
        self.start_port.insert(0, "1")
        self.start_port.pack(side="left", padx=5)

        tk.Label(
            port_frame,
            text="End Port",
            bg=BG,
            fg=TEXT
        ).pack(side="left", padx=10)

        self.end_port = tk.Entry(port_frame, width=10)
        self.end_port.insert(0, "1024")
        self.end_port.pack(side="left")

        # Scan Button
        self.scan_btn = tk.Button(
            container,
            text="🔍 START SCAN",
            bg=ACCENT,
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.start_scan
        )
        self.scan_btn.pack(pady=15)

        # Progress Bar
        self.progress = ttk.Progressbar(
            container,
            length=750,
            mode="determinate"
        )
        self.progress.pack()

        self.status = tk.Label(
            container,
            text="Ready",
            bg=BG,
            fg=SUBTEXT,
            font=("Arial", 10)
        )
        self.status.pack(pady=5)

        # Results
        tk.Label(
            container,
            text="Open Ports",
            bg=BG,
            fg=TEXT,
            font=("Arial", 12, "bold")
        ).pack(anchor="w", pady=(15,5))

        self.results = tk.Text(
            container,
            bg=PANEL,
            fg=GREEN,
            height=18,
            font=("Consolas", 11)
        )
        self.results.pack(fill="both", expand=True)

        # Bottom buttons
        bottom = tk.Frame(container, bg=BG)
        bottom.pack(fill="x", pady=10)

        tk.Button(
            bottom,
            text="💾 Save Results",
            command=self.save_results
        ).pack(side="left")

        tk.Button(
            bottom,
            text="❌ Exit",
            command=self.destroy
        ).pack(side="right")

    # =====================================
    # START SCAN
    # =====================================
    def start_scan(self):

        host = self.host_entry.get().strip()

        if not host:
            messagebox.showerror(
                "Error",
                "Enter host name or IP"
            )
            return

        self.results.delete("1.0", "end")
        self.open_ports.clear()

        threading.Thread(
            target=self.scan_ports,
            daemon=True
        ).start()

    # =====================================
    # SCAN
    # =====================================
    def scan_ports(self):

        host = self.host_entry.get().strip()
        start_port = int(self.start_port.get())
        end_port = int(self.end_port.get())

        try:
            ip = socket.gethostbyname(host)
        except:
            messagebox.showerror(
                "Error",
                "Unable to resolve host"
            )
            return

        total_ports = end_port - start_port + 1

        start_time = time.time()

        self.status.config(
            text=f"Scanning {ip} ..."
        )

        for count, port in enumerate(
            range(start_port, end_port + 1)
        ):

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(0.5)

            result = sock.connect_ex(
                (ip, port)
            )

            if result == 0:

                self.open_ports.append(port)

                self.results.insert(
                    "end",
                    f"Port {port:<5} OPEN\n"
                )

                self.results.see("end")

            sock.close()

            percent = (
                (count + 1)
                / total_ports
            ) * 100

            self.progress["value"] = percent

        elapsed = round(
            time.time() - start_time,
            2
        )

        self.status.config(
            text=f"Completed | "
                 f"{len(self.open_ports)} open ports | "
                 f"{elapsed}s"
        )

    # =====================================
    # SAVE
    # =====================================
    def save_results(self):

        if not self.open_ports:
            messagebox.showinfo(
                "Info",
                "No results to save."
            )
            return

        file = filedialog.asksaveasfilename(
            defaultextension=".txt"
        )

        if file:

            with open(file, "w") as f:

                f.write(
                    "OPEN PORTS\n\n"
                )

                for port in self.open_ports:
                    f.write(
                        f"Port {port} OPEN\n"
                    )

            messagebox.showinfo(
                "Saved",
                "Results saved successfully."
            )

# ================= RUN =================
if __name__ == "__main__":
    app = PortScannerApp()
    app.mainloop()