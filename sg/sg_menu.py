import PySimpleGUI as sg
import draft
import sg.sg_game as sg_game
from sg import sg_tournament_menu
from team import Team
from tournament import Tournament


def start_single():
    team1 = Team('blue')
    team2 = Team('green')
    teams = [team1, team2]
    draft.draft(teams)
    game = [0, team1, team2, 0, 0, 'Scheduled'] # Много лишней инфы ради генерации матчей в турнирах
    sg_game.main(game)


def start_tournament():
    blue = Team('blue')
    green = Team('green')
    red = Team('red')
    yellow = Team('yellow')

    teams = [blue, green, red, yellow]

    # Инициализируем турнир и заодно проводим
    t = Tournament('Test League', 'league', teams, 2)

    sg_tournament_menu.main(t)

def main():
    ### LAYOUTS ###
    frame_menu = [[sg.Button('Generate Single Game', key='single')],
                  [sg.Button('Generate Tournament', key='tournament')], [sg.Button('Exit', key='exit')]]
    layout_menu = [[sg.Push(), sg.Frame('', frame_menu, element_justification='center'), sg.Push()]]
    window = sg.Window('Main menu', layout_menu, finalize=True, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'exit'):
            break
        if event == 'single':
            start_single()
        if event =='tournament':
            start_tournament()
    window.close()
