from tkinter import *
from tkinter.ttk import *
import PIL
import os
import fnmatch
from tkinter import messagebox as popup
files = []
recentpaths = []
class File:
    def __init__(self, row, column, filepath, filename):
        if os.path.isfile(filepath):
            self.image = PhotoImage(file=os.getcwd() + "/icons/blank.png")
        else:
            self.image = PhotoImage(file=os.getcwd() + "/icons/Folder-0.png")
            if filename == "Downloads":
                self.image = PhotoImage(file=os.getcwd() + "/icons/Folder Downloads-0.png")
        if filename.endswith(".zip"):
            self.image = PhotoImage(file=os.getcwd() + "/icons/Zip-0.png")
        elif filename.endswith(".exe"):
            self.image = PhotoImage(file=os.getcwd() + "/icons/exe-0.png")
        elif filename.endswith(".mp3") | filename.endswith(".wav") | filename.endswith(".ogg"):
            self.image = PhotoImage(file=os.getcwd() + "/icons/Audio-0.png")
        elif filename.endswith(".mp4") | filename.endswith(".vid"):
            self.image = PhotoImage(file=os.getcwd() + "/icons/Video file-0.png")
        elif filename.endswith(".png") | filename.endswith(".jpg") | filename.endswith(".jpeg") | filename.endswith(".ico"):
            self.image = PhotoImage(file=os.getcwd() + "/icons/Photos file-0.png")
        self.btn = Button(app, text=filename, command=lambda:self.openfile(), image=self.image, compound="top")
        self.btn.grid(row=row, column=column)
        self.filename = filename
        self.filepath = filepath
        files.append(self)
    def openfile(self):
        global path, recentpaths
        if os.path.isfile(self.filepath):
            os.system("mousepad " + self.filepath)
        else:
            recentpaths.append(path)
            path += self.filename + "/"
            opendir()
    def delete(self):
        self.btn.destroy()
def goback():
    global path, recentpaths
    print(recentpaths)
    try:
        path = recentpaths[len(recentpaths) - 1]
        recentpaths.pop(len(recentpaths) - 1)
    except:
        popup.showwarning("File Manager", "No more history")
    print(recentpaths)
    opendir()
def goto(e):
    global path
    recentpaths.append(path)
    if pathvar.get().endswith("/"):
        path = pathvar.get()
    else:
        path = pathvar.get() + "/"
    opendir()
app = Tk()
app.title("File Manager")
app.geometry("1050x1050")
app.config(bg="white")
app.call("source", os.getcwd() + "/arc/arc.tcl")
app.iconphoto(False, PhotoImage(file=os.getcwd() + "/icons/Folder-0.png"))
Style(app).theme_use("arc")
Button(app, text="<-- Back <--", command=goback).grid(row=0, column=0,ipadx=5, ipady=15)
pathvar = StringVar()
pathentry = Entry(app, textvariable=pathvar)
pathentry.bind('<KeyRelease-Return>', goto)
pathentry.grid(row=0, column=1, ipadx=5, ipady=15)
path = os.getcwd()
def opendir():
    global files, pathvar
    pathvar.set(path)
    for file in files:
        file.delete()
    files = []
    print(files)
    print("-" * 64 + "Done" + "-" * 64)
    row = 1
    column = 0
    for file in os.listdir(path):
        if column == 14:
            column = 0
            row += 1
        File(row, column, path + file, file)
        column += 1
    print(files)
    print("-" * 64 + "Path" + "-" * 64)
    print(path)
opendir()
app.mainloop()
