from tkinter import *
from tkinter import messagebox

# from PIL import Image, ImageTk
from formulas import Formula as fm
from Elec_formulas import ohms_law as om

tk = Tk()
tk.title("Resistor Conversion")
tk.geometry("500x500")
tk.configure(background="#1E194A")

backcolo = "#1E194A"
fgcolo = "yellow"


def radio():
    match res.get():
        case 1:
            r = Label(tk, text="Resistor", bg=backcolo, font=("Arial", 12)).grid()
            messagebox.showinfo(
                title="Resistor Conversion", message="Please enter the resistor value"
            )
        case 2:
            a = Label(tk, text="Ampere/Current", bg=backcolo, font=("Arial", 12)).grid()
        case 3:
            o = Label(tk, text="Ohm", bg=backcolo, font=("Arial", 12)).grid()
        case 4:
            c = Label(tk, text="Current", bg=backcolo, font=("Arial", 12)).grid()


res = IntVar()
ty = StringVar()

fr_1 = Frame(tk, width=400, height=400, bd=1, bg="#766bb3", relief="sunken")
fr_1.grid(columnspan=4, row=4)

rbutton_1 = Radiobutton(
    fr_1, text="  Resistor", width=10, bg=backcolo, fg="#a8b36b", variable=res, value=1
).pack()
rbutton_2 = Radiobutton(
    fr_1, text="  Ampere", width=10, bg=backcolo, fg="#a8b36b", variable=res, value=2
).pack()
rbutton_3 = Radiobutton(
    fr_1, text="  Ohm     ", width=10, bg=backcolo, fg="#a8b36b", variable=res, value=3
).pack()
rbutton_4 = Radiobutton(
    fr_1, text="  Current ", width=10, bg=backcolo, fg="#a8b36b", variable=res, value=4
).pack()

# ------------------------------------
v_label = Label(tk, text="Volt", bg=backcolo, fg=fgcolo, font=("Helvetica", 14)).grid(
    column=0, row=6
)

volt = Entry(tk, width=10, text="Insert Value", font=("Helvetica", 14)).grid(
    column=0, row=7
)
# ------------------------------------

i_label = Label(
    tk, text="Current", bg=backcolo, fg=fgcolo, font=("Helvetica", 14)
).grid(column=1, row=6)

current = Entry(tk, width=10, text="Insert Value", font=("Helvetica", 14)).grid(
    column=1, row=7
)
# ------------------------------------


r_label = Label(
    tk, text="Resistor", bg=backcolo, fg=fgcolo, font=("Helvetica", 14)
).grid(column=2, row=6)

res = Entry(tk, width=10, text="Insert Value", font=("Helvetica", 14)).grid(
    column=2, row=7
)
# ------------------------------------

filler_label = Label(
    tk, text=" ", bg=backcolo, fg="yellow", font=("Helvetica", 20)
).grid(columnspan=4, row=8)


b1 = Button(tk, text="Convert", command=radio).grid(column=1, row=9)

Label(tk, text=" Waiting...      ", bg=backcolo, fg="yellow", font=("Helvetica", )).grid(columnspan=4,row=20)
tk.mainloop()
