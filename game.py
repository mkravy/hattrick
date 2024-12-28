import config
import draft
from plays import plays_generator as pg


class Game:
    def __init__(self, team1, team2):
        self.home = team1
        self.away = team2
        self.draft_roster = draft.get_players()
        # self.draft_roster = draft.draft(team1, team2)
        self.pregame()
        self.game()

    def pregame(self):
        # Загружаем список тактик
        config.upload_tactics()

        team1 = self.home
        team1.pregame_init()
        team1.show_skills()
        # team1.pregame_info()

        team2 = self.away
        team2.pregame_init()
        team2.show_skills()
        # team2.pregame_info()

    def game(self):
        score1 = 0
        score2 = 0
        for i in range(6):
            print(f"Play #{i+1}:")
            res = pg(self.home, self.away)
            score1 += res[0]
            score2 += res[1]
            print("\n")
        print(f"Full time!\n{score1} - {score2}")