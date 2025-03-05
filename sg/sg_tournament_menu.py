import PySimpleGUI as sg
import draft
import sg.sg_game as sg_game
import sg.sg_table as sg_table
import sg.sg_schedule as sg_shedule
import tournament
from team import Team
from tournament import Tournament


def get_table(teams):
    teams = sorted(teams, key=lambda t: (-t.table_stat['points'], -t.table_stat['gd']))
    sg_table.main(teams)


def get_schedule(schedule):
    for game in schedule:
            print(game[0], game[1].name, game[2].name, game[3], game[4], game[5])
    sg_shedule.main(schedule)


def get_next_game(schedule):
    scheduled_games = []
    for game in schedule:
        if game[5] == 'Scheduled':
            scheduled_games.append(game)
    game = scheduled_games[0]
    sg_game.main(game)


def simulate_games(schedule):
    scheduled_games = []
    for game in schedule:
        if game[5] == 'Scheduled':
            scheduled_games.append(game)
    for game in scheduled_games:
        sg_game.main(game)


def main(tournament):
    t = tournament
    ### LAYOUTS ###
    frame_menu = [[sg.Button('Play next game', key='game')],
                  [sg.Button('Play all games', key='simulate')],
                  [sg.Button('Watch Schedule', key='schedule')],
                  [sg.Button('Tourney table', key='table')],
                  [sg.Button('Return to menu', key='menu')]]
    layout_menu = [[sg.Push(), sg.Frame('', frame_menu, element_justification='center'), sg.Push()]]
    window = sg.Window('Main menu', layout_menu, finalize=True, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'menu'):
            break
        if event == 'table':
            get_table(t.teams)
        if event == 'schedule':
            get_schedule(t.schedule)
        if event == 'game':
            get_next_game(t.schedule)
        if event == 'simulate':
            simulate_games(t.schedule)
    window.close()
