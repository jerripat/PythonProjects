from ast import Expr
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("400x400")
tk.configure(background="#06185c")

options = ['Temperature',
            'Distance',
            'Liquid',
            'Measurement']



def FtoC(unit):
    # F = (9/5 * C) + 32
    f = unit
    result = (f - 32) * (9 / 5)
    messagebox.showinfo(
        "Conversion",
        f"The converion from {f}{chr(176)} Farenhight to Centigrade is: {result:.2f}{chr(176)}",
    )
    # popup(result, f)
    return result


def CtoF(unit):
    # (xC * 5/9) + 32
    c = unit
    result = (c * 9 / 5) + 32
    messagebox.showinfo(
        "Converting...",
        f"The converion from {c}{chr(176)} Centigrade to Farenhight is: {result:.2f}{chr(176)}",
    )
    return result


def radio():
    if radioVar.get() == 0:
        callFtoC(e.get())
    else:
        callCtoF(e.get())


def callFtoC(unit):
    num = 0
    num = unit
    if num.isdigit():
        convert = FtoC(int(num))
        convert = f"{convert:.2f}"
        display_label = Label(
            tk,
            text=f"The converion from {num}{chr(176)} Farenhight to Centigrade is: {convert}{chr(176)}",
            bg="#06185c",
            fg="yellow",
        )
    else:
        display_label = Label(
            tk, text="Only numbers are allowed!", bg="#06185c", fg="yellow"
        )
    display_label.pack(pady=10)


def callCtoF(unit):
    num = 0
    num = unit
    if num.isdigit():
        convert = CtoF(int(num))
        convert = f"{convert:.2f}"
        display_label = Label(
            tk,
            text=f"The converion from {num}{chr(176)} Centigrade to Farenhight is: {convert}{chr(176)}",
            bg="#06185c",
            fg="yellow",
        )
    else:
        display_label = Label(
            tk, text="Only numbers are allowed!", bg="#06185c", fg="yellow"
        )

    display_label.pack(pady=10)


e1_label = Label(
    tk,
    text="Select conversion",
    bg="#06185c",
    fg="yellow",
    font=("Helvetica", 16),
).pack(pady=10)

my_combo = ttk.Combobox(tk, value=options, state="readonly")
my_combo.current(0)
my_combo.pack(pady=10)

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
