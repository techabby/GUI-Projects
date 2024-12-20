from tkinter import *
import random
import string
import tkinter.messagebox as tmsg
from tkinter import font

root = Tk()
root.geometry("550x400")
root.title("Password Generator")
root.config(bg="#1FF4E1")


def pass_gen(length, complexity):
    if complexity == "weak":
        chars = string.ascii_lowercase
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits
    elif complexity == "strong":
        chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(chars) for i in range(length))
    return password


def main():
    try:
        complexity = val2.get()
        length = val1.get()
        if complexity and length:
            if length <= 4:
                raise ValueError("Password length must be greater than 4")
            password = pass_gen(length, complexity)
            return password
        else:
            raise ValueError("Please enter all fields correctly")
    except Exception as e:
        tmsg.showinfo(title="Error", message=e, icon="error")
        return None


def generated():
    password = main()
    if password:
        tmsg.showinfo(
            "Password Generated Successfully!",
            f"Your generated password is:\n\n\t{password}",
        )


myfont = font.Font(family="Bebas_Neue", size=15, weight="bold")
myfont2 = font.Font(family="Oldenburg", size=15, weight="bold")
myfont3 = font.Font(family="Quicksand", size=10, weight="bold")
myfont4 = font.Font(family="digital-7", size=18)

Label(
    root,
    text="PASSWORD GENERATOR",
    bg="Black",
    fg="#1FF4E1",
    font=myfont,
    padx=10,
    pady=5,
).pack(fill=X)
Label(
    root,
    text="Generate Secure and Unique Passwords with Ease",
    padx=5,
    pady=10,
    bg="#201D1D",
    fg="#1FF4E1",
    font=("Times New Roman", 13, "bold"),
).pack(fill=X)

val1 = IntVar()
val1.set("")
Label(root, text="Enter the length of password:", font=myfont2, bg="#1FF4E1").pack(
    fill=X, padx=5, pady=10
)
Entry(root, textvariable=val1, font=myfont4).pack(pady=10)

Label(
    root,
    text="Choose the complexity of the password",
    font=myfont2,
    bg="#1FF4E1",
    pady=20,
).pack(fill=X, padx=5)

frame = Frame(root, bg="#1FF4E1")
frame.pack(padx=5)

val2 = StringVar()
Radiobutton(
    frame,
    text="Weak",
    variable=val2,
    value="weak",
    bg="#1FF4E1",
    borderwidth=0,
    highlightthickness=0,
    font=myfont3,
).pack(side=LEFT, padx=40)
Radiobutton(
    frame,
    text="Medium",
    variable=val2,
    value="medium",
    bg="#1FF4E1",
    borderwidth=0,
    highlightthickness=0,
    font=myfont3,
).pack(side=LEFT, padx=80)
Radiobutton(
    frame,
    text="Strong",
    variable=val2,
    value="strong",
    bg="#1FF4E1",
    borderwidth=0,
    highlightthickness=0,
    font=myfont3,
).pack(side=LEFT, padx=40)

Button(
    root, text="Generate", command=generated, bg="Black", fg="#1FF4E1", font=myfont2
).pack(padx=5, pady=30)

root.mainloop()
