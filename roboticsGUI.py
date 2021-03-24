import PySimpleGUIWeb as sg
sg.theme('Dark Blue 13')

def open_window():
    layout = [[sg.Text("You've entered:")],
              [sg.Text('Height: ', height)],
              [sg.Text('Width: ', width)],
              [sg.Button("Back"), sg.Button("Close")]]
    window = sg.Window("Second Window", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    choice = None
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
            int(height) = values['-h-']
            int(width) = values['-w-']
            # Set grid variables
            int(height_grid) = height*3
            int(width_grid) = width*3
            print('height: ', height)
            print('width: ', width)
            print('height_grid: ', height_grid)
            print('width_grid: ', width_grid)
            open_window()
        
    window.close()
if __name__ == "__main__":
    main()