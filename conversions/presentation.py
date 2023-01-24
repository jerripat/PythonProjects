from ast import Expr
from tkinter import *
from formulas import Formula

tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("400x400")
# tk.configure(bg="blue")


# fm = Formula()


# def callMenu():
#     num = e.get()
#     if num.isdigit():
#         convert = fm.FtoC(int(num))
#         convert = f"{convert:.2f}"
#         display_label = Label(
#             tk, bg="blue", fg="yellow", text=f"You entered : {convert}"
#         )
#     else:
#         display_label = Label(
#             tk, bg="blue", fg="yellow", text="Only numbers  allowed!!"
#         )
#     display_label.pack(pady=20)


# def editMenu():
#     pass


# def temp_conversion():
#     pass


# my_label = Label(
#     tk,
#     text="Select Conversion from 'Menu'",
#     font=("Comic Sans", 12, "bold"),
#     fg="black",
#     bg="blue",
# ).pack(pady=10)
# e = Entry(tk, font=("Helvetica", 12), bg="blue")
# e.pack(pady=10)
# e.focus_set()
# my_button = Button(
#     tk, text="Convert", font=("Helvetica", 12), fg="#120e8c", command=callMenu
# )
# my_button.pack(pady=15)
# my_menu = Menu(tk)
# # tk.config(menu=my_menu)
# file_menu = Menu(my_menu)
# my_menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New", command=callMenu)
# file_menu.add_command(label="Exit", command=tk.quit)

# edit_menu = Menu(my_menu)
# my_menu.add_cascade(label="Menu", menu=edit_menu)
# edit_menu.add_command(label="Convert Temps", command=temp_conversion)

# file_frame = Frame(tk, width=200, height=200, bd=5, bg="blue", relief="groove")
# file_frame.pack()
