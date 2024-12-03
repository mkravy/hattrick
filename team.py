import config
from player import Player
from tactic import Tactic


class Team:
    def __init__(self, name):
        self.name = name
        self.skills = {'gk': 0, 'df': 0, 'mf': 0, 'fw': 0}
        self.total_skills = 0
        self.roster = []
        self.lineup = []
        self.bench = []
        self.scheme = ''
        self.tactic_list = []

    def calc_tactic(self):
        for tactic in config.tactics:
            t = Tactic(tactic, self.roster)
            self.tactic_list.append(t)

    def choose_tactic(self):
        list = []
        for t in self.tactic_list:
            list.append(t)
        list = sorted(list, key=lambda t: t.total_skills, reverse=True)
        for l in list:
            print(l.get_info())
        tactic = list[0]
        self.lineup = tactic.lineup
        self.bench = tactic.bench
        self.skills = tactic.skills
        self.total_skills = tactic.total_skills
        self.scheme = tactic.name

    def show_roster(self):
        for player in self.roster:
            player.show_info()

    def show_lineup(self):
        self.show_skills()
        print(self.scheme)
        print(f"==={self.name}===\nStarting lineup:")
        for player in self.lineup:
            player.show_info()

    def show_bench(self):
        print(f"Bench:")
        for player in self.bench:
            player.show_info()

    def show_skills(self):
        list = []
        for position in self.skills.values():
            list.append(position)
        list.append(self.total_skills)
        print(f"{list[0]} | {list[1]} | {list[2]} | {list[3]} | {list[4]}")

    def show_position_info(self):
        list = {'gk': 0, 'df': 0, 'mf': 0, 'fw': 0}
        for player in self.roster:
            list[player.position] += 1
        print(list)