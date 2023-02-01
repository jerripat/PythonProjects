from ast import Expr
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from formulas import Formula

mk = 0.0
tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("450x400")
tk.configure(background="#06185c")

fm = Formula(mk)


def radio():
    if radioVar.get() == 0:
        callMtoK(e.get())
    else:
        callKtoM(e.get())


def callMtoK(mk):
    num = 0
    num = mk

    if num.isdigit():
        convert = fm.KmToMi(int(num))
        convert = '%.2f' % convert
        display_label = Label(
            tk,
            text=f"The converion from {num} mile(s) to {convert} Kilometers",
            bg="#06185c",
            fg="yellow",
        )
    else:
        messagebox.showerror("Error", "Please enter a valid number")

    messagebox.showinfo("Conversion",
        f"The converion from {num} mile(s) to {convert} Kilometers"
    )

    display_label.pack(pady=10)


def callKtoM(mk):
    num = 0
    num = mk
    if num.isdigit():
        convert = fm.KmToMi(int(num))
        convert = "%.2f" % convert
        display_label = Label(
            tk,
            text=f"The converion from {num} Kilometer(s) {convert} Mile(s)",
            bg="#06185c",
            fg="yellow",
        )
    else:
        messagebox.showerror("Error", "Please enter a valid number")

    messagebox.showinfo("Conversion",
            f"The converion from {num} Kilometer(s) to {convert} Mile(s)"
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
    text=" Mile(s) to Killometer(s) ",
    variable=radioVar,
    value=0,
    bg="#06185c",
    fg="yellow",
).pack(pady=2)

rbutton2 = Radiobutton(
    tk,
    text=" Kilometer(s) to Mile(s) ",
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
