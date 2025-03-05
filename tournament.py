import draft
from sg import sg_game


class Tournament:
    def __init__(self, name, tournament_type, teams, round):
        """Проводим драфт на все команды турнира, генерируем расписание, TODO: исходя из типа турнира"""
        self.name = name
        self.type = tournament_type
        self.teams = teams
        self.round = round  # Количество кругов (для кругового турнира)
        self.schedule = []
        draft.draft(teams)
        self.generate_schedule()

    def generate_schedule(self):
        """Генерируем расписание"""
        teams = self.teams
        n = len(teams)
        game_id = 1
        if n % 2 == 1:
            teams.append(None)  # Добавляем пустую команду для нечетного числа команд

        # for round in range(n - 1):
        for round in range(self.round*(n-1)):
            round_matches = []
            for i in range(n // 2):
                home = teams[i]
                away = teams[n - 1 - i]
                if round % 2 == 0:
                    game = [game_id, home, away, 0, 0, 'Scheduled']
                    # round_matches.append(game_id, home, away, 0, 0, 'Schedule')  # Чередуем
                    # round_matches.append(game)
                    self.schedule.append(game)
                else:
                    game = [game_id, away, home, 0, 0, 'Scheduled']
                    # round_matches.append(game_id, away, home, 0, 0, 'Schedule')
                    # round_matches.append(game)
                    self.schedule.append(game)
                game_id += 1

            # self.schedule.append(round_matches)

            # Сдвиг команд для следующего тура
            teams = [teams[0]] + [teams[-1]] + teams[1:-1]

    # def show_schedule(self):
    #     """Показываем расписание - отказываемся"""
    #     for tour in self.schedule:
    #         for game in tour:
    #             # print(f"{game[1].name} - {game[2].name}")
    #             print(game)
    #
    # def play_game_by_schedule(self):
    #     """Играем следующий по очереди матч согласно расписанию"""
    #     """Не используется"""
    #     t = 0
    #     for tour in self.schedule:
    #         t += 1
    #         for match in tour:
    #             game_id = match[0]
    #             team1 = match[1]
    #             team2 = match[2]
    #             sg_game.main(game_id, t, team1, team2)
