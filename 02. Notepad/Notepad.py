from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()
root.geometry("644x788")
root.title("Untitled - Notepad")


# Function
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)


def openfile():
    global file
    file = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(
            initialfile="Untitled.txt",
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
        )
    if file == "":
        file = None
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + "- Notepad")


def cut():
    text.event_generate(("<<Cut>>"))


def copy():
    text.event_generate(("<<Copy>>"))


def paste():
    text.event_generate(("<<Paste>>"))


def about():
    tmsg.showinfo(
        "Notepad",
        "This is a notepad by techabby. You can create new files, edit existing files, save data using this notepad.",
    )


# Text
text = Text(root, font=("Times New Roman", 14))
text.pack(fill=BOTH, expand=True)
file = None

# Menubar
menubar = Menu(root)
# File Menu
File_Menu = Menu(menubar, tearoff=0)
File_Menu.add_command(label="New File", command=newfile)
File_Menu.add_command(label="Open File", command=openfile)
File_Menu.add_command(label="Save File", command=savefile)
File_Menu.add_separator()
File_Menu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=File_Menu)

# Edit Menu
Edit_Menu = Menu(menubar, tearoff=0)
Edit_Menu.add_command(label="Cut", command=cut)
Edit_Menu.add_command(label="Copy", command=copy)
Edit_Menu.add_command(label="Paste", command=paste)
menubar.add_cascade(label="Edit", menu=Edit_Menu)

# Help Menu
Help_Menu = Menu(menubar, tearoff=0)
Help_Menu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=Help_Menu)

root.config(menu=menubar)

# ScrollBar
scrollbar = Scrollbar(text)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

root.mainloop()
