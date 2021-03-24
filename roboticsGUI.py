import PySimpleGUIWeb as sg

sg.theme('Dark Blue 13')

def open_window():
    layout = [[sg.Text("Robotics GUI Capstone Project", justification="center", size=(30, 1), font='Any 48')],
              [sg.Text('Made by Luken Henness', justification="center", size=(20, 1), font='Any 24')],
              [sg.Text('')],
              [sg.Button('yo', size=(5, 2), key=(x0,0), pad=(0,0)) for x0 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x1,1), pad=(0,0)) for x1 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x2,2), pad=(0,0)) for x2 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x3,3), pad=(0,0)) for x3 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x4,4), pad=(0,0)) for x4 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x5,5), pad=(0,0)) for x5 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x6,6), pad=(0,0)) for x6 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x7,7), pad=(0,0)) for x7 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x8,8), pad=(0,0)) for x8 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x9,9), pad=(0,0)) for x9 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x10,10), pad=(0,0)) for x10 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x11,11), pad=(0,0)) for x11 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x12,12), pad=(0,0)) for x12 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x13,13), pad=(0,0)) for x13 in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x14,14), pad=(0,0)) for x14 in range(15)],
              ]
    window = sg.Window("Second Window", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)

    #window['-output1-'].update('height variable goes here')
    #window['-output2-'].update('width variable goes here')
    while True:
        event, values = window.read()
        if event == "Exit" or event == "Close" or event == sg.WIN_CLOSED or event is None:
            break
        elif event == "Clear":
            main()
        
    window.close()

def main():
    layout = [[sg.Text('Welcome to the Robotics GUI Capstone Project!', justification='center', size=(30, 1), font='Any 48')],
              [sg.Text('Please make a selection.', justification="center", size=(20, 1), font='Any 36')],
              [sg.Button("Start Program", size=(10,4), pad=(5,15), key="open")]]
    window = sg.Window("Main Window", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED or event is None:
            break
        if event == "open":
            open_window()
            window.close()
        
    window.close()
if __name__ == "__main__":
    main()
