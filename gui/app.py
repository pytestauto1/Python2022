import tkinter as tk
from tkinter import filedialog, Text
import os 


root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=600, bg="#263D42")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)

root.mainloop()
