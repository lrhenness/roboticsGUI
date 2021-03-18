import PySimpleGUIWeb as sg
def open_window():
    layout = [[sg.Text("New Window", key="new")]]
    window = sg.Window("Second Window", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()
def main():
    layout = [[sg.Button("Open Window", key="open")]]
    window = sg.Window("Main Window", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "open":
            open_window()
        
    window.close()
if __name__ == "__main__":
    main()
