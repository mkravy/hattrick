import config
import db_test
import draft
import team
from game import Game
from player import Player
from team import Team
import random as rnd

team1 = Team('Home')
team2 = Team('Away')
draft.draft(team1, team2)
game = Game(team1, team2)