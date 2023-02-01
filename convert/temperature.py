from ast import Expr
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from formulas import Formula

temp = 0.0
tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("450x400")
tk.configure(background="#06185c")

fm = Formula(temp)


def radio():
    if radioVar.get() == 0:
        callFtoC(e.get())
    else:
        callCtoF(e.get())


def callFtoC(temp):
    num = 0
    num = temp

    if num.isdigit():
        convert = fm.FtoC(int(num))
        convert = " %.2f" % convert
        display_label = Label(
            tk,
            text=f"The converion from {num}{chr(176)} Farenhight is : {convert}{chr(176)} Centigrade",
            bg="#06185c",
            fg="yellow",
        )
    else:
        messagebox.showerror("Error", "Please enter a valid number")
    messagebox.showinfo(
        "Conversion",
        f"The converion from {num}{chr(176)} Farenhight is: {convert}{chr(176)} Centigrade",
    )

    display_label.pack(pady=10)


def callCtoF(temp):
    num = 0
    num = temp
    if num.isdigit():
        convert = fm.CtoF(int(num))
        convert = "%.2f" % convert
        display_label = Label(
            tk,
            text=f"The converion from {num}{chr(176)} Centigrade is {convert}{chr(176)} Farenhight",
            bg="#06185c",
            fg="yellow",
        )
    else:
        messagebox.showerror("Error", "Please enter a valid number")ca
        
    messagebox.showinfo(
        "Conversion",
        f"The converion from {temp}{chr(176)} Centigrade is {convert}{chr(176)} Farenhight",
    )

    display_label.pack(pady=10)


e1_label = Label(
    tk,
    text="Select conversion",
    bg="#06185c",
    fg="yellow",
    font=("Helvetica", 16),
).pack(pady=10)


radioVar = IntVar()

rbutton1 = Radiobutton(
    tk,
    selectcolor="#06185c",
    text=" Farenheigt to Centigrade ",
    variable=radioVar,
    value=0,
    bg="#06185c",
    fg="yellow",
).pack(pady=2)

rbutton2 = Radiobutton(
    tk,
    text=" Centigrade to Farenheigt ",
    variable=radioVar,
    value=1,
    bg="#06185c",
    fg="yellow",
    selectcolor="#06185c",
).pack(pady=4)

e = Entry(tk, text="Select Converion Type", font=("Helvetica", 14))
e.pack(pady=10)
e.focus_set()

temp = e.get()

radButton = Button(tk, text="Convert", command=radio).pack(pady=10)

my_menu = Menu(tk)
tk.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Exit", command=tk.quit)

edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=edit_menu)
edit_menu.add_command(label="Temperature")
edit_menu.add_command(label="Distance")
edit_menu.add_command(label="Measurement")
edit_menu.add_command(label="Liquid")


tk.mainloop()
