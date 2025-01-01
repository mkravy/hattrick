import config
from plays import plays_generator as pg


class Game:
    def __init__(self, team1, team2):
        self.home = team1
        self.away = team2
        self.pregame()
        self.game()

    def pregame(self):
        """Подготовительные моменты к игре"""
        team1 = self.home
        team2 = self.away

        # Загружаем список тактик, выбираем лучшую, готовим составы
        config.upload_tactics()
        team1.pregame_init()
        team2.pregame_init()

    def game(self):
        """Процесс матча"""
        score1 = 0
        score2 = 0
        print(f"{self.home.name} - {self.away.name}")
        for i in range(6):
            # print(f"Play #{i+1}:")
            res = pg(self.home, self.away)
            score1 += res[0]
            score2 += res[1]
            # print("\n")
        print(f"Full time!\n{score1} - {score2}")
        self.calc_stats(self.home, self.away, score1, score2)

    def calc_stats(self, team1, team2, score1, score2):
        """Считаем статистику в турнирную таблицу после матча"""
        t1 = team1.table_stat
        t2 = team2.table_stat
        if score1 > score2:
            t1['win'] += 1
            t2['lose'] += 1
        elif score1 == score2:
            t1['draw'] += 1
            t2['draw'] += 1
        elif score1 < score2:
            t1['lose'] += 1
            t2['win'] += 1
        t1['gf'] += score1
        t2['gf'] += score2
        t1['ga'] += score2
        t2['ga'] += score1
        t1['points'] = t1['win'] * 3 + t1['draw']
        t2['points'] = t2['win'] * 3 + t2['draw']