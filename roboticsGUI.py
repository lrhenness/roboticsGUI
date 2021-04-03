import PySimpleGUIWeb as sg

sg.theme('Dark')

def open_window():
    # Appologies for the giant and un-maintainable wall of text that follows.
    # I messed with for loops to draw out the layout for the grid but with
    # needing to change multiple things in each button it was going to be
    # quicker for me to just write it out like this for the project. 
    # Please merge a fix for this eye sore!
    grid = [[sg.B('*', size=(3,1), key=(0,24), pad=((1,0),(1,0))),sg.B('*', size=(3,1), key=(1,24), pad=((0,0),(0,1))),sg.B('*', size=(3,1), key=(2,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(3,24), pad=((0,0),(0,1))),sg.B('*', size=(3,1), key=(4,24), pad=((0,0),(0,1))),sg.B('*', size=(3,1), key=(5,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(6,24), pad=((0,0),(0,1))),sg.B('*', size=(3,1), key=(7,24), pad=((0,0),(0,1))),sg.B('*', size=(3,1), key=(8,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(9,24), pad=((0,0),(0,1))),sg.B('*', size=(3,1), key=(10,24), pad=((0,0),(0,1))),sg.B('*', size=(3,1), key=(11,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(12,24), pad=((0,0),(0,1))),sg.B('*', size=(3,1), key=(13,24), pad=((0,0),(0,1))),sg.B('*', size=(3,1), key=(24,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(15,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(16,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(17,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(18,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(19,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(20,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(21,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(22,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(23,24), pad=((0,1),(0,1))),sg.B('*', size=(3,1), key=(24,24), pad=((0,1),(0,1)))]]

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
