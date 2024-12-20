from tkinter import *
from tkinter import font
import random

root = Tk()
root.geometry("430x400")
root.title("Quotes Generator")
root.configure(bg="#FFFDD0")

Quotes = [
    "The only way to do great work\nis to love what you do.\n- Steve Jobs -",
    "Your time is limited, don't waste it\nliving someone else's life.\n- Oprah Winfrey -",
    "Success is not final, failure is not fatal:\nIt is the courage to continue that counts.\n- Winston Churchill -",
    "The only person you are destined to\nbecome is the person you decide to be.\n- Ralph Waldo Emerson -",
    "Don't watch the clock; do what it does.\nKeep going.\n- Sam Levenson -",
    "The future belongs to those who believe\nin the beauty of their dreams.\n- Eleanor Roosevelt -",
    "It's not about ideas.\nIt's about making ideas happen.\n- Scott Belsky -",
    "The only limit to our realization of\ntomorrow will be our doubts of today.\n- Franklin D. Roosevelt -",
    "Do not wait to strike till the iron is hot,\nbut make it hot by striking.\n- William Butler Yeats -",
    "I find that the harder I work,\nthe more luck I seem to have.\n- Thomas Jefferson -",
    "Success is stumbling from failure to\nfailure with no loss of enthusiasm.\n- Winston S. Churchill -",
    "The best way to predict the future is to\ncreate it.\n- Peter Drucker -",
    "Your life does not get better by chance,\nit gets better by change.\n- Jim Rohn -",
    "The way to get started is to quit\ntalking and begin doing.\n- Walt Disney -",
    "I attribute my success to this:\nI never gave or took any excuse.\n- Florence Nightingale -",
    "The only place where success comes\nbefore work is in the dictionary.\n- Vidal Sassoon -",
    "Success usually comes to those who are\ntoo busy to be looking for it.\n- Henry David Thoreau -",
    "The only thing standing between you and\nyour goalis the story you keep telling yourself\nas to why you can't achieve it.\n- Jordan Belfort -",
    "Don't be pushed around by the fears in your mind.\nBe led by the dreams in your heart.\n- Roy T. Bennett -",
    "Success is not in what you have,\nbut who you are.\n- Bo Bennett -",
    "The only limit to our realization of\ntomorrow will be our doubts of today.\n- Franklin D. Roosevelt -",
    "Your work is going to fill a large part of\nyour life, and the only way to be truly satisfied\nis to do what you believe is great work.\n- Steve Jobs -",
    "If you are not willing to risk the usual,\nyou will have to settle for the ordinary.\n- Jim Rohn -",
    "Believe you can and you're halfway there.\n- Theodore Roosevelt -",
    "The difference between a successful person and\nothers is not alack of strength,\nnot a lack of knowledge,\nbut rather a lack in will.\n- Vince Lombardi -",
    "Opportunities don't happen.\nYou create them.\n- Chris Grosser -",
    "Don't be afraid to give up the good\nto go for the great.\n- John D. Rockefeller -",
    "You miss 100% of the shots you don't take.\n- Wayne Gretzky -",
    "Success is not just about making money.\nIt's about making a difference.\n- Unknown -",
    "The greatest glory in living lies not in\nnever falling,\nbut in rising every time we fall.\n- Nelson Mandela -"
]

def generate_quotes():
    quote = random.choice(Quotes)
    Quote.config(text=quote)

thefont = font.Font(family="Quicksand", size=14, weight="bold")
thefont2 = font.Font(family="Gloria Hallelujah", size=11, weight="bold")

Label(root,text="Random Quotes Generator",bg="Black",fg="White",font=(thefont),pady=5).pack(fill=X)
Label(root,text="This GUI generates random quotes for you.",bg="#343434",fg="White",pady=5).pack(fill=X)

Button(root,text="Generate",bg="Black",fg="White",font=thefont,borderwidth=3,relief=RIDGE,command=generate_quotes).pack(pady=30)

Quote = Label(root,text=" ",fg="Black",bg="#FFFDD0",font=thefont2,borderwidth=3)
Quote.pack(pady=25)

root.mainloop()
