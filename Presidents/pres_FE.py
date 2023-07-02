from tkinter import *
import tkinter as tk


mainwindow = tk.Tk()
mainwindow.geometry("600x600")
mainwindow.resizable(True, True)
mainwindow.title("The Presidents")

menubar = tk.Menu(mainwindow)
mainwindow.config(menu=menubar, bg="darkblue")

sub_menu = Menu(menubar, tearoff=0)
sub_menu.add_command(label="Exit", command=mainwindow.destroy)

# con_menu = Menu(menubar, tearoff=0)
# con_menu.add_command(label="Metric")
# sub_con_menu= Menu(con_menu, tearoff=0)

# sub_con_menu.add_cascade(label="Ft to Met", menu=con_menu)
# #sub_con_menu.add_command(label="Met to Ft",menu=con_menu)

menubar.add_cascade(label="File", menu=sub_menu)
menubar.add_cascade(label="Conversions", menu=menubar)

import tkinter as tk
from tkinter import messagebox

def show_option1():
    messagebox.showinfo("Menu selection", "You selected Option 1")

def show_option2():
    messagebox.showinfo("Menu selection", "You selected Option 2")

def show_sub_option1():
    messagebox.showinfo("Menu selection", "You selected Sub-Option 1")

def show_sub_option2():
    messagebox.showinfo("Menu selection", "You selected Sub-Option 2")

root = tk.Tk()

# Create main menu bar
menubar = tk.Menu(root)

# Create the submenu 
file = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Option 1', menu = file)
file.add_command(label ='Sub-Option 1', command = show_sub_option1)
file.add_command(label ='Sub-Option 2', command = show_sub_option2)

# Adding another menu entry
menubar.add_command(label ='Option 2', command = show_option2)

root.config(menu = menubar)
root.mainloop()


# def button_clicked():
#     print("Button clicked")
Sure, here's a simple example of a command line interface with menus and sub-menus using a Python script:

```python
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            sub_menu_1()
        elif choice == "2":
            sub_menu_2()
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")
            
            
def sub_menu_1():
    while True:
        print("\nSub Menu 1:")
        print("1. Sub-option 1")
        print("2. Sub-option 2")
        print("3. Return to main menu")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You chose Sub-option 1")
        elif choice == "2":
            print("You chose Sub-option 2")
        elif choice == "3":
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice, please try again.")

            
def sub_menu_2():
    while True:
        print("\nSub Menu 2:")
        print("1. Sub-option 3")
        print("2. Sub-option 4")
        print("3. Return to main menu")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You chose Sub-option 3")
        elif choice == "2":
            print("You chose Sub-option 4")
        elif choice == "3":
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice, please try again.")
            
            
if __name__ == "__main__":
    main_menu()
```

In this script, we have a `main_menu()` function that displays the main menu. When the user selects an option, it calls either `sub_menu_1()` or `sub_menu_2()`. In these sub-menu functions, the user can choose sub-options or return to the main menu. If the user chooses "Exit" in the main menu, the script will terminate. 
mainwindow.mainloop()