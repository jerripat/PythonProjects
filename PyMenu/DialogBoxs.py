#from argparse import FileType
#import pyautogui
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

#pyautogui.alert('Just a test', "Title")

root = tk.Tk()
root.title('File Dialog boxs')
root.resizable(False, False)
root.geometry("400x400")

filetypes = (
    ('Pics', '*.png'),
    ('All Files', '*.*')
)


def select_file():

    filetypes = (
        ('Pics', '*.png'),
        ('All Files', '*.*')
    )


def open_image():
    img_button = Button(root, text="Open Image", filetypes=(("PNG File", "*.png"),
                        ("JPG File", "*.jpg"), ("All Files", "*.*")), command=open_image).pack(pady=10)
    my_label = Label(root, text=root.filename).pack(pady=10)


filename = fd.askopenfilename(
    title='Open Files',
    initialdir='/',
    filetypes=filetypes)

showinfo(
    title='Selected File',
    message=filename
)

open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file()
)
open_button.pack(expand=True)
#img_button = Button(root, text="Open Image", command=open_image).pack(pady=10)

root.mainloop()
