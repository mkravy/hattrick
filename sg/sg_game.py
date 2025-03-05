import PySimpleGUI as sg
import draft
import tournament
from game import Game
from team import Team
import random as r
import time
from plays import plays_generator as pg


def change_scoreboard_thread(window):
    while True:
        window.write_event_value(('-THREAD-', 'scoreboard'), 'scoreboard')
        time.sleep(1)


def main(game_info):
    team1 = game_info[1]
    team2 = game_info[2]
    teams = [team1, team2]
    # draft.draft(teams)
    game = Game(team1, team2)

    table_lineup_home = [[sg.Table([[p.name, p.position, p.skill] for p in team1.lineup],
                                   headings=['Player', 'Pos', 'Skill'], justification='center', num_rows=11,
                                   hide_vertical_scroll=True, auto_size_columns=False, col_widths=[15, 4, 4])]]

    table_lineup_away = [[sg.Table([[p.name, p.position, p.skill] for p in team2.lineup],
                                   headings=['Player', 'Pos', 'Skill'], justification='center', num_rows=11,
                                   hide_vertical_scroll=True, auto_size_columns=False, col_widths=[15, 4, 4])]]

    table_bench_home = [[sg.Table([[p.name, p.position, p.skill] for p in team1.bench],
                                  headings=['Player', 'Pos', 'Skill'], justification='center', num_rows=7,
                                  hide_vertical_scroll=True, auto_size_columns=False, col_widths=[15, 4, 4])]]

    table_bench_away = [[sg.Table([[p.name, p.position, p.skill] for p in team2.bench],
                                  headings=['Player', 'Pos', 'Skill'], justification='center', num_rows=7,
                                  hide_vertical_scroll=True, auto_size_columns=False, col_widths=[15, 4, 4])]]
    ### SCOREBOARD ###
    frame_scoreboard_home = [[sg.Text(team1.name, key='team1')],
                             [sg.Push(), sg.Text('0', font=('Comic Sans', 20,), justification='center', key='score1'),
                              sg.Push()]]
    frame_scoreboard_away = [[sg.Text(team2.name, key='team2')],
                             [sg.Push(), sg.Text('0', font=('Comic Sans', 20,), justification='center', key='score2'),
                              sg.Push()]]
    frame_scoreboard_timer = [[sg.Text(f'0/6', key='timer')]]

    table_plays = [[sg.Table([[i + 1, 'Total', team1.name] for i in range(6)],
                             headings=['#', 'Plays', 'Team'], key='plays', justification='center', num_rows=6,
                             hide_vertical_scroll=True, auto_size_columns=False, col_widths=[4, 10, 10])]]

    frame_scoreboard = [[sg.Frame('', frame_scoreboard_home), sg.Frame('', frame_scoreboard_timer),
                         sg.Frame('', frame_scoreboard_away)],
                        [table_plays]]

    frame_total = [[sg.Frame(team1.name, table_lineup_home, element_justification='center', pad=(5, 5)),
                    sg.Frame(team2.name, table_lineup_away, element_justification='center', pad=(5, 3)),
                    sg.Frame('', frame_scoreboard, element_justification='center', pad=(5, 5))],
                   [sg.Frame('Bench', table_bench_home, element_justification='center', pad=(5, 0)),
                    sg.Frame('Bench', table_bench_away, element_justification='center', pad=(5, 0)), sg.Sizegrip()]]
    ### LAYOUTS ###
    layout_lineup = [[sg.Push(), sg.Frame('', frame_total), sg.Push()]]

    window = sg.Window('Test', layout_lineup, finalize=True, resizable=True)
    window.start_thread(lambda: change_scoreboard_thread(window), ('-THREAD-', '-THREAD ENDED-'))
    # while True:
    score1 = 0
    score2 = 0
    print(f"{team1.name} - {team2.name}")
    for count in range(6):
        res = pg(team1, team2)
        print(f'res: {res}')

        score1 += res[2]
        score2 += res[3]
        play = res[0]

        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event[0] == '-THREAD-':
            if event[1] == 'scoreboard':
                window['timer'].update(f'{count + 1}/6')
                window['score1'].update(score1)
                window['score2'].update(score2)
                row = count
                col = 2
                data = values['plays']
                # data[row][col] = res[0]
                # window['plays'].update(values=data)
    # Исходя из статусов игроков проставляем статистику
    for team in teams:
        for player in team.roster:
            if player.status in ['Lineup', 'Subs on', 'Subs off']:
                player.stats['games'] += 1

    print(f"Full time!\n{score1} - {score2}")
    window.close()
    game.calc_stats(team1, team2, score1, score2)
    game_info[3] = score1
    game_info[4] = score2
    game_info[5] = 'Finished'

    while True:
        event, values = window.read()
        sg.popup('Game is finished!',
                 f'{team1.name} {score1}:{score2} {team2.name}', title='MODAL')
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()

# main(team1, team2)
