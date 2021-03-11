#!/usr/bin/env python
import PySimpleGUIWeb as sg

# Basic example of PSGWeb

def main():
    # Define the layout of the page. This can be done in multiple functions.
    layout = [
        [sg.Text('This is a text element')],
        [sg.Input()],
        [sg.Combo(['Combo 1','Combo 2'])],
        [sg.Text('If you close the browser tab, the app will exit gracefully')],
        [sg.InputText('Source')],
        [sg.InputText('Dest')],
        [sg.Ok(), 
        sg.Cancel(),
        sg.Button('Yo', key='button_yo')]
    ]

    window = sg.Window('Demo window..', layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    #i = 0
    while True:
        event, values = window.read(timeout=1)
        #if event != sg.TIMEOUT_KEY:
        #    print(event, values)
        if event == 'button_yo':
            yo()
        if event is None:
            break
        #i += 1
    window.close()

def yo():
    # Testing multiple layouts
    layout = [
        [sg.Text('Hello World!')],
        [sg.Ok(), sg.Cancel()]
    ]

    window = sg.Window('Yo test window..', layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)


main()
print('Program terminating normally')
