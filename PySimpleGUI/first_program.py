
import PySimpleGUI as sg
#import PySimpleGUIQt as sg
#import PySimpleGUI as sg
#import PySimpleGUI as sg


#sg.set_options(font='Arial 18', background_color='teal',keep_on_top=True)

#def main():
layout = [
            [sg.Text('My Window')],
            #[sg.Input(key='-IN-')],
            [sg.Button('Go!'),sg.Button('Exit')]
            #[sg.Text(30, key='-OUT-')]
            #[sg.Button('Go!'),sg.Button('Exit')]
        ]

window = sg.Window('Window Title', layout)

# while True:
#         event, values = window.read()
#         print(event, values)
#         if event in [sg.WIN_CLOSED, 'Exit']:
#             break
# window['-OUT-'].update(f'You Clicked {event}')
event, values =window.read()

window.close()