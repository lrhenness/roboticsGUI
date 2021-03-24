import PySimpleGUIWeb as sg

sg.theme('Dark Blue 13')

# Global Variables
#height = int()
#width = int()
#height_grid = int()
#width_grid = int()

def open_window():
    layout = [[sg.Text("Robotics GUI Capstone Project", justification="center", font='Any 48')],
              [sg.Text('Made by Luken Henness', justification="center", font='Any 24')],
              [sg.Text('')],
              [sg.Button('yo', size=(5, 2), key=(x0,y0), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x1,y1), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x2,y2), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x3,y3), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x4,y4), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x5,y5), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x6,y6), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x7,y7), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x8,y8), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x9,y9), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x10,y10), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x11,y11), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x12,y12), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x13,y13), pad=(0,0)) for x in range(15)],
              [sg.Button('yo', size=(5, 2), key=(x14,y14), pad=(0,0)) for x in range(15)],
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
    layout = [[sg.Text('Welcome to the Robotics GUI Capstone Project!', justification="center", font='Any 48')],
              [sg.Text('Please make a selection.', justification="center", font='Any 36')],
              [sg.Button("Start Program", size=(10,4), pad=(5,5), key="open")]]
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
