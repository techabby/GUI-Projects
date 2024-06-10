from tkinter import *
from tkinter import font

root = Tk()
root.geometry("600x800")
root.title("Calculator")
root.config(bg="#292c30")


# Function to handle button click
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "0      ":
        text = "0"

    if text == " 1":
        text = "1"

    if text == "C":
        scvalue.set("")
        output.update()
    elif text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                value = "SCIENTIFIC ERROR"

        scvalue.set(value)
        output.update()
    else:
        scvalue.set(scvalue.get() + text)
        output.update()


# Fonts
myfont = font.Font(family="Digital-7", size=40, weight="bold")

# Entry
scvalue = StringVar()
scvalue.set("")
output = Entry(
    root,
    textvariable=scvalue,
    bg="#292c30",
    fg="#b7bfc8",
    font=myfont,
    highlightthickness=0,
    borderwidth=0,
)
output.pack(fill=X, ipady=40, pady=10, padx=30)

# Frames
frame1 = Frame(root, bg="#292c30")
frame1.pack()
b = Button(
    frame1,
    text="C",
    font=myfont,
    padx=30,
    pady=15,
    bg="Red",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame1,
    text="()",
    font=myfont,
    padx=20,
    pady=15,
    bg="#30ad6b",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame1,
    text="%",
    font=myfont,
    padx=30,
    pady=15,
    bg="#30ad6b",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame1,
    text="/",
    font=myfont,
    padx=30,
    pady=15,
    bg="#30ad6b",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

frame2 = Frame(root, bg="#292c30")
frame2.pack()
b = Button(
    frame2,
    text="7",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame2,
    text="8",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame2,
    text="9",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame2,
    text="*",
    font=myfont,
    padx=30,
    pady=15,
    bg="#30ad6b",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

frame3 = Frame(root, bg="#292c30")
frame3.pack()
b = Button(
    frame3,
    text="4",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame3,
    text="5",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame3,
    text="6",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame3,
    text="-",
    font=myfont,
    padx=30,
    pady=15,
    bg="#30ad6b",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

frame4 = Frame(root, bg="#292c30")
frame4.pack()
b = Button(
    frame4,
    text="1",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame4,
    text="2",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame4,
    text="3",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame4,
    text="+",
    font=myfont,
    padx=30,
    pady=15,
    bg="#30ad6b",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

frame5 = Frame(root, bg="#292c30")
frame5.pack()
b = Button(
    frame5,
    text="0      ",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame5,
    text=".",
    font=myfont,
    padx=30,
    pady=15,
    bg="#323538",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

b = Button(
    frame5,
    text="=",
    font=myfont,
    padx=30,
    pady=15,
    bg="#30ad6b",
    fg="#b7bfc8",
    highlightthickness=0,
    borderwidth=0,
)
b.pack(side=LEFT, pady=20, padx=30)
b.bind("<Button-1>", click)

root.mainloop()
