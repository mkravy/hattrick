import draft
from game import Game


class Tournament:
    def __init__(self, name, tournament_type, teams):
        self.name = name
        self.type = tournament_type
        self.teams = teams
        self.schedule = []
        draft.draft(teams)
        self.generate_schedule()
        self.show_schedule()
        self.get_games_by_schedule()

    def generate_schedule(self):
        teams = self.teams
        n = len(teams)
        if n % 2 == 1:
            teams.append(None)  # Добавляем пустую команду для нечетного числа команд

        for round in range(n - 1):
            round_matches = []
            for i in range(n // 2):
                home = teams[i]
                away = teams[n - 1 - i]
                if round % 2 == 0:
                    round_matches.append((home, away))  # Чередуем
                else:
                    round_matches.append((away, home))

            self.schedule.append(round_matches)

            # Сдвиг команд для следующего тура
            teams = [teams[0]] + [teams[-1]] + teams[1:-1]

    def show_schedule(self):
        for tour in self.schedule:
            for game in tour:
                print(f"{game[0].name} - {game[1].name}")

    def get_games_by_schedule(self):
        for tour in self.schedule:
            for match in tour:
                team1 = match[0]
                team2 = match[1]
                game = Game(team1, team2)

    def calc_points(self, team):
        t = team.table_stat
        self.points = self.win * 3 + self.draw
        t['points'] = t['win'] * 3 + t['draw']

    def calc_stats(self, team1, team2, score1, score2):
        """TO DO"""
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
