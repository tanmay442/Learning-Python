import os
import shutil as sh
import PySimpleGUI as sg

sg.theme('DarkAmber')  
sg.set_options(font=('Helvetica', 14))  

def sorter():
    os.chdir(f"{folder}")
    already=os.listdir()
    

    for i in (selected):
        if i not in already:
            os.mkdir(f"{i}")
            
        else:
            pass

    items = os.listdir()
    for i in items:
        print(i)

        if i.endswith(tuple(["exe", "jar", "appinstaller", "msi"])):
            sh.move((f"{folder}" + f"/{i}"), (f"{folder}" + "/Executable"))

        elif i.endswith(tuple(["mp4", "mov", "wvm", "flv", "avi", "avchd", "webm", "mkv"])):
            sh.move((f"{folder}" + f"/{i}"), (f"{folder}" + "/Media"))

        elif i.endswith(tuple(["pdf"])):
            sh.move((f"{folder}" + f"/{i}"), (f"{folder}" + "/PDF"))

        elif i.endswith(tuple(["jpeg", "jpg", "png", "psd", "webp", "raw", "psd"])):
            sh.move((f"{folder}" + f"/{i}"), (f"{folder}" + "/Images"))

        elif i.endswith(tuple(["txt"])):
            sh.move((f"{folder}" + f"/{i}"), (f"{folder}" + "/Text Files"))

        elif i.endswith(tuple(["mp3", "pcm", "wav", "aiff", "wma"])):
            sh.move((f"{folder}" + f"/{i}"), (f"{folder}" + "/Music"))

        elif i.endswith(tuple(["zip", "rar", "tar", "gz", "deb", "rpm", "pak"])):
            sh.move((f"{folder}" + f"/{i}"), (f"{folder}" + "/Compressed"))

        elif i.endswith(tuple(["py"])):
            sh.move((f"{folder}" + f"/{i}"), (f"{folder}" + "/Python"))

        else:
            pass
                
layout = [
    [sg.Text("Choose the Directory to implement the sorter", text_color='white'), sg.Input(), sg.FolderBrowse(key='-FOLDER-', button_color=('white', 'blue'))],
    [sg.Button("Submit", button_color=('white', 'green')), sg.Button("Cancel", button_color=('white', 'red'))],
    [sg.Listbox(values=['Executable', 'Media', 'PDF', 'Images', 'Text Files', 'Music', 'Compressed', 'Python'],
                select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE,
                key='-LIST-', size=(20, 5), text_color='white')]
]

window = sg.Window("Choose the Directory to implement the sorter", layout)

while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        folder = values['-FOLDER-']
        print(f"{folder}")
        selected = tuple(values['-LIST-'])
        print(selected)
        sorter()
        break


window.close()
