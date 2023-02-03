#!/usr/bin/python

from ast import Expr
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

from formulas import Formula

mk = 0.0
tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("450x450")
tk.configure(background="#06185c")

# fm = Formula(mk)
frame = Frame(tk, width=200, height=150)
frame.pack()
frame.place(anchor="center", relx=0.5, rely=0.5)

menu_frame = Frame(tk,width=100,height=100,bg='#735303')
menu_frame.pack(pady=100,padx=10)

img = ImageTk.PhotoImage(Image.open("images/Kali2.jpg"))
img_label = Label(frame, image=img)
img_label.pack()

fr_label = Label(menu_frame,text=' Conversion Menu ').pack(pady=10)

tk.mainloop()
