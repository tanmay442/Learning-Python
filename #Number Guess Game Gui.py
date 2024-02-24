import PySimpleGUI as sg
import random

class NumberListGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def generate(self):
        return set(range(self.start, self.end+1))

def numberguessgame():
    random_number = random.randint(1, 100)
    almostthere = NumberListGenerator(random_number-5, random_number+5)
    soclose = NumberListGenerator(random_number-10, random_number+10)
    close = NumberListGenerator(random_number-15, random_number+15)
    near = NumberListGenerator(random_number-25, random_number+25)
    far = NumberListGenerator(random_number-40, random_number+40)
    toofar = NumberListGenerator(random_number-60, random_number+60)
    noteventrying = NumberListGenerator(random_number-99, random_number+99)

    sg.theme('DarkAmber')  

    layout = [[sg.Text("Welcome to the Number Guessing Game! \nYou have to guess a number between 1 and 100.", font=("Helvetica", 18))],
              [sg.Text("Enter any number:", font=("Helvetica", 14)), sg.Input(key='-IN-',)],
              [sg.Button('Submit', bind_return_key=True, button_color=('white', 'green')), sg.Button('Exit', button_color=('white', 'red'))],  
              [sg.Text(size=(40,1), key='-OUTPUT-', text_color='yellow', font=('Helvetica', 16, 'bold'))]]  

    window = sg.Window('Number Guessing Game', layout, size=(600,400))
 
    count=0

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Submit':
            g = int(values['-IN-'])
            window['-IN-'].update('')  
            if g == random_number:
                sg.popup(f"Congratulations! You Guessed it in {count} attempts", title="Congratulations")
                break
            elif g in soclose.generate().difference(almostthere.generate()):
                window['-OUTPUT-'].update("You are so close to it")
            elif g in close.generate().difference(soclose.generate()):
                window['-OUTPUT-'].update("You are close to it")
            elif g in near.generate().difference(close.generate()):
                window['-OUTPUT-'].update("You are somewhat near to it")
            elif g in far.generate().difference(near.generate()):
                window['-OUTPUT-'].update("You are far from it")
            elif g in toofar.generate().difference(far.generate()):
                window['-OUTPUT-'].update("You are too far from it")
            elif g in noteventrying.generate().difference(toofar.generate()):
                window['-OUTPUT-'].update("You are not even trying")
            elif g in almostthere.generate():
                window['-OUTPUT-'].update("You are almost there")
            else:
                window['-OUTPUT-'].update("Choose Correct range")
                numberguessgame()
            count+=1

    window.close()

    play_again = sg.popup_yes_no('Do you want to play again?', title='Play Again')
    if play_again == 'Yes':
        numberguessgame()

numberguessgame()
