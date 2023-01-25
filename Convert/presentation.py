from ast import Expr
from tkinter import *
from formulas import Formula

tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("400x400")


fm = Formula()


def callMenu():
    # num = e.get()
    convert = fm.FtoC()
    convert = f"{convert:.2f}"
    display_label = Label(tk, text=f"You entered : {convert}")
    display_label.pack(pady=20)


def editMenu():
    pass


def open_conversion():
    pass


my_label = Label(
    tk, text="Enter Number to convert", font=("Helvetica", 16), fg="#471bcc"
).pack(pady=10)
e = Entry(tk, font=("Helvetica", 12))
e.pack(pady=10)
e.focus_set()
my_button = Button(
    tk, text="Convert", font=("Helvetica", 12), fg="#120e8c", command=callMenu
)
my_button.pack(pady=15)
menu_label = Label(tk).pack(pady=10)

my_menu = Menu(tk)
tk.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=callMenu)
file_menu.add_command(label="Exit", command=tk.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Open Conversion Menu", command=open_conversion)


tk.mainloop()
