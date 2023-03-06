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
img_label.grid(column=5, row=0, columnspan=2, rowspan=2, padx=5, pady=5)

menubar = tk.Menu(mainwindow)

sub_menu = Menu(menubar, tearoff=0)
sub_menu.add_command(label="Exit", command=mainwindow.destroy)

con_menu = Menu(menubar, tearoff=0)
con_menu.add_command(label="SAE to Metric")
con_menu.add_command(label="Metric to SAE")
con_menu.add_command(label="Ft to Met")
con_menu.add_command(label="Met to Ft")

menubar.add_cascade(label="File", menu=sub_menu)
menubar.add_cascade(label="Conversions", menu=con_menu)

mainwindow.config(menu=menubar)

mainwindow.mainloop()
