import random as r
from config import plays


def plays_generator(team1, team2):
    """Определяем и разыгрываем событие"""
    """TODO Замены"""
    play = r.choice(plays)
    res = ''
    if play == 'total':
        res = play_versus(play, team1, team2, team1.total_skills, team2.total_skills, ['gk', 'df', 'mf', 'fw'])
    if play == 'attack':
        res = play_versus(play, team1, team2, team1.skills['fw'], team2.skills['fw'], ['fw'])
    if play == 'defence':
        res = play_versus(play, team1, team2, team1.skills['df'], team2.skills['df'], ['df'])
    if play == 'midfield':
        res = play_versus(play, team1, team2, team1.skills['mf'], team2.skills['mf'], ['mf'])
    if play == 'home att vs def':
        res = play_versus_home_att_vs_def(play, team1, team2, team1.skills['fw'], team2.skills['df'], ['fw'])
    if play == 'away att vs def':
        res = play_versus_away_att_vs_def(play, team2, team1, team1.skills['fw'], team2.skills['df'], ['fw'])
    if play == 'home penalty':
        res = play_penalty(play, team1, team2)
    if play == 'away penalty':
        res = play_penalty(play, team2, team1)
    if play == 'home rc':
        res = red_card(play, team1)
    if play == 'away rc':
        res = red_card(play, team2)
    return res


def play_versus(play, team1, team2, point1, point2, lines):
    """Сравниваем значения, которые пихаем исходя из ситуации"""
    score = [play, '', 0, 0]
    if point1 > point2:
        scorer = choose_scorer(lines, team1.lineup)
        score = [play, team1.name, 1, 0, scorer]
    if point1 < point2:
        scorer = choose_scorer(lines, team2.lineup)
        score = [play, team2.name, 0, 1, scorer]
    return score


def play_versus_home_att_vs_def(play, team1, team2, point1, point2, lines):
    """Чуть поменял оригинальную логику, так кажется более правильно"""
    score = [play, '', 0, 0]
    if point1 > point2:
        scorer = choose_scorer(lines, team1.lineup)
        score = [play, team1.name, 1, 0, scorer]
    return score


def play_versus_away_att_vs_def(play, team1, team2, point1, point2, lines):
    """Чуть поменял оригинальную логику, так кажется более правильно"""
    score = [play, '', 0, 0]
    if point1 > point2:
        scorer = choose_scorer(lines, team1.lineup)
        score = [play, team1.name, 0, 1, scorer]
    return score



def play_penalty(play, team1, team2):
    """Выбираем бьющих и пробиваем пенальти"""

    def choose_penalty_kicker(team):
        """Выбираем игрока, бьющего пенальти"""
        player = r.choice(team.lineup)
        # print(f"{player.name} ({player.skill})")
        return player

    def get_penalty_keeper(team):
        """Просто достаем вратаря из состава"""
        return team.lineup[0]

    score = [0, 0, 0, 0]
    if play == 'home penalty':
        kick = choose_penalty_kicker(team1)
        gk = get_penalty_keeper(team2)
        team = team1.name
        if kick.skill > gk.skill:
            score = [play, team, 1, 0, kick.name]
    if play == 'away penalty':
        kick = choose_penalty_kicker(team2)
        gk = get_penalty_keeper(team1)
        team = team2.name
        if kick.skill > gk.skill:
            score = [play, team, 0, 1, kick.name]
    else:
        score = [play, team, 0, 0, '']
    kick.stats['goals'] += 1
    return score


def red_card(team, play):
    """Определяем удаляемого игрока и пересчитываем инфу о команде"""
    player = r.choice(team.lineup)
    player.stats['rc'] += 1
    team.lineup.remove(player)
    team.tactic.get_skills() # Пересчитываем стату
    team.calc_after_tactic()
    score = [play, team.name, 0, 0, player.name]
    return score


def choose_scorer(lines, lineup):
    player = ''
    score = -1
    for p in lineup:
        if p.position in lines:
            i = p.skill * r.random()
            if i > score:
                player = p
    player.stats['goals'] += 1
    return player.name