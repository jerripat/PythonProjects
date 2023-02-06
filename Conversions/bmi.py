from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image



from formulas import BMICalc

tk = Tk()
tk.title("BMI Calculator")
tk.geometry("400x400")
tk.configure(background="#06185c")

bm = BMICalc()

wt = StringVar()
ht = IntVar()
ht2 = IntVar()

wt.set("")
ht.set("")
ht2.set("")

def callBMI():
    wt = e1.get()
    ht = e2.get()
    ht2 = e3.get()
    convert = ""
    weight = bm.convertWeight(wt)
    # height = bm.convertHeight(int(ht),int(ht2))

    if weight > 0:

        convert = weight
        convert = "%.2f" % convert

    else:
        messagebox.showerror("Error", "Please enter a valid number")

    messagebox.showinfo("Body Mass Index", f"The body mass index is: {convert} ")


screen_frame = Frame(tk, width=300, height=300, bg="#06185c")
screen_frame.pack(pady=20)

img = ImageTk.PhotoImage(Image.open("images/people-icon.png"))
img_label = Label(tk, image=img)
img_label.pack()

e1 = Entry(screen_frame, text="Enter Weight", width=5, font=("Helvetica", 12))
e1.grid(column=0, row=2, pady=5)
e1.focus_set()

e2 = Entry(screen_frame, text=" Height (ft)", width=5, font=("Helvetica", 12))
e2.grid(column=0, row=6, pady=5)

e3 = Entry(screen_frame, text=" Height (in)", width=5, font=("Helvetica", 12))
e3.grid(column=0, row=10, pady=5)

wt = e1.get()
ht = e2.get()
ht2 = e3.get()


e1_label = Label(
    screen_frame,
    text="Enter Weight",
    bg="#06185c",
    fg="yellow",
    font=("Helvetica", 12),
).grid(column=0, row=1, pady=5)


e2_label = Label(
    screen_frame,
    text="Enter Height (ft)",
    bg="#06185c",
    fg="yellow",
    font=("Helvetica", 12),
).grid(column=0, row=5, pady=5)

e3_label = Label(
    screen_frame,
    text="Height (in)",
    bg="#06185c",
    fg="yellow",
    font=("Helvetica", 12),
).grid(column=0, row=9, pady=5)


bmi_button = Button(tk, text="Calculate BMI", command=callBMI)
bmi_button.pack(pady=15)

tk.mainloop()
