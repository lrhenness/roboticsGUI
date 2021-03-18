import PySimpleGUIWeb as sg
sg.theme('Dark Blue 13')

def open_window():
    layout = [[sg.Text("You've entered:")],
              [sg.Text("Height: ", height)],
              [sg.Text("Width: ", width)],
              [sg.Button("Back"), sg.Button("Close")]]
    window = sg.Window("Second Window", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED or event is None:
            break
        
    window.close()
def main():
    layout = [[sg.Text("How large is the working area?")],
              [sg.Text("Height (meters)...... "), sg.In(key='-h-')],
              [sg.Text("Width (meters)....... "), sg.In(key='-w-')],
              [sg.Button("Continue", key="open")]]
    window = sg.Window("Main Window", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED or event is None:
            break
        if event == "open":
            height = values['-h-']
            width = values['-w-']
            print(height)
            print(width)
            open_window()
        
    window.close()
if __name__ == "__main__":
    main()