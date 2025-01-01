from team import Team
from tournament import Tournament

# TODO
# Создаем команды (пока так)
blue = Team('blue')
green = Team('green')
red = Team('red')
yellow = Team('yellow')

teams = [blue, green, red, yellow]

# Инициализируем турнир и заодно проводим
league = Tournament('Test League', 'league', teams, 2)

# Выводим таблицу
teams = sorted(teams, key=lambda t: (-t.table_stat['points']))

for team in teams:
    team.show_table_info()

