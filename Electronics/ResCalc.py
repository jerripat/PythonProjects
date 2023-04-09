from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from formulas import Formula as fm

tk = Tk()
tk.title("Resistor Conversion")
tk.geometry("400x400")
tk.configure(background="#239943")


def convert(ty, val):
    # sourcery skip: merge-comparisons, merge-duplicate-blocks, remove-redundant-if
    i = 10
    v = 20
    global r, a, o, c
    match ty:
        case "v":
            v1 = int(val)
            val = v1 / i
            l1 = Label(tk, text=f"Resistor: {val} ", font=("Arial", 12)).pack(pady=5)
        case "i":
            i1 = int(val)
            l1 = Label(tk, text=ty, font=("Arial", 12)).pack()
        case "r":
            r1 = int(val) / i
            l1 = Label(tk, text=r1, font=("Arial", 12)).pack(pady=10)

    return val


def radio():
    match res.get():
        case 1:
            r = Label(tk, text="Resistor", font=("Arial", 12)).pack()
        case 2:
            a = Label(tk, text="Ampere", font=("Arial", 12)).pack()
        case 3:
            o = Label(tk, text="Ohm", font=("Arial", 12)).pack()
        case 4:
            c = Label(tk, text="Current", font=("Arial", 12)).pack()


def hide():
    r.pack_forget()


def show():
    r.pack(pady=10)


res = IntVar()
ty = StringVar()

Label(tk, text="Select Calculation").pack()

fr_1 = Frame(tk, width=200, height=200, bd=1, bg="teal", relief="sunken")
fr_1.pack(padx=20, pady=10)

rbutton_1 = Radiobutton(tk, text="Resistor", variable=res, value=1)
rbutton_1.pack(padx=10)
rbutton_2 = Radiobutton(tk, text="Ampere", variable=res, value=2)
rbutton_2.pack()
rbutton_3 = Radiobutton(tk, text="Ohm     ", variable=res, value=3)
rbutton_3.pack()
rbutton_4 = Radiobutton(tk, text="Current", variable=res, value=4)
rbutton_4.pack()


val = Entry(tk, width=10, text="Insert Value", font=("Helvetica", 14))
val.pack()

b1 = Button(tk, text="Convert", command=radio).pack(pady=10)


stat = Label(
    tk,
    text="Waiting...",
    relief="sunken",
    width=50,
    bg="#766bb3",
    fg="#a8b36b",
    font=("Arial", 12),
).pack(pady=50)

tk.mainloop()
