import tkinter as tk
from tkinter import filedialog

def pick_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory()
    return folder_path
