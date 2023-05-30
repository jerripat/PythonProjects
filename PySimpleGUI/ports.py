import PySimpleGUI as sg
#import PySimpleGUIQt as sgq
#import PySimpleGUIWx as sgq
#import PySimpleGUIWeb as sgq

def main():  # sourcery skip: merge-comparisons
    
    layout = [[sg.Text('My Window!')],
        [sg.input(key='-IN-')],
        [sg.Text(size=(30,1), key='-OUT-')],
        [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('My Window', layout)
    
    while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            window['-OUT-'].update(values['-IN-'])

    window.close()