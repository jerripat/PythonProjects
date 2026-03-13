from tkinter import *

# Create a window
root = Tk()
root.title('Dropdown List')
root.geometry('400x300')
root.config(bg='lightblue')


def show():
    myLabel = Label(root, text='You selected:' + clicked.get(), font=("Helvetica", 18, "bold")).pack(pady=20)


choice = ['Apple',
          'Banana',
          'Cherry',
          'Date']
clicked = StringVar()
clicked.set('Apple')

drop = OptionMenu(root, clicked, *choice)
drop.pack()
myButton = Button(root, text='Get Selected Value', command=show).pack()

root.mainloop()
