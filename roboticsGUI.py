import PySimpleGUIWeb as sg

sg.theme('Dark')

def open_window():
    grid = [
           [sg.B('*', size=(5, 2), key=(0,0), pad=((1,0),(1,0))),sg.B('*', size=(5, 2), key=(1,0), pad=((0,0),(1,0))),sg.B('*', size=(5, 2), key=(2,0), pad=((0,1),(1,0))),sg.B('*', size=(5, 2), key=(3,0), pad=((0,0),(1,0))),sg.B('*', size=(5, 2), key=(4,0), pad=((0,0),(1,0))),sg.B('*', size=(5, 2), key=(5,0), pad=((0,1),(1,0))),sg.B('*', size=(5, 2), key=(6,0), pad=((0,0),(1,0))),sg.B('*', size=(5, 2), key=(7,0), pad=((0,0),(1,0))),sg.B('*', size=(5, 2), key=(8,0), pad=((0,1),(1,0))),sg.B('*', size=(5, 2), key=(9,0), pad=((0,0),(1,0))),sg.B('*', size=(5, 2), key=(10,0), pad=((0,0),(1,0))),sg.B('*', size=(5, 2), key=(11,0), pad=((0,1),(1,0))),sg.B('*', size=(5, 2), key=(12,0), pad=((0,0),(1,0))),sg.B('*', size=(5, 2), key=(13,0), pad=((0,0),(1,0))),sg.B('*', size=(5, 2), key=(14,0), pad=((0,1),(1,0)))],
           [sg.B('*', size=(5, 2), key=(0,1), pad=((1,0),(0,0))),sg.B('*', size=(5, 2), key=(1,1), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(2,1), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(3,1), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(4,1), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(5,1), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(6,1), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(7,1), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(8,1), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(9,1), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(10,1), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(11,1), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(12,1), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(13,1), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(14,1), pad=((0,1),(0,0)))],
           [sg.B('*', size=(5, 2), key=(0,2), pad=((1,0),(0,1))),sg.B('*', size=(5, 2), key=(1,2), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(2,2), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(3,2), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(4,2), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(5,2), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(6,2), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(7,2), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(8,2), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(9,2), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(10,2), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(11,2), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(12,2), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(13,2), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(14,2), pad=((0,1),(0,1)))],
           [sg.B('*', size=(5, 2), key=(0,3), pad=((1,0),(0,0))),sg.B('*', size=(5, 2), key=(1,3), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(2,3), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(3,3), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(4,3), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(5,3), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(6,3), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(7,3), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(8,3), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(9,3), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(10,3), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(11,3), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(12,3), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(13,3), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(14,3), pad=((0,1),(0,0)))],
           [sg.B('*', size=(5, 2), key=(0,4), pad=((1,0),(0,0))),sg.B('*', size=(5, 2), key=(1,4), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(2,4), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(3,4), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(4,4), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(5,4), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(6,4), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(7,4), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(8,4), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(9,4), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(10,4), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(11,4), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(12,4), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(13,4), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(14,4), pad=((0,1),(0,0)))],
           [sg.B('*', size=(5, 2), key=(0,5), pad=((1,0),(0,1))),sg.B('*', size=(5, 2), key=(1,5), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(2,5), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(3,5), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(4,5), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(5,5), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(6,5), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(7,5), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(8,5), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(9,5), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(10,5), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(11,5), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(12,5), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(13,5), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(14,5), pad=((0,1),(0,1)))],
           [sg.B('*', size=(5, 2), key=(0,6), pad=((1,0),(0,0))),sg.B('*', size=(5, 2), key=(1,6), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(2,6), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(3,6), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(4,6), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(5,6), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(6,6), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(7,6), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(8,6), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(9,6), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(10,6), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(11,6), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(12,6), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(13,6), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(14,6), pad=((0,1),(0,0)))],
           [sg.B('*', size=(5, 2), key=(0,7), pad=((1,0),(0,0))),sg.B('*', size=(5, 2), key=(1,7), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(2,7), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(3,7), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(4,7), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(5,7), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(6,7), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(7,7), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(8,7), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(9,7), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(10,7), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(11,7), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(12,7), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(13,7), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(14,7), pad=((0,1),(0,0)))],
           [sg.B('*', size=(5, 2), key=(0,8), pad=((1,0),(0,1))),sg.B('*', size=(5, 2), key=(1,8), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(2,8), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(3,8), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(4,8), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(5,8), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(6,8), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(7,8), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(8,8), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(9,8), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(10,8), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(11,8), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(12,8), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(13,8), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(14,8), pad=((0,1),(0,1)))],
           [sg.B('*', size=(5, 2), key=(0,9), pad=((1,0),(0,0))),sg.B('*', size=(5, 2), key=(1,9), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(2,9), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(3,9), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(4,9), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(5,9), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(6,9), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(7,9), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(8,9), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(9,9), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(10,9), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(11,9), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(12,9), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(13,9), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(14,9), pad=((0,1),(0,0)))],
           [sg.B('*', size=(5, 2), key=(0,11), pad=((1,0),(0,1))),sg.B('*', size=(5, 2), key=(1,11), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(2,11), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(3,11), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(4,11), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(5,11), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(6,11), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(7,11), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(8,11), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(9,11), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(10,11), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(11,11), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(12,11), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(13,11), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(14,11), pad=((0,1),(0,1)))],
           [sg.B('*', size=(5, 2), key=(0,12), pad=((1,0),(0,0))),sg.B('*', size=(5, 2), key=(1,12), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(2,12), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(3,12), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(4,12), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(5,12), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(6,12), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(7,12), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(8,12), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(9,12), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(10,12), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(11,12), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(12,12), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(13,12), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(14,12), pad=((0,1),(0,0)))],
           [sg.B('*', size=(5, 2), key=(0,13), pad=((1,0),(0,0))),sg.B('*', size=(5, 2), key=(1,13), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(2,13), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(3,13), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(4,13), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(5,13), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(6,13), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(7,13), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(8,13), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(9,13), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(10,13), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(11,13), pad=((0,1),(0,0))),sg.B('*', size=(5, 2), key=(12,13), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(13,13), pad=((0,0),(0,0))),sg.B('*', size=(5, 2), key=(14,13), pad=((0,1),(0,0)))],
           [sg.B('*', size=(5, 2), key=(0,14), pad=((1,0),(0,1))),sg.B('*', size=(5, 2), key=(1,14), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(2,14), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(3,14), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(4,14), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(5,14), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(6,14), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(7,14), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(8,14), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(9,14), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(10,14), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(11,14), pad=((0,1),(0,1))),sg.B('*', size=(5, 2), key=(12,14), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(13,14), pad=((0,0),(0,1))),sg.B('*', size=(5, 2), key=(14,14), pad=((0,1),(0,1)))]
           ]

    options = [[sg.Input(size=(5,1), key='-r1_v-'), sg.Text('Velocity for Robot 1 in meters/second', size=(35,1))],
               [sg.Input(size=(5,1), key='-r2_v-'), sg.Text('Velocity for Robot 2 in meters/second', size=(35,1))],
               [sg.CalendarButton('Calendar', size=(10,1), target='-start_date-', key='-calendar-'), sg.Text('Date chosen: '), sg.Text('None yet', size=(25,1), key='-start_date-')],
               [sg.Input(size=(10,1), key='-start_time-'), sg.Text('Time for movement: HH:MM:SS', size=(30,1))],
               [sg.Text('Last button pushed:'), sg.Text(' ', key=('-pushed-'))],
               [sg.Button('Clear', size=(10,1)), sg.Button('Exit', size=(10,1))]
               ]

    layout = [[sg.Text("Robotics GUI Capstone Project", justification="center", font='Any 38', size=(125,2))],
              [sg.Text('Made by Luken Henness', justification="center", font='Any 16', size=(125,1))],
              #[sg.Text('')],
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

    #Main Event Loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED or event is None:
            break
        elif event == "Clear":
            main()
        #print('Button pushed: ', event)
        window['-pushed-'].update(str(event))
        
    window.close()

def main():
    layout = [[sg.Text("Robotics GUI Capstone Project", justification="center", font='Any 38', size=(125,2))],
              [sg.Text('Made by Luken Henness', justification="center", font='Any 16', size=(125,1))],
              [sg.Button("Start Program", size=(35,4), pad=((150,150),(15,15)), key="open")]]
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
