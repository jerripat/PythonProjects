from ast import Expr
from tkinter import *
#from formulas import Formula

tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("400x400")
tk.configure(background="#06185c")


#fm = Formula()

def FtoC(unit):
        # F = (9/5 * C) + 32
        f = unit
        return (f - 32) * 5 / 9

def CtoF(unit):
        # (xC * 5/9) + 32
        c = unit
        return (c * 5 / 9) + 32

def callFtoC(unit):
    num = unit
    if num.isdigit():

        convert = FtoC(int(num))
        convert = f"{convert:.2f}"
        display_label = Label(
            tk, text=f"You entered : {convert}", bg="#06185c", fg="yellow"
        )
    else:
        display_label = Label(
            tk, text="Only numbers are allowed!", bg="#06185c", fg="yellow"
        )


def callCtoF(unit):
    num = unit
    if num.isdigit():
        convert = CtoF(int(num))
        convert = f"{convert:.2f}"
        display_label = Label(
            tk, text=f"You entered : {convert}", bg="#06185c", fg="yellow"
        )
    else:
        display_label = Label(
            tk, text="Only numbers are allowed!", bg="#06185c", fg="yellow"
        )

    display_label.pack(pady=10)


def editMenu():
    pass

def radio():
    if radioVar.get() == 0:
        callFtoC(e.get())
    else:
        callCtoF(e.get())

e_label = Label(
    tk,
    text="Enter Temperature to Convert",
    bg="#06185c",
    fg="yellow",
    font=("Helvetica", 16),
).pack(pady=10)

e = Entry(tk, font=("Helvetica", 14))
e.pack(pady=10)
e.focus_set()

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

print(f'radioVar = : {radioVar.get()}')
rbutton2 = Radiobutton(
    tk,
    text=" Centigrade to Farenheigt ",
    variable=radioVar,
    value=1,
    bg="#06185c",
    fg="yellow",
    selectcolor="#06185c",
).pack(pady=4)

radButton = Button(tk, text="Choose Temp Type", command=radio).pack(pady=10)

my_menu = Menu(tk)
tk.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Exit", command=tk.quit)

edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options")
edit_menu.add_command(label="Temperature")
menu_sub = Menu(edit_menu, tearoff=0, bg="green")


tk.mainloop()
