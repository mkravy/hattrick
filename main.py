import config
import db_test
import draft
import team
from game import Game
from player import Player
from team import Team
import random as rnd
from tournament import Tournament

blue = Team('blue')
green = Team('green')
red = Team('red')
yellow = Team('yellow')

# game = Game(team1, team2)
teams = [blue, green, red, yellow]
# draft.draft(teams)
league = Tournament('Test League', 'league', teams)

teams = sorted(teams, key=lambda t: (-t.table_stat['points']))

for team in teams:
    team.show_table_info()

