
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Radio/Popup/checkbox/combobox Buttons")
root.geometry("450x550")


def radio():
    if v.get() == 1:
        my_label = Label(root, text="You clicked button one").pack(pady=10)
    elif v.get() == 2:
        my_label = Label(root, text="You clicked button Two",
                         fg="red").pack(pady=10)
    elif v.get() == 3:
        my_label = Label(root, text="You clicked button Three").pack(pady=10)
    else:
        my_label = Label(root, text="You clicked button Four",
                         fg="green").pack(pady=10)


def menu_choice():
    if v.get() == "rsync all files":
        my_label = Label(root, text="You slected all files?")
    else:
        my_label = Label(root, "Make another selection")
    my_label = Label(root, text=v.get())
    my_label.pack(pady=10)


def popup():
    # messagebox.showinfo, showwarning, showerror, askquestion, askokcancelaskyesno
    response = messagebox.askyesno(
        "Pop up Titile", "This is a messagebox popup")
    my_label = Label(root, text=response).pack(pady=10)


def select():
    if my_combo.get() == "Monday":
        my_label = Label(root, text="You clicked: " +
                         my_combo.get()).pack(pady=10)
    elif my_combo.get() == "Tuesday":
        my_label = Label(root, text="You clicked: " +
                         my_combo.get()).pack(pady=10)
    elif my_combo.get() == "Wednesday":
        my_label = Label(root, text="You clicked: " +
                         my_combo.get()).pack(pady=10)


# Radio Buttons
v = IntVar()
v.set(1)
#x = StringVar()
rbutton_1 = Radiobutton(root, text="One", variable=v, value=1).pack()
rbutton_2 = Radiobutton(root, text="Two", variable=v, value=2).pack()
rbutton_3 = Radiobutton(root, text="Three", variable=v, value=3).pack()
rbutton_4 = Radiobutton(root, text="Four", variable=v, value=4).pack()

my_button = Button(root, text="Click me!", command=radio)
my_button.pack(pady=10)

# Check boxs

v = StringVar()
my_check = Checkbutton(root, text="rsync all files", variable=v,
                       onvalue="rsync all files", offvalue="none")
my_check.deselect()
my_check.pack()

my_button = Button(root, text="Select backup",
                   command=menu_choice).pack(pady=20)

# Pop-up boxs

pop_button = Button(root, text="Click to Pop Up!",
                    command=popup).pack(pady=10)

# Comboboxs
options = [

    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]
my_combo = ttk.Combobox(root, value=options)
my_combo.current(0)
my_combo.pack(pady=10)

my_button = Button(root, text="Select", command=select).pack(pady=10)

root.mainloop()
