import PySimpleGUI as sg
from plays import plays_generator as pg


def main(teams):
    team = teams[0]
    option_teams = []

    for team in teams:
        option_teams.append(team.name)

    team_data = [
        [p.name, p.position, p.skill, p.country, p.stats['games'], p.stats['goals'], p.stats['yc'], p.stats['rc']] for p
        in team.roster]
    headings = ['Player', 'Position', 'Skill', 'Country', 'Games', 'Goals', 'YC', 'RC']
    team_roster = [[sg.Table(values=team_data, headings=headings, key='roster', justification='center', num_rows=14,
                             hide_vertical_scroll=False, auto_size_columns=False, col_widths=[12, 7, 5, 15])]]

    ### LAYOUTS ###
    layout_roster = [[sg.OptionMenu(option_teams, default_value=f'{option_teams[0]}', key='option_team', enable_events=True)], [sg.Frame('', team_roster)]]
    window = sg.Window(f'{team.name} roster', layout_roster, finalize=True, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'option_team':
            for t in teams:
                if t.name == values['option_team']:
                    team = t
            team_data_new = [
                [p.name, p.position, p.skill, p.country, p.stats['games'], p.stats['goals'], p.stats['yc'],
                 p.stats['rc']] for p in team.roster]
            team.show_roster()
            window['roster'].update(values=team_data_new)

    window.close()
