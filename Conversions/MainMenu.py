from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

my_win = tk.Tk()
my_win.title("Menus")
my_win.geometry("400x400")


# Define a Menu
def my_fun():
    pass

menubar = tk.Menu(my_win)
# tk.config(menu=menubar)

def closeMe():
    messagebox.showinfo("Close", "Are you sure you want to quit?")
    my_win.destroy()


# Create Menu Items
menu_file = Menu(menubar, tearoff=0)  # file menu
menu_edit = Menu(menubar, tearoff=0, bg='yellow',font=('Hack',12))  # edit menu

menubar.add_cascade(label="File", menu=menu_file)  # top line
menubar.add_cascade(label="Edit", menu=menu_edit)  # top line

menu_file.add_command(label="New", command=my_fun)
menu_file.add_command(label="Open", command=my_fun)
menu_file.add_command(label="Save as...", command=my_fun)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=closeMe)

menu_edit.add_command(label="Undo", command=my_fun)
menu_edit.add_command(label="Redo", command=my_fun)

my_win.config(menu=menubar)
my_win.mainloop()
