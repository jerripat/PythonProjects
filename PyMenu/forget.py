#from argparse import FileType
#import pyautogui
from tkinter import *
import tkinter as tk

#pyautogui.alert('Just a test', "Title")

root = tk.Tk()
root.title('Forget')
root.geometry("400x400")


def submit():
    hello_label = Label(root, text="Hello " + e.get())
    hello_label.grid(row=3, column=0)


def clear():
    hello_label.grid_forget()


# Forget
my_label = Label(root, text="Enter your name:").grid(row=0, column=0)

e = Entry(root)
e.grid(row=1, column=0)

my_button = Button(root, text="Submit", command=submit).grid(row=2, column=0)

clear_button = Button(root, text="Clear", command=clear)
