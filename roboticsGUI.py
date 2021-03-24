import PySimpleGUIWeb as sg

sg.theme('Dark Blue 13')

# Global Variables
#height = int()
#width = int()
#height_grid = int()
#width_grid = int()

def open_window(height,width):
    layout = [[sg.Text("You've entered:")],
              [sg.Text('Height: '), sg.Text(size=(40,1), key='-h-')],
              [sg.Text('Width: '), sg.Text(size=(40,1), key='-w-')],
              [sg.Button("Back"), sg.Button("Close")]]
    window = sg.Window("Second Window", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    #choice = None

    # Debug/
    print('open_window() height: ', height)
    print('open_window() width: ', width)
    # /Debug
    window['-h-'].update('height variable goes here')
    window['-w-'].update('width variable goes here')
    while True:
        event, values = window.read()
        if event == "Exit" or event == "Close" or event == sg.WIN_CLOSED or event is None:
            break
        elif event == "Back":
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
            open_window(height,width)
            # /Debug
        
    window.close()
if __name__ == "__main__":
    main()