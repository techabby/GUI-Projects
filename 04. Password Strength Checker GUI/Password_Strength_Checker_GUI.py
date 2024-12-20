from tkinter import *
from tkinter import font
import re

root = Tk()
root.geometry("500x400")
root.title("Password Strength Checker")
root.configure(bg="#EEEEFF")


# Fuctions
def strength():
    password = value.get()

    if len(password) < 8:
        return "Your Password is too short.\nIt must be at least 8 characters long."

    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).{8,}$"
    if not re.match(pattern, password):
        return "Password is not complex enough.\nIt must include a mix of digits, lowercase,\nuppercase, and special characters."

    if password.islower() or password.isupper():
        return "Password is not unique enough.\nIt should contain both uppercase and lowercase characters."

    return "Password is strong."


def check_strength():
    message = strength()
    display.config(text=message)


# Appearence

myfont = font.Font(family="Pacifico", size=13, weight="bold")

Label(
    root,
    text="PASSWORD STRENGTH CHECKER",
    bg="#022b3a",
    fg="#EEEEFF",
    font=myfont,
    pady=8,
    padx=3,
).pack(fill=X)
Label(
    root,
    text="Checks the strength of the password for better security",
    bg="#1f7a8c",
    fg="#EEEEFF",
    font=("Opensans", 11, "bold"),
    pady=8,
    padx=3,
).pack(fill=X)

frame = Frame(root, bg="#EEEEFF")
frame.pack(pady=30)

Label(
    frame,
    text="Enter your password: ",
    bg="#EEEEFF",
    fg="#022b3a",
    font=("Opensans", 12, "bold"),
    pady=8,
    padx=1,
).pack(side=LEFT, padx=5)
value = StringVar()
Entry(frame, textvariable=value).pack(side=LEFT, padx=5)

Button(
    frame,
    text="Enter",
    bg="#1f7a8c",
    fg="#EEEEFF",
    borderwidth=3,
    relief=SUNKEN,
    font=("Opensans", 7, "bold"),
    command=check_strength,
).pack(side=LEFT, padx=10)

display = Label(
    root,
    text="",
    bg="#EEEEFF",
    fg="#022b3a",
    font=("Times New Roman", 20, "bold"),
    pady=8,
    padx=4,
)
display.pack(pady=20)

root.mainloop()
