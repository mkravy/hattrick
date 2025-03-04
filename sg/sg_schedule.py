import PySimpleGUI as sg
from plays import plays_generator as pg


def main(schedule):
    table_tournament = [[sg.Table(
        [[schedule[i][0], schedule[i][1].name, schedule[i][2].name, schedule[i][3], schedule[i][4], schedule[i][5]] for t in
         range(6) for i in range(12)],
        headings=['#', 'Home Team', 'Away Team', 'Score1', 'Score2', 'Status'], key='table', justification='center',
        num_rows=12,
        hide_vertical_scroll=False, auto_size_columns=False, col_widths=[4, 15, 10, 10])]]
    ### LAYOUTS ###
    layout_lineup = [[sg.Frame('', table_tournament)]]
    window = sg.Window('Tournament schedule', layout_lineup, finalize=True, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()
