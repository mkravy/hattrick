import PySimpleGUI as sg
import draft
from game import Game
from team import Team


def main():
    team1 = Team('Blue')
    team2 = Team('Green')
    teams = [team1, team2]
    draft.draft(teams)
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
    frame_scoreboard_home = [[sg.Text(team1.name, key='team1')], [sg.Push(), sg.Text(game.score1, font=('Comic Sans', 20,), justification='center', key='score1'), sg.Push()]]
    frame_scoreboard_away = [[sg.Text(team2.name, key='team2')], [sg.Push(), sg.Text(game.score2, font=('Comic Sans', 20,), justification='center', key='score2'), sg.Push()]]
    frame_scoreboard_timer = [[sg.Text(f'{game.count}/6', key='timer')]]

    table_plays = [[sg.Table([[i+1, 'Total', team1.name] for i in range(6)],
                             headings=['#', 'Plays', 'Team'], justification='center', num_rows=6,
                                  hide_vertical_scroll=True, auto_size_columns=False, col_widths=[4, 10, 10])]]

    frame_scoreboard = [[sg.Frame('', frame_scoreboard_home), sg.Frame('', frame_scoreboard_timer), sg.Frame('', frame_scoreboard_away)],
                        [table_plays]]

    frame_total = [[sg.Frame(team1.name, table_lineup_home, element_justification='center', pad=(5, 5)),
                      sg.Frame(team2.name, table_lineup_away, element_justification='center', pad=(5, 3)),
                      sg.Frame('', frame_scoreboard, element_justification='center', pad=(5, 5))],
                      [sg.Frame('Bench', table_bench_home, element_justification='center', pad=(5, 0)),
                      sg.Frame('Bench', table_bench_away, element_justification='center', pad=(5, 0)), sg.Sizegrip()]]
    ### LAYOUTS ###
    layout_lineup = [[sg.Push(), sg.Frame('', frame_total), sg.Push()]]

    window = sg.Window('Test', layout_lineup, finalize=True, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()

main()