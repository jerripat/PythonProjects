
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window


sg.set_options(font='Arial 18', background_color='teal',keep_on_top=True)
layout = [
    [sg.Text('This is a Text Box',background_color='teal')],
    [sg.Button('Click me!')]
    
]
    
WINDOW = sg.Window('Title', layout)

event, values = WINDOW.read()

Window.close(self)