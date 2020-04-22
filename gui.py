import PySimpleGUI as sg
import matchGenerator
from matchGenerator import count,playerList

sg.theme("Reddit")
layout = [[sg.Button('View Players'), sg.Button('Generate Matches'), sg.Exit()] ]

window = sg.Window('Random Match Generator').Layout(layout)

while True:         
    event, values = window.Read()
    if event in (None, 'Exit'):
        break

    if event == 'View Players':
        team = matchGenerator.viewPlayers()
        sg.popup("The players are:",team)

    elif event == 'Generate Matches':
        list = matchGenerator.matchView(count,playerList)
        sg.popup("The matches are between:",list)
window.Close()