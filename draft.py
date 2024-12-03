import config
import db_test
from player import Player
import random as rnd


def get_players():
    draft = [Player('Sylvain', 'mf', 5, 'France'), Player('Bjorn', 'gk', 5, 'Sweden'), Player('Pipo', 'fw', 5, 'Italy'),
             Player('Andreas', 'df', 5, 'Germany'), Player('Jesus', 'df', 4, 'Spain'),
             Player('Jan', 'df', 4, 'Germany'), Player('Jurgen', 'df', 4, 'Germany'),
             Player('Diego', 'fw', 4, 'Argentina'), Player('Chris', 'df', 4, 'England'),
             Player('Kike', 'mf', 4, 'Spain'), Player('Mika', 'mf', 3, 'Finland'), Player('Claus', 'mf', 3, 'Swiss'),
             Player('Henny', 'fw', 3, 'Young'), Player('Theo', 'fw', 3, 'Young'),
             Player('Hans-Christian', 'df', 3, 'Denmark'), Player('Karel', 'df', 3, 'Czech'),
             Player('Jari', 'fw', 3, 'Finland'), Player('Bob', 'mf', 3, 'Belgium'), Player('Yannis', 'gk', 2, 'None'),
             Player('Wang', 'df', 2, 'None'), Player('Derek', 'mf', 2, 'None'), Player('Nestor', 'mf', 2, 'None'),
             Player('Josue', 'fw', 2, 'None'), Player('Hatsodoku', 'gk', 2, 'None'), Player('Jason', 'mf', 2, 'None'),
             Player('Andrew', 'df', 2, 'None'), Player('Martijn', 'df', 2, 'None'), Player('Marcel', 'fw', 2, 'None'),
             Player('Baltazaras', 'mf', 1, 'None'), Player('Coach', 'df', 1, 'None'), Player('Ludwig', 'df', 1, 'None'),
             Player('Isah', 'df', 1, 'None'), Player('Rene', 'fw', 1, 'None'), Player('Johan', 'df', 1, 'None'),
             Player('Bartek', 'df', 1, 'None'), Player('Nolberto', 'fw', 1, 'None'), Player('Stanko', 'mf', 1, 'None'),
             Player('Daniel', 'fw', 1, 'None')]

    return draft


def draft(team1, team2):
    """Процедура драфта игроков по командам"""
    # draft_players = get_players()
    draft_players = db_test.db_test()
    teams = [team1, team2]
    # teams = [team1]
    for skill in range(5, 0, -1):
        limit = config.draft_count[skill]
        for i in range(limit):
            for team in teams:
                team.show_roster()
                team.show_position_info()
                positions = get_position_list(team)
                filtered_list = filter_by_skill(draft_players, skill, positions)
                player = rnd.choice(filtered_list)
                draft_players.remove(player)
                team.roster.append(player)


def filter_by_skill(draft_players, skill, positions):
    """Получаем список игроков с заданным скиллом и позициями"""
    list = []
    for player in draft_players:
        if player.skill == skill and player.position in positions:
            list.append(player)
    return list


def get_position_list(team):
    """Собираем доступные для выбора в команду позиции"""
    # positions = config.positions
    positions = ['gk', 'df', 'mf', 'fw']
    list = {'gk': 0, 'df': 0,  'mf': 0, 'fw': 0}
    max_count = config.max_count_position
    for player in team.roster:
        list[player.position] += 1
    for key, value in list.items():
        if list[key] >= max_count[key] and key in positions:
            positions.remove(key)
    return positions

