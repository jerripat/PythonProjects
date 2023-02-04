from ast import Expr
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

from formulas import Formula

mk = 0.0
tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("450x400")
tk.configure(background="#06185c")

fm = Formula(mk)
# frame = Frame(tk, width=20, height=20)
# frame.pack()
# frame.place(anchor="nw", relx=0.5, rely=0.5)
screen_frame = Frame(tk, width=200, height=200, bg="#735303")
screen_frame.grid(column=0, row=0)

img = ImageTk.PhotoImage(Image.open("images/scale.png"))
img_label = Label(screen_frame, image=img)
img_label.grid(column=0, row=2)


def radio():
    if radioVar.get() == 0:
        callInchToMil(e.get())
    else:
        callMilToInch(e.get())


def callInchToMil(mk):
    num = 0
    num = mk

    if num.isdigit():
        convert = fm.InchToMil(int(num))
        convert = "%.2f" % convert
        display_label = Label(
            tk,
            text=f"The conversion from {num} inch(s) to {convert} millimeters",
            bg="#06185c",
            fg="yellow",
        )
    else:
        messagebox.showerror("Error", "Please enter a valid number")

    messagebox.showinfo(
        "Conversion", f"The conversion from {num} inch(s) to {convert} milimeters"
    )

    display_label.grid(column=2, row=1)


def callMilToInch(mk):
    num = 0
    num = mk
    if num.isdigit():
        convert = fm.MtoI(int(num))
        convert = "%.2f" % convert
        display_label = Label(
            tk,
            text=f"The conversion from {num} milimeter(s) {convert} inch(s)",
            bg="#06185c",
            fg="yellow",
        )
    else:
        messagebox.showerror("Error", "Please enter a valid number")

    messagebox.showinfo(
        "Conversion", f"The conversion from {num} milimeter(s) to {convert} inch(s)"
    )

    display_label.grid(column=2, row=1)


e1_label = Label(
    tk,
    text="Select Conversion",
    bg="#06185c",
    fg="yellow",
    font=("Helvetica", 16),
).grid(column=1, row=2)


radioVar = IntVar()

rbutton1 = Radiobutton(
    tk,
    selectcolor="#06185c",
    text="  Inch(s) to Milimeter(s)  ",
    variable=radioVar,
    value=0,
    bg="#06185c",
    fg="yellow",
).grid(column=1, row=3)

rbutton2 = Radiobutton(
    tk,
    text="  Milimeter(s) to Inch(s)  ",
    variable=radioVar,
    value=1,
    bg="#06185c",
    fg="yellow",
    selectcolor="#06185c",
).grid(column=1, row=4)

e = Entry(tk, text="Select Converion", font=("Helvetica", 12))
e.grid(column=1, row=5)
e.focus_set()

temp = e.get()

radButton = Button(tk, text="Convert", command=radio).grid(column=1, row=8)

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
