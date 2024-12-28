class Table:
    def __init__(self, teams):
        self.teams = teams

    def calc_points(self):
        self.points = self.win * 3 + self.draw

    def calc_stats(self, score1, score2):
        if score1 > score2:
            self.win += 1
        elif score1 == score2:
            self.draw += 1
        elif score1 < score2:
            self.lose += 1
        self.gf += score1
        self.ga += score2
        self.dif = self.gf - self.ga
        self.calc_points()

    def show_info(self):
        print(f"{self.name}'s Skill: {self.skill}\nStats:\n +{self.win} ={self.draw} -{self.lose} {self.points} points ({self.gf} - {self.ga})\n")

    # teams = sorted(teams, key=lambda t: (-t.points, -t.dif))
    #
    # for team in teams:
    #     team.show_info()