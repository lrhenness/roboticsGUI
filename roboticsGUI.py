import PySimpleGUIWeb as sg

sg.theme('Dark')

def open_window():
    grid = [[sg.B('yo', size=(5, 2), key=(x0,0), pad=((0,0),(0,0))) for x0 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x1,1), pad=((0,0),(0,0))) for x1 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x2,2), pad=((0,0),(0,1))) for x2 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x3,3), pad=((0,0),(0,0))) for x3 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x4,4), pad=((0,0),(0,0))) for x4 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x5,5), pad=((0,0),(0,1))) for x5 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x6,6), pad=((0,0),(0,0))) for x6 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x7,7), pad=((0,0),(0,0))) for x7 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x8,8), pad=((0,0),(0,1))) for x8 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x9,9), pad=((0,0),(0,0))) for x9 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x10,10), pad=((0,0),(0,0))) for x10 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x11,11), pad=((0,0),(0,1))) for x11 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x12,12), pad=((0,0),(0,0))) for x12 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x13,13), pad=((0,0),(0,0))) for x13 in range(15)],
            [sg.B('yo', size=(5, 2), key=(x14,14), pad=((0,0),(0,1))) for x14 in range(15)]]

    options = [[sg.Input(size=(5,1), key='-r1_v-'), sg.Text('Velocity for Robot 1 in meters/second', size=(35,1))],
               [sg.Input(size=(5,1), key='-r2_v-'), sg.Text('Velocity for Robot 2 in meters/second', size=(35,1))],
               [sg.CalendarButton('Calendar', size=(10,1), target='-calendar-', key='-calendar-'), sg.Text('Date for movement', size=(30,1))],
               [sg.Text('No date chosen', size=(10,1), key='-start_date-')],
               [sg.Input(size=(10,1), key='-start_time-'), sg.Text('Time for movement: HH:MM:SS', size=(30,1))],
               [sg.Text('Test Element 2')],
               [sg.Button('Clear', size=(10,1)), sg.Button('Exit', size=(10,1))]
               ]

    layout = [[sg.Text("Robotics GUI Capstone Project", justification="center", font='Any 24', auto_size_text='True')],
              [sg.Text('Made by Luken Henness', justification="center", font='Any 16', auto_size_text='True')],
              [sg.Text('')],
              [sg.Frame('Inputs Inputs Inputs Inputs Inputs',[[
                  sg.Column(grid, pad=((50,15),(15,15))),
                  sg.Text(' '),
                  sg.Column(options, pad=(15,15))
                  ]],
                  title_location='TITLE_LOCATION_TOP',
                  pad=((25,25),(25,25)),
              )]
              ]
    window = sg.Window("Second Window", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)

    #window['-output1-'].update('height variable goes here')
    #window['-output2-'].update('width variable goes here')
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED or event is None:
            break
        elif event == "Clear":
            main()
        print('Button pushed: ', event, values)
        #window['-pushed-'].update()
        
    window.close()

def main():
    layout = [[sg.Text('Welcome to the Robotics GUI Capstone Project!', justification='center', font='Any 48', auto_size_text='True')],
              [sg.Text('')],
              [sg.Text('Please make a selection.', justification="center", font='Any 36', auto_size_text='True')],
              [sg.Text('')],
              [sg.Button("Start Program", size=(40,4), pad=(5,15), key="open")]]
    window = sg.Window("RobGUI", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
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
