#Female Artificial Intelligience
import tkinter as tk
from tkinter import *

HAI = Tk()
HAI.title("Female AI")

#Background
bg = Image.open("AI_images/Background.jpg")
bg = bg.resize((1000, 10000))
bg = ImageTk.PhotoImage(bg)
bgr = Label(HAI, image=bg, width=1000, height=10000)
bgr.pack(side=TOP, expand="yes")

human = Image.open("AI_images/HAI.jpg")
human = human.resize((600, 600))
human = ImageTk.PhotoImage(human)
man = Label(HAI, image=human, width=600, height=600)
man.place(x=60, y=300)

HAI.mainloop()