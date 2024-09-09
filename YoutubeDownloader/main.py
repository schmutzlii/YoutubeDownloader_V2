import tkinter as tk
import os
from pathlib import Path
from tkinter import ttk
from download import Downloader
from gui import GUI
from pytube import cipher

PATH_SAVE = os.path.join(Path.home(), "Downloads")
EXTENSION = ".webm"

def main():
    root = tk.Tk()
    root.title("YouTube Downloader")
    downloader = Downloader(PATH_SAVE, EXTENSION)
    gui = GUI(root, downloader)

    root.mainloop()

if __name__ == "__main__":
    main()
