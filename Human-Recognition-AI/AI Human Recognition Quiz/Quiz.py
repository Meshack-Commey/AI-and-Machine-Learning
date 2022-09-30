#Artificial Intelligience Human Quiz
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

QUIZ = Tk()
QUIZ.title("Male AI")

#Background
bg = Image.open("images/Background.jpg")
bg = bg.resize((1000, 10000))
bg = ImageTk.PhotoImage(bg)
bgr = Label(QUIZ, image=bg, width=1000, height=10000)
bgr.pack(side=TOP, expand="yes")

#Quiz1 image
human = Image.open("images/Quiz1.jpg")
human = human.resize((720, 1450))
human = ImageTk.PhotoImage(human)
man = Label(QUIZ, image=human, width=720, height=1450)
man.place(x=0, y=1)

hair = Text(QUIZ, width=8, height=2,cursor ="arrow")
hair.place(x=46, y=168)
hair.insert(INSERT, "hair")

def Bell():
 bell = Label(QUIZ, text="Correct!", bg="white",fg="blue")
 bell.place(x=46, y=250)
 
if hair == "hair":
 print("Correct!")
else:
 print("Wrong")


QUIZ.mainloop()