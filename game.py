import config
import draft


class Game:
    def __init__(self, team1, team2):
        self.home = team1
        self.away = team2
        self.draft_roster = draft.get_players()
        self.pregame()

    def pregame(self):
        # Загружаем список тактик
        config.upload_tactics()

        team1 = self.home
        print(f"{team1.name}'s roster:")
        team1.show_roster()
        team1.calc_tactic()
        team1.choose_tactic()
        team1.show_lineup()
        team1.show_bench()

        team2 = self.away
        print(f"{team2.name}'s roster:")
        team2.show_roster()
        team2.calc_tactic()
        team2.choose_tactic()
        team2.show_lineup()
        team2.show_bench()