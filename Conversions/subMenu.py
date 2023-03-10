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
        filemenu.add_command(label="Exit", command=self.closeMe)

        conmenu = tk.Menu(mainframe, tearoff=0)
        conmenu.add_command(label="Metric", command=self.closeMe)

        sub_con_menu = tk.Menu(conmenu, tearoff=0,bg='#054229')
        #sub_con_menu.add_cascade(label="Metric to Imperial", sub_con_menu=conmenu)

        sub_con_menu.add_command(label="Metric to Imperial", command=self.func)
        sub_con_menu.add_command(label="Export as PNG", command=self.func)
        sub_con_menu.add_command(label="Export as SVG", command=self.func)

        conmenu.add_command(label="Imperial", command=self.func)
        conmenu.add_command(label="Something else", command=self.func)

        mainmenu.add_cascade(label="File", menu=filemenu)
        mainmenu.add_cascade(label="Conversions", menu=conmenu)

    def func(self):
        print("This is a empty function")

    def closeMe(self):
        # messagebox.showinfo("Close", "Are you sure you want to quit?")
        mainwindow.destroy()


mainwindow = tk.Tk()
mainwindow.title("Conversion Calculator")
mainwindow.geometry("500x450")
mainwindow.configure(background="#084722")

img = ImageTk.PhotoImage(Image.open("images/ubuntu-icon.png"))
img_label = Label(mainwindow, image=img)
img_label.pack(pady=20)  # column=5, row=0, columnspan=2, rowspan=2, padx=5, pady=5)

window = Window(mainwindow)

mainwindow.mainloop()
