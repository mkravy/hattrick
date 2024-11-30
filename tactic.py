class Tactic:
    def __init__(self, tactic, roster):
        self.name = tactic["name"]
        self.position_count = {'gk': tactic["gk"], 'df': tactic["df"], 'mf': tactic["mf"], 'fw': tactic["fw"]}
        self.skills = {'gk': 0, 'df': 0, 'mf': 0, 'fw': 0}
        self.total_skills = 0
        self.position = ['gk', 'df', 'mf', 'fw']
        self.roster = roster
        self.lineup = []
        self.bench = []
        self.set_lineup()

    def get_info(self):
        print(f"{self.name} | {self.total_skills} | {self.skills}")

    def set_lineup(self):
        for position in self.position:
            list = []
            count = self.position_count[position]

            # Перебираем состав в поиске нужной позиции
            for player in self.roster:
                if player.position == position:
                    list.append(player)

            # Сортируем в порядке убывания
            list = sorted(list, key=lambda player: player.skill, reverse=True)

            # Распределяем на основу и запас
            for player in list:
                index = list.index(player)
                if index < count:
                    self.lineup.append(player)
                else:
                    self.bench.append(player)
        if len(self.lineup) == 11:
            # Считаем скиллы
            self.get_skills()

    def get_skills(self):
        for player in self.lineup:
            self.skills[player.position] += player.skill
        for position in self.skills.values():
            self.total_skills += position