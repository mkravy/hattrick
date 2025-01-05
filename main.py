import draft
from game import Game
from team import Team
from tournament import Tournament

# # TODO
# # Создаем команды (пока так)
# blue = Team('blue')
# green = Team('green')
# red = Team('red')
# yellow = Team('yellow')
#
# teams = [blue, green, red, yellow]
#
# # Инициализируем турнир и заодно проводим
# league = Tournament('Test League', 'league', teams, 2)
#
# # Выводим таблицу
# teams = sorted(teams, key=lambda t: (-t.table_stat['points']))
#
# for team in teams:
#     team.show_table_info()

team1 = Team('Home')
team2 = Team('Away')
teams = [team1, team2]
draft.draft(teams)
game = Game(team1, team2)