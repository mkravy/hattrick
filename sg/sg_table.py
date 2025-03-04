import PySimpleGUI as sg
from plays import plays_generator as pg

def main(teams):
    table_tournament = [[sg.Table([[i + 1, teams[i].name, teams[i].table_stat['games'], teams[i].table_stat['points'], teams[i].table_stat['gd']] for i in range(4)],
                             headings=['#', 'Team', 'Games', 'Points', 'GD'], key='table', justification='center', num_rows=4,
                             hide_vertical_scroll=True, auto_size_columns=False, col_widths=[4, 15, 10, 10])]]
    ### LAYOUTS ###
    layout_lineup = [[sg.Frame('', table_tournament)]]
    window = sg.Window('Tournament table', layout_lineup, finalize=True, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()