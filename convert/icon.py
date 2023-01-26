import tkinter as tk

root = tk.Tk()

root.title("Conversion Calculator")
root.geometry("400x400")
root.configure(background="#06185c")
#img = tk.PhotoImage(file="uninstall.ico")
root.tk.call('wm','iconbitmap',root._w,'/home/jerripat/PythonProjects/convert/uninstall.ico')


root.mainloop()
