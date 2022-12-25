from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New Windows")
root.geometry("400x400")


def newWindow():
    new = Toplevel()
    new.title("Second window Windows")
    new.geometry("400x500")
    my_label = Label(new, text="This is a new window").pack(pady=20)

    my_img = ImageTk.PhotoImage(Image.open("Images/EmpireState.jpg"))
    img_label = Label(new, image=my_img).pack(pady=10)

    # Minimize original window
    #hide_button = Button(new, text="Hide Main Widow", command=root.iconify)
    #show_button = Button(new, text="Show Main Window", command=root.deiconify)

    # Withdraw original Window
    hide_button = Button(new, text="Hide Main Widow", command=root.withdraw)
    show_button = Button(new, text="Show Main Window", command=root.deiconify)
    hide_button.pack()
    show_button.pack()

    kill_original = Button(new, text="Kill Original",
                           command=root.destroy).pack(pady=10)
    destroy_button = Button(
        new, text="Quit", command=new.destroy).pack(pady=20)

    new.mainloop()


# Create new window
my_button = Button(root, text="Open new window", command=newWindow)
my_button.pack(pady=10)


root.mainloop()
