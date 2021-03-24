import PySimpleGUIWeb as sg

sg.theme('Dark Blue 13')

# Global Variables
#height = int()
#width = int()
#height_grid = int()
#width_grid = int()

def open_window(height,width):
    layout = [[sg.Text("You've entered:")],
              [sg.Text('Height: ' + str(height)),  sg.Text('Width: ' + str(width)),  sg.Button("Clear"), sg.Button("Close")],
              [sg.Text('')],
              [sg.Button('yo', size=(5, 2), key=(x,y), pad=(0,0)) for x in range(width) for y in range(height)]]
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
    layout = [[sg.Text('How large is the working area?', font='Any 24')],
              [sg.Text('Height (meters)'), sg.Input(key='-h-')],
              [sg.Text('Width (meters)'), sg.Input(key='-w-')],
              [sg.Button("Continue", key="open")]]
    window = sg.Window("Main Window", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED or event is None:
            break
        if event == "open":
            # ============================================================================
            # Insert input validation to make sure height and width entered are integers
            # https://stackoverflow.com/questions/27310631/checking-if-input-is-an-integer
            # ============================================================================
            height = int(values['-h-'])
            width = int(values['-w-'])
            # Set grid variables
            height_grid = int(height*3)
            width_grid = int(width*3)
            # Debug/
            print('height: ', height)
            print('width: ', width)
            print('height_grid: ', height_grid)
            print('width_grid: ', width_grid)
            # /Debug
            window.close()
            open_window(height,width)
        
    window.close()
if __name__ == "__main__":
    main()