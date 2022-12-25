from tkinter import *
from tkinter import messagebox

def  custom_quit():
    answer=messagebox.askokcancel("Are you sure?", "Your data will be lost if you exit")
    if (answer):
        quit()
        
# the main window 
# the actual menu 
root=Tk()
root.geometry('444x444')

text=Label(root,text='*my first menu*').pack()

menu1=Menu(root)
root.configure(menu=menu1)

submenu1=Menu(menu1)
menu1.add_cascade(label='File', menu=submenu1)
sub2menu=Menu(submenu1)
sub2menu.add_command(label='Recent')
sub2menu.add_command(label='Browse')

submenu1.add_command(label='New File')
submenu1.add_cascade(label='Open File', menu=sub2menu)
submenu1.add_command(label='Save As')
submenu1.add_command(label='Print')
submenu1.add_command(label='Quit', command=custom_quit)

submenu2=Menu(menu1)
menu1.add_cascade(label='Edit', menu=submenu2)
submenu2.add_command(label='Undo')
submenu2.add_cascade(label='Redo')
submenu2.add_command(label='Cut')
submenu2.add_command(label='Copy')
submenu2.add_command(label='Paste')
submenu2.add_command(label='Select All')

submenu3=Menu(menu1)
menu1.add_cascade(label='Format', menu=submenu3)
submenu3.add_command(label='Indent Region')
submenu3.add_command(label='Comment')
submenu3.add_command(label='All')
submenu3.add_command(label='Selected')
submenu3.add_command(label='Format Paragraph')

submenu4=Menu(menu1)
menu1.add_cascade(label='Run', menu=submenu4)
submenu4.add_command(label='Python Shell')
submenu4.add_cascade(label='Run Module')
submenu4.add_command(label='Check Module')

submenu5=Menu(menu1)
menu1.add_cascade(label='Options', menu=submenu5)
submenu5.add_command(label='Configure IDLE')
submenu5.add_cascade(label='Show Code Context')
submenu5.add_command(label='Zoom Height')

submenu6=Menu(menu1)
menu1.add_cascade(label='Window', menu=submenu6)
submenu6.add_command(label='Python 3.8.? shell')
submenu6.add_cascade(label='Untitled')
# submenu6.add_command(label='Resize window', command=Res)
# submenu6.add_command(label='Normal size window',command=B2N)
# submenu6.add_command(label='Large window', command=Full)

submenu7=Menu(menu1)
menu1.add_cascade(label='Help', menu=submenu7)
submenu7.add_command(label='About IDLE')
submenu7.add_cascade(label='IDLE Help')
submenu7.add_command(label='FAQ')
submenu7.add_command(label='Contact Us')

# Option 2
# Python console help menu // optonMenu

option_menu = {
    
    1: 'Option 1' ,
    2: 'Option 2' ,
    3: 'Exit' ,
}

# This function will print out your option menu
def print_options():
    
     for key in option_menu.keys():
         print(key , '--------' , option_menu[key])

# Create your option functions here. / Add more for your needs

def option1():
    pass

def option2():
    pass

if __name__ == '__main__':
    
    while (True):
        print_options()
        
        option = ""
        
        try:
            # Edit 'Enter option' for your need
                option = int(input('Enter option: '))
        
        except:
            
            print('option' , option)
            
        if option == 1:
            option1()
            #
            # Code here
            #
            # Also change the print message for your needs
            print("OPTION1 WORKING....")
        
        elif option == 2:
                option2()
                # Code here
                #
                # Change message
                print("OPTION@ WORKING...")
                
        elif option == 3:
            
            print("Exit code...")
            
        else:
            print('invalid option:' , option , 'Try again...')