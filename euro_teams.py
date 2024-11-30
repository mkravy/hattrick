euro_teams = []


class EuroTeam:
    def __init__(self, name, tactic, total, players):
        self.name = name
        self.tactic = tactic
        self.total = total
        self.players = players


euro_teams.append(EuroTeam('Athens', '433', 36, [[2], [5, 4, 3, 3], [1, 5, 2], [4, 3, 4]]))
euro_teams.append(EuroTeam('Barcelona', '343', 37, [[4], [4, 2, 1], [3, 5, 3, 3], [5, 4, 3]]))
euro_teams.append(EuroTeam('Bremen', '343', 34, [[3], [2, 2, 2], [5, 1, 1, 5], [5, 3, 5]]))
euro_teams.append(EuroTeam('Eindhoven', '442', 40, [[4], [5, 3, 3, 3], [5, 3, 3, 3], [4, 4]]))
