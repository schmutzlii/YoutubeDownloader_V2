import tkinter as tk
import time
from tkinter import ttk
from tkinter import messagebox

class GUI:
    def __init__(self, root, downloader):
        self.urls_to_download = []
        self.root = root
        self.downloader = downloader

        self.frame = ttk.Frame(root, padding="20")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame, text="").grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.url_text = tk.Text(self.frame, height=5, width=50)
        self.url_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.download_button = ttk.Button(self.frame, text="Download All", command=self.download)
        self.download_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.input_url_entry = ttk.Entry(self.frame, width=50)
        self.input_url_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.add_url_button = ttk.Button(self.frame, text="Add", command=self.add_url_to_list)
        self.add_url_button.grid(row=5, column=0, padx=10, pady=5)

        self.status_label = ttk.Label(self.frame, text="")
        self.status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def download(self):
        urls = self.url_text.get("1.0", tk.END).strip().split("\n")
        self.downloader.download_all_parallel(urls + self.urls_to_download)
        self.url_text.delete("1.0", tk.END)  # Clear the URL text field
        self.urls_to_download = []
        self.status_label.config(text="Downloads finished!")  # Update status label
        # Delete the status message after 3 seconds
        self.root.after(3000, self.clear_status_label)


    def add_url_to_list(self):
        url = self.input_url_entry.get()
        if url:
            self.urls_to_download.append(url)
            self.url_text.insert(tk.END, url + '\n')
            self.input_url_entry.delete(0, tk.END)

    def clear_status_label(self):
        self.status_label.config(text="")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

