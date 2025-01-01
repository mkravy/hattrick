import config
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
        self.tactic = ''
        self.table_stat = {'games': 0, 'win': 0, 'draw': 0, 'lose': 0, 'gf': 0, 'ga': 0, 'points': 0}

    def calc_tactic(self):
        """Добавляем все тактики в список и обсчитываем"""
        for tactic in config.tactics:
            t = Tactic(tactic, self.roster)
            self.tactic_list.append(t)

    def choose_tactic(self):
        """Выбираем самую подходящую и ставим ее для команды"""
        list = []
        for t in self.tactic_list:
            list.append(t)
        list = sorted(list, key=lambda t: t.total_skills, reverse=True)
        self.tactic = list[0]
        self.calc_after_tactic()

    def calc_after_tactic(self):
        """Определяем и пересчитываем все, что нужно после определения тактики"""
        self.lineup = self.tactic.lineup
        self.bench = self.tactic.bench
        self.skills = self.tactic.skills
        self.total_skills = self.tactic.total_skills
        self.scheme = self.tactic.name

    def show_roster(self):
        """Демонстрируем ростер"""
        for player in self.roster:
            player.show_info()

    def show_lineup(self):
        """Демонстрируем стартоавый состав"""
        self.show_skills()
        print(self.scheme)
        print(f"==={self.name}===\nStarting lineup:")
        for player in self.lineup:
            player.show_info()

    def show_bench(self):
        """Демонстрируем скамейку запасных"""
        print(f"Bench:")
        for player in self.bench:
            player.show_info()

    def show_skills(self):
        """Демонстрируем скиллы стартового состава команды"""
        list = []
        for position in self.skills.values():
            list.append(position)
        list.append(self.total_skills)
        print(f"{list[0]} | {list[1]} | {list[2]} | {list[3]} | {list[4]}")

    def show_position_info(self):
        """Демонстрируем инфо по позициям на драфте"""
        list = {'gk': 0, 'df': 0, 'mf': 0, 'fw': 0}
        for player in self.roster:
            list[player.position] += 1
        print(list)

    def pregame_init(self):
        """Прдематчевая подготовка - обсчет тактик и выбор лучшей"""
        self.calc_tactic()
        self.choose_tactic()

    def pregame_info(self):
        """Демонстрируем всю предматчевую инфу через один вызов"""
        self.show_roster()
        self.show_lineup()
        self.show_bench()
        self.show_skills()

    def show_table_info(self):
        """Демонстрируем инфу для турнирной таблицы"""
        print(f"{self.name}\nStats:\n +{self.table_stat['win']} ={self.table_stat['draw']} -{self.table_stat['lose']} {self.table_stat['points']} points ({self.table_stat['gf']} - {self.table_stat['ga']})\n")