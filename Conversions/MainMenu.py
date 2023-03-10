from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import sys

root = Tk()
root.title("Menus")
root.geometry("400x400")
root.resizable(False, False)

# Define a Menu
rootMenu = Menu(root)
root.config(menu=rootMenu,bg="#084722")

def openFile():
    pass

def saveFile():
    pass

def closeMe():
        messagebox.showinfo("Close", "Are you sure you want to quit?")
        root.destroy()

# Create Menu Items
fileMenu = Menu(rootMenu, tearoff=0)
rootMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=closeMe)

conMenu = Menu(rootMenu, tearoff=0)
rootMenu.add_cascade(label="Conversion", menu=conMenu)
conMenu.add_command(label="Temperature", command=fileMenu)
conMenu.add_command(label="Distance", command=openFile)
conMenu.add_command(label="Met to SAE", command=saveFile)



root.mainloop()
