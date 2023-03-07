import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


class Window:
    def __init__(self, master):
        mainframe = tk.Frame(master, width=200, height=200, bg="#099142")
        mainframe.pack(pady=20)

        mainmenu = tk.Menu(mainframe)
        master.config(menu=mainmenu)

        filemenu = tk.Menu(mainframe, tearoff=0)
        filemenu.add_command(label="New File", command=self.func)
        filemenu.add_command(label="Save", command=self.func)
        filemenu.add_command(label="Load", command=self.func)
        filemenu.add_command(label = "Exit", command=self.closeMe)

        exportmenu = tk.Menu(mainframe, tearoff=0)
        exportmenu.add_command(label="Export as PDF", command=self.func)
        exportmenu.add_command(label="Export as PNG", command=self.func)
        exportmenu.add_command(label="Export as SVG", command=self.func)

        mainmenu.add_cascade(label="File", menu=filemenu)
        filemenu.add_cascade(label="Export", menu=exportmenu)

    def func(self):
        print("This is a empty function")

    def closeMe(self):
        messagebox.showinfo("Close", "Are you sure you want to quit?")
        mainwindow.destroy()


mainwindow = tk.Tk()
mainwindow.title("Conversion Calculator")
mainwindow.geometry("500x450")
mainwindow.configure(background="#084722")

img = ImageTk.PhotoImage(Image.open("images/ubuntu-icon.png"))
img_label = Label(mainwindow, image=img)
img_label.pack(pady=20) #column=5, row=0, columnspan=2, rowspan=2, padx=5, pady=5)

window = Window(mainwindow)

mainwindow.mainloop()
