import os
import PySimpleGUI as sg

sg.theme('DarkAmber')  

def ren():     
    files_list=(os.listdir(f"{folder}"))
    files_list=sorted(files_list)
    ln=len(files_list) 

    n=0
    for i in range(ln):
        n+=1

        a=files_list[i][::-1]            
        b=a.find(".")        
        extension=a[:b+1]
        extension=extension[::-1]
        
        os.rename(folder+"/"+files_list[i],folder+"/"+f"{n}%%##$$"+extension)
        files_list[i]=f"{n}%%##$$"+extension 
           
    n=0
    for j in files_list:
        n+=1
        os.rename(folder+"/"+j,folder+"/"+f"{n}{ctile}"+extension)

layout = [
    [sg.Text("Choose the Directory to implement the sorter", text_color='white'), sg.Input(), sg.FolderBrowse(key='-FOLDER-', button_color=('white', 'blue'))],
    
    [[sg.Text("Enter the Common Title")],
          [sg.Input(key='-OP-', text_color='white', background_color='dark blue')]],

    [sg.Button("Submit", button_color=('white', 'green')), sg.Button("Cancel", button_color=('white', 'red'))],
    
]

window = sg.Window("Choose the Directory to Rename the files", layout, text_justification='center')

while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        folder = values['-FOLDER-']
        ctile = values['-OP-']        
        print("Selected",folder)
        ren()
        break

window.close()
