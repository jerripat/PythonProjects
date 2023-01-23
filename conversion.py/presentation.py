from tkinter import *
from formulas import *
tk = Tk()
tk.title("Conversion Calculator")
tk.geometry("400x400")


def callMenu():
    num = e.get()
    convert = FtoC(num)
    display_label = Label(tk, text=f"You entered : {num}")



my_label = Label(tk,text="Enter Number to convert",
                 font=("Helvetica",16),fg='#471bcc').pack(pady=10)
e = Entry(tk, font=("Helvetica",12))
e.pack(pady=10)
my_button = Button(tk,text="Convert",font=("Helvetica",12),fg='#120e8c',command=callMenu).pack(pady=15)
menu_label = Label(tk).pack(pady=10)

 # import pyMenu
    # ans = input('Start conversions?(y/n) :')
    # x = pyMenu.menu_handler()

    # if ans == 'y':
    #         print('Opening menu...')
    #         exec(open('pyMenu.py').read())
    # else:
    #     print('Closing menu...')
    #     exit()

tk.mainloop()
