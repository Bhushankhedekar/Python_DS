import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests
import threading
import csv
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
class WebsiteCheckerApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Website Connectivity Checker")
        self.geometry("900x650")
        self.configure(bg=BG)
        self.resizable(False, False)

        self.results_data = []

        self.build_header()
        self.build_body()

    # ================= HEADER =================
    def build_header(self):

        header = tk.Frame(self, bg=ACCENT2, pady=15)
        header.pack(fill="x")

        tk.Label(
            header,
            text="🌐 WEBSITE CONNECTIVITY CHECKER",
            font=("Georgia", 22, "bold"),
            fg=TEXT,
            bg=ACCENT2
        ).pack()

        tk.Label(
            header,
            text="Check Website Availability and Response Time",
            font=("Arial", 10),
            fg=SUBTEXT,
            bg=ACCENT2
        ).pack()

    # ================= BODY =================
    def build_body(self):

        container = tk.Frame(self, bg=BG)
        container.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(
            container,
            text="Website URL",
            font=("Arial", 11, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(anchor="w")

        self.url_entry = tk.Entry(
            container,
            font=("Arial", 12),
            bg=PANEL,
            fg=TEXT,
            insertbackground=TEXT
        )
        self.url_entry.pack(fill="x", pady=5)

        example = tk.Label(
            container,
            text="Example: https://www.google.com",
            fg=SUBTEXT,
            bg=BG,
            font=("Arial", 9)
        )
        example.pack(anchor="w")

        btn_frame = tk.Frame(container, bg=BG)
        btn_frame.pack(fill="x", pady=15)

        self.check_btn = tk.Button(
            btn_frame,
            text="🔍 CHECK WEBSITE",
            font=("Arial", 11, "bold"),
            bg=ACCENT,
            fg="white",
            command=self.start_check
        )
        self.check_btn.pack(side="left", padx=5)

        self.export_btn = tk.Button(
            btn_frame,
            text="💾 EXPORT CSV",
            font=("Arial", 11, "bold"),
            bg=GREEN,
            fg="white",
            command=self.export_csv
        )
        self.export_btn.pack(side="left", padx=5)

        self.clear_btn = tk.Button(
            btn_frame,
            text="🗑 CLEAR",
            font=("Arial", 11, "bold"),
            bg=ACCENT2,
            fg="white",
            command=self.clear_results
        )
        self.clear_btn.pack(side="left", padx=5)

        # Status
        self.status_label = tk.Label(
            container,
            text="Ready",
            font=("Arial", 10),
            fg=SUBTEXT,
            bg=BG
        )
        self.status_label.pack(anchor="w")

        # Table
        columns = (
            "Website",
            "Status",
            "Code",
            "Response Time"
        )

        self.tree = ttk.Treeview(
            container,
            columns=columns,
            show="headings",
            height=18
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200)

        self.tree.pack(fill="both", expand=True, pady=10)

        scrollbar = ttk.Scrollbar(
            self.tree,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

    # ================= CHECK =================
    def start_check(self):

        url = self.url_entry.get().strip()

        if not url:
            messagebox.showerror(
                "Error",
                "Please enter a website URL."
            )
            return

        threading.Thread(
            target=self.check_website,
            args=(url,),
            daemon=True
        ).start()

    # ================= WEBSITE CHECK =================
    def check_website(self, url):

        self.status_label.config(
            text=f"Checking {url}..."
        )

        try:

            start_time = time.time()

            response = requests.get(
                url,
                timeout=10
            )

            end_time = time.time()

            response_time = round(
                (end_time - start_time) * 1000,
                2
            )

            status_code = response.status_code

            status = (
                "Working"
                if status_code == 200
                else "Not Working"
            )

            self.results_data.append([
                url,
                status,
                status_code,
                f"{response_time} ms"
            ])

            self.tree.insert(
                "",
                "end",
                values=(
                    url,
                    status,
                    status_code,
                    f"{response_time} ms"
                )
            )

            self.status_label.config(
                text=f"Completed: {url}"
            )

        except Exception as e:

            self.results_data.append([
                url,
                "Offline",
                "-",
                "-"
            ])

            self.tree.insert(
                "",
                "end",
                values=(
                    url,
                    "Offline",
                    "-",
                    "-"
                )
            )

            self.status_label.config(
                text=f"Failed: {url}"
            )

    # ================= EXPORT =================
    def export_csv(self):

        if not self.results_data:
            messagebox.showinfo(
                "Info",
                "No data available."
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV File", "*.csv")]
        )

        if not file_path:
            return

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Website",
                "Status",
                "HTTP Code",
                "Response Time"
            ])

            writer.writerows(
                self.results_data
            )

        messagebox.showinfo(
            "Success",
            "CSV exported successfully."
        )

    # ================= CLEAR =================
    def clear_results(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.results_data.clear()

        self.status_label.config(
            text="Ready"
        )


# ================= RUN =================
if __name__ == "__main__":

    app = WebsiteCheckerApp()
    app.mainloop()