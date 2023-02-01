from ast import Expr
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

from formulas import Formula

mk = 0.0
tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("450x400")
tk.configure(background="#06185c")

#fm = Formula(mk)
img = ImageTk.PhotoImage(Image.open('/images/Kali2.jpg'))
img_label = Label(image=img)
img_label.pack()

tk.mainloop()