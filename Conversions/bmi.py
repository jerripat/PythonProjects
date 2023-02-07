from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image



from formulas import BMICalc

# BMI = (mass(lb) / height ** 2 (in)) x 703

tk = Tk()
tk.title("BMI Calculator")
tk.geometry("600x600")
tk.configure(background="#06185c")

bm = BMICalc()

wt = IntVar()
ht = IntVar()
ht2 = IntVar()

wt.set("")
ht.set("")
ht2.set("")

t_label = Label(tk, text="BMI Calculator", font=("Helvetica", 12),bg="#06185c", fg ='yellow').pack(anchor="center",pady=20)

def callBMI():  # sourcery skip: square-identity
    wt = 0.00
    ht = 0.00
    ht2 = 0.00
    wt = e1.get()
    ht = e2.get()
    ht2 = e3.get()
    convert = ""
    weight = bm.convertWeight(wt)
    height = bm.convertHeight(int(ht),int(ht2))

    if float(weight) > 0 and float(height) > 0:

        convert = weight
        convert = "%.2f" % convert
        bmi = (float(convert) / (float(height) * float(height)))

    else:
        messagebox.showerror("Error", "Please enter a valid number")

    messagebox.showinfo("Body Mass Index", f"The body mass index is: {bmi} ")

img = ImageTk.PhotoImage(Image.open("images/people-icon.png"))
img_label = Label(tk, image=img)
img_label.pack(anchor=NW,padx=20)

screen_frame = Frame(tk, width=300, height=300, bg="#06185c")
screen_frame.pack(pady=20)


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

chart_frame = Frame(tk, bg="#06185c", width=300, height=300)
chart_frame.pack(pady=20)
chart = ImageTk.PhotoImage(Image.open("images/bmi_chart.png"))
chart_label = Label(chart_frame, image=chart)
chart_label.pack()


tk.mainloop()
