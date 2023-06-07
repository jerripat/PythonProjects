"""
    The Official Python GUI Programming with PySimpleGUI Course

    The PySimpleGUI Ports

    http://www.PySimpleGUI.org
"""

#import PySimpleGUI as sg
#import PySimpleGUIQt as sg
import PySimpleGUIWx as sg
# import PySimpleGUIWeb as sg


def main():

    layout = [[sg.Text('My Window')],
              [sg.Input(key='-IN-')],
              [sg.Text(size=(100,30), key='-OUT-')],
              [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout)

    while True:         # Event Loop
        event, values = window.read()
        print(event, values)
        if event in [sg.WIN_CLOSED, 'Exit']:
            break

        window['-OUT-'].update(f'You clicked {event}')

    window.close()


if __name__ == '__main__':
    main()
