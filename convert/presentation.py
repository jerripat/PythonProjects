from ast import Expr
from tkinter import *
from formulas import Formula

tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("400x400")
tk.configure(background="#06185c")
tk.iconbitmap("ubuntu.ico")


fm = Formula()


def new_frame():
    hide_con_frame()
    open_con_frame()


def callMenu():
    num = e.get()
    if num.isdigit():

        convert = fm.FtoC(int(num))
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


def open_con_frame():
    con_frame.pack(pady=25)
    con_frame.focus_set()


def hide_con_frame():
    con_frame.pack_forget()


my_menu = Menu(tk)
tk.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_frame)
file_menu.add_command(label="Exit", command=tk.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Open Conversion Menu", command=open_con_frame)

con_label = Label(
    tk, text="Select 'New' from File", font=("Helvetica", 14), bg="#06185c", fg="yellow"
).pack(pady=10)
con_frame = Frame(tk, width="300", height="250", bd=2, bg="#06185c", relief="groove")
# con_frame.pack(pady=25)
con_frame_label = Label(
    con_frame, text="   Convert   ", font=("Helvetica", 14), bg="#06185c", fg="yellow"
)
con_frame_label.pack(pady=10)

v = IntVar()
rbutton1 = Radiobutton(
    tk,
    text=" Farenheigt to Centigrade ",
    variable=v,
    value=1,
    bg="#06185c",
    fg="yellow",
).pack(pady=2)
rbutton2 = Radiobutton(
    tk,
    text=" Centigrade to Farenheigt ",
    variable=v,
    value=2,
    bg="#06185c",
    fg="yellow",
).pack(pady=4)
e = Entry(con_frame, font=("Helvetica", 12))
e.pack(pady=10)
# e.focus_set()
my_button = Button(
    con_frame, text="Convert", font=("Helvetica", 12), fg="#120e8c", command=callMenu
)
my_button.pack(pady=15)


tk.mainloop()
