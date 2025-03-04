tactics = []
draft_count = {5: 1, 4: 2, 3: 3, 2: 4, 1: 4}
max_count_position = {'gk': 1, 'df': 5, 'mf': 5, 'fw': 3}
positions = ['gk', 'df', 'mf', 'fw']

# TODO
# Доделать все события в матче
# plays = ['total', 'attack', 'midfield', 'defence', 'home penalty', 'away penalty', 'home rc', 'away rc', 'home injury', 'away injury', 'def vs att', 'att vs def']
# plays = ['total', 'attack', 'midfield', 'defence', 'home penalty', 'away penalty', 'home rc', 'away rc', 'def vs att', 'att vs def']
plays = ['total', 'attack', 'midfield', 'defence', 'home penalty', 'away penalty', 'def vs att', 'att vs def']
tournament_types = ['league']


def upload_tactics():
    tactics.append({'name': '532', 'gk': 1, 'df': 5, 'mf': 3, 'fw': 2})
    tactics.append({'name': '442', 'gk': 1, 'df': 4, 'mf': 4, 'fw': 2})
    tactics.append({'name': '433', 'gk': 1, 'df': 4, 'mf': 3, 'fw': 3})
    tactics.append({'name': '343', 'gk': 1, 'df': 3, 'mf': 4, 'fw': 3})
    tactics.append({'name': '352', 'gk': 1, 'df': 3, 'mf': 5, 'fw': 2})