import PySimpleGUI as sg
from plays import plays_generator as pg


def main(teams):
    team = teams[0]
    order_pos = {'gk': 0, 'df': 1, 'mf': 2, 'fw': 3}
    team.roster = sorted(team.roster, key=lambda x: (order_pos[x.position], -x.skill))

    team_roster = [[sg.Table(
        [[p.name, p.position, p.skill, p.country] for p in team.roster],
        headings=['Player', 'Position', 'Skill', 'Country'], key='roster', justification='center',
        num_rows=14,
        hide_vertical_scroll=False, auto_size_columns=False, col_widths=[12, 7, 5, 15])]]
    ### LAYOUTS ###
    layout_roster = [[sg.Frame('', team_roster)]]
    window = sg.Window(f'{team.name} roster', layout_roster, finalize=True, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()
