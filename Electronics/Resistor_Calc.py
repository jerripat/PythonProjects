from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from formulas import Formula as fm

my_win = tk.Tk()
my_win.title("Resistor Conversion")
my_win.geometry("400x400")


menubar = tk.Menu(my_win)
# tk.config(menu=menubar)

# Define a Menu
def my_fun():
    pass

def closeMe():
    #messagebox.showinfo("Close", "Are you sure you want to quit?")
    my_win.destroy()

def Change_Color(color):
    color = "green" if color == "red" else "red"
    menu_file.config(fg=color)
    my_win.after(1000, Change_Color, color)



# Create Menu Items
menu_file = Menu(menubar, tearoff=0, postcommand=lambda:Change_Color('red'))  # file menu
menu_edit = Menu(menubar, tearoff=0, bg='yellow',
                 font=('Hack',10),activebackground='green')  # edit menu

menubar.add_cascade(label="File", menu=menu_file)  # top line
menubar.add_cascade(label="Edit", menu=menu_edit)  # top line

menu_file.add_command(label="New", command=my_fun)
menu_file.add_command(label="Open", command=my_fun)
menu_file.add_command(label="Save as...", command=my_fun)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=closeMe)

menu_edit.add_command(label="Undo", command=my_fun)
menu_edit.add_command(label="Redo", command=my_fun)


def callMtToFt(mk):
    num = 0
    num = mk
    if num.isdigit():
        convert = fm.MtoI(int(num))
        convert = "%.2f" % convert
        display_label = Label(
            tk,
            text=f"The conversion from {num} Meter(s) {convert} Feet",
            bg="#06185c",
            fg="yellow",
        )
    else:
        messagebox.showerror("Error", "Please enter a valid number")

    messagebox.showinfo(
        "Conversion", f"The conversion from {num} Meter(s) to {convert} Feet"
    )

    display_label.pack(pady=10)
def radio():
    pass

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
    text=" Feet to Meter(s) ",
    variable=radioVar,
    value=0,
    bg="#06185c",
    fg="yellow",
).pack(pady=2)

rbutton2 = Radiobutton(
    tk,
    text=" Meter(s) to Feet ",
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
my_win.config(menu=menubar)
my_win.mainloop()