import random as r
from config import plays


def plays_generator(team1, team2):
    """Определяем и разыгрываем событие"""
    play = r.choice(plays)
    print(f"play: {play}")
    res = ''
    if play == 'total':
        res = play_versus(play, team1.total_skills, team2.total_skills)
    if play == 'attack':
        res = play_versus(play, team1.skills['fw'], team2.skills['fw'])
    if play == 'defence':
        res = play_versus(play, team1.skills['df'], team2.skills['df'])
    if play == 'midfield':
        res = play_versus(play, team1.skills['mf'], team2.skills['mf'])
    if play == 'def vs att':
        res = play_versus(play, team1.skills['df'], team2.skills['fw'])
    if play == 'att vs def':
        res = play_versus(play, team1.skills['fw'], team2.skills['df'])
    if play == 'home penalty':
        res = play_penalty(play, team1, team2)
    if play == 'away penalty':
        res = play_penalty(play, team2, team1)
    if play == 'home rc':
        res = red_card(team1)
    if play == 'away rc':
        res = red_card(team2)
    print(f"res: {res}")
    return res


def play_versus(play, point1, point2):
    """Сравниваем значения, которые пихаем исходя из ситуации"""
    print(f"play_{play}")
    score = [0, 0]
    print(f"total: {point1} - {point2}")
    if point1 > point2:
        score = [1, 0]
    if point1 < point2:
        score = [0, 1]
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

    score = [0, 0]
    if play == 'home penalty':
        kick = choose_penalty_kicker(team1)
        gk = get_penalty_keeper(team2)
    if play == 'away penalty':
        kick = choose_penalty_kicker(team2)
        gk = get_penalty_keeper(team1)
    print(f"Kicker: {kick.name}({kick.skill})\nKeeper: {gk.name}({gk.skill})")
    if kick.skill > gk.skill:
        score = [1, 0]
    return score


def red_card(team):
    """Определяем удаляемого игрока и пересчитываем инфу о команде"""
    team.show_skills()
    player = r.choice(team.lineup)
    print(f"Player {player.name} ({player.skill}) was sent off!")
    team.lineup.remove(player)
    team.tactic.get_skills() # Пересчитываем стату
    team.calc_after_tactic()
    team.show_skills()
    score = [0, 0]
    return score
