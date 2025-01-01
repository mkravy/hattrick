import config
import db_test
import random as r


def draft(teams):
    """Процедура драфта игроков по командам"""
    draft_players = db_test.db_test()
    for skill in range(5, 0, -1):
        limit = config.draft_count[skill]
        for i in range(limit):
            for team in teams:
                positions = get_position_list(team)
                filtered_list = filter_by_skill(draft_players, skill, positions)
                player = r.choice(filtered_list)
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

