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
        callItoM(e.get())
    else:
        callMtoI(e.get())


def callItoM(mk):
    num = 0
    num = mk

    if num.isdigit():
        convert = fm.ItoM(int(num))
        convert = "convert = %.2f" % convert
        display_label = Label(
            tk,
            text=f"The conversion from {num} inch(s) to {convert} millimeters",
            bg="#06185c",
            fg="yellow",
        )

    messagebox.showinfo("Conversion",
        f"The conversion from {num} inch(s) to {convert} milimeters"
    )

    display_label.pack(pady=10)


def callMtoI(mk):
    num = 0
    num = mk
    if num.isdigit():
        convert = fm.MtoI(int(num))
        convert = "convert = %.2f" % convert
        display_label = Label(
            tk,
            text=f"The conversion from {num} milimeter(s) {convert} inch(s)",
            bg="#06185c",
            fg="yellow",
        )
    else:
        display_label = Label(
            tk, text="Only numbers are allowed!", bg="#06185c", fg="yellow"
        )
    messagebox.showinfo("Conversion",
            f"The conversion from {num} milimeter(s) to {convert} inch(s)"
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
    text=" Inch(s) to Milimeter(s) ",
    variable=radioVar,
    value=0,
    bg="#06185c",
    fg="yellow",
).pack(pady=2)

rbutton2 = Radiobutton(
    tk,
    text=" milimeter(s) to inch(s) ",
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
