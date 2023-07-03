import tkinter as tk
from tkinter import messagebox

mainwindow = tk.Tk()
mainwindow.geometry("600x600")
mainwindow.resizable(True, True)
mainwindow.title("The Presidents")

def show_option1():
    messagebox.showinfo("Menu selection", "You selected Option 1")

def show_option2():
    messagebox.showinfo("Menu selection", "You selected Option 2")

def show_sub_option1():
    messagebox.showinfo("Menu selection", "You selected Sub-Option 1")

def show_sub_option2():
    messagebox.showinfo("Menu selection", "You selected Sub-Option 2")

root = tk.Tk()

# Create main menu bar
menubar = tk.Menu(root)

# Create the submenu 
file = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Option 1', menu = file)
file.add_command(label ='Sub-Option 1', command = show_sub_option1)
file.add_command(label ='Sub-Option 2', command = show_sub_option2)

# Adding another menu entry
menubar.add_command(label ='Option 2', command = show_option2)

root.config(menu = menubar)
root.mainloop()

