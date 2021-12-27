import tkinter as tk
from tkinter import filedialog, Text
import os 


root = tk.Tk()
apps = [] 

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title = "Select a file", filetypes=(("Executable", "*.exe"),("All files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg ="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=600, width=600, bg="#263D42")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)


#add buttons
openFile = tk.Button(root,text="Open File", padx=10, pady=10, fg="white" ,bg="#263D42", command=addApp)
openFile.pack()

runApps = openFile = tk.Button(root,text="Run Apps", padx=10, pady=10, fg="white" ,bg="#263D42",command=runApps)
runApps.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
