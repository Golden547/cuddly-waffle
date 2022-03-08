# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:06:02 2022

@author: shn99
"""

from tkinter import*
from PIL import ImageTk, Image
root=Tk()

root.title("Endless Pokemon Game")
root.geometry("600x400")

root.configure(background="yellow2")

img=ImageTk.PhotoImage(Image.open ("dice1.4.jpg"))

player1 = Label(root, text = "Player 1", bg="royal blue", fg="White")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg="royal blue",fg="White")
player2.place(relx = 0.9, rely= 0.3, anchor=CENTER)

player_1_score = Label(root, bg="royal blue", fg = "White")
player_1_score.place(relx=0.1, rely=0.4, anchor=CENTER)

player_2_score = Label(root, bg="royal blue", fg = "white")
player_2_score.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()