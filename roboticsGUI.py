#!/usr/bin/env python
import PySimpleGUIWeb as sg
import time

# Basic example of PSGWeb

def make_win1():
    # Define the layout of the page. This can be done in multiple functions.
    layout = [
        [sg.Text('This is window 1!')],
        [sg.Button('Press me to open a window2', key='open_window2')]
    ]
    return sg.Window('Demo window..', layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)

def make_win1():
    # Define the layout of the page. This can be done in multiple functions.
    layout = [
        [sg.Text('This is window 2! Hell yeah.')],
        [sg.Button('Press me to open a window1', key='open_window1')]
    ]
    return sg.Window('Demo window..', layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)

window = make_win1(), None    # Start off with first window open

def main():
    while True:
        window, event, values = window.read(timeout=100)
        if event != sg.TIMEOUT_KEY:
            print('event called: ', event)
        if event == 'open_window1':
            print('Opening window 1...')
            window1 = make_win1()
        if event == 'open_window2':
            print('Opening window 2...')
            window2 = make_win2()
        if event is None:
            break
    window.close()

main()
print('Program terminating normally')
