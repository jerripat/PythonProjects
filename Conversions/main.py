#!/usr/bin/python

from ast import Expr
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

from formulas import Formula


def hello():
    messagebox.showinfo("Conversions", "Hello World")


mk = 0.0
mainwindow = tk.Tk()
mainwindow.title("Conversion Calculator")
mainwindow.geometry("500x450")
mainwindow.configure(background="#084722")

img = ImageTk.PhotoImage(Image.open("images/ubuntu-icon.png"))
img_label = Label(mainwindow, image=img)
img_label.grid(columnspan=3, row=2)

menubar = tk.Menu(mainwindow)
sub_menu = Menu(menubar, tearoff=0)
sub_menu.add_command()

# sub_sub_menu = Menu(sub_menu, tearoff=0)
# sub_sub_menu.add_command(label="SAE to Metric")
# sub_sub_menu.add_command(label="Metric to SAE")

# #menubar.add_cascade(label="Conversions", menu=sub_menu)
# sub_menu.add_command(label="Exit", command=mainwindow.destroy)

menubar.add_cascade(label="File", menu=sub_menu)
menubar.add_cascade(label="Conversions")
#sub_menu.add_cascade(label="Metrics",sub_menu=sub_sub_menu)

mainwindow.config(menu=menubar)

mainwindow.mainloop()
