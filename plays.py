import random as r
from config import plays


def plays_generator(team1, team2):
    """Определяем и разыгрываем событие"""
    """TODO Замены"""
    play = r.choice(plays)
    res = ''
    if play == 'total':
        res = play_versus(play, team1, team2, team1.total_skills, team2.total_skills)
    if play == 'attack':
        res = play_versus(play, team1, team2, team1.skills['fw'], team2.skills['fw'])
    if play == 'defence':
        res = play_versus(play, team1, team2, team1.skills['df'], team2.skills['df'])
    if play == 'midfield':
        res = play_versus(play, team1, team2, team1.skills['mf'], team2.skills['mf'])
    if play == 'def vs att':
        res = play_versus(play, team1, team2, team1.skills['df'], team2.skills['fw'])
    if play == 'att vs def':
        res = play_versus(play, team1, team2, team1.skills['fw'], team2.skills['df'])
    if play == 'home penalty':
        res = play_penalty(play, team1, team2)
    if play == 'away penalty':
        res = play_penalty(play, team2, team1)
    if play == 'home rc':
        res = red_card(play, team1)
    if play == 'away rc':
        res = red_card(play, team2)
    return res


def play_versus(play, team1, team2, point1, point2):
    """Сравниваем значения, которые пихаем исходя из ситуации"""
    score = [play, '', 0, 0]
    if point1 > point2:
        score = [play, team1.name, 1, 0]
    if point1 < point2:
        score = [play, team2.name, 0, 1]
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
    if play == 'away penalty':
        kick = choose_penalty_kicker(team2)
        gk = get_penalty_keeper(team1)
        team = team2.name
    if kick.skill > gk.skill:
        score = [play, team, 1, 0]
    else:
        score = [play, team, 0, 0]
    return score


def red_card(team, play):
    """Определяем удаляемого игрока и пересчитываем инфу о команде"""
    player = r.choice(team.lineup)
    team.lineup.remove(player)
    team.tactic.get_skills() # Пересчитываем стату
    team.calc_after_tactic()
    score = [play, team.name, 0, 0]
    return score
