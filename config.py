tactics = []
draft_count = {5: 1, 4: 2, 3: 3, 2: 4, 1: 4}
max_count_position = {'gk': 1, 'df': 5, 'mf': 5, 'fw': 3}
positions = ['gk', 'df', 'mf', 'fw']
# plays = {1: 'total', 2: 'attack', 3: 'midfield', 4: 'defence', 5: 'home penalty', 6: 'away penalty', 7: 'home rc', 8: 'away rc', 9: 'home injury', 10: 'away injury', 11: 'def vs att', 12: 'att vs def'}
# plays = ['total', 'attack', 'midfield', 'defence', 'home penalty', 'away penalty', 'home rc', 'away rc', 'home injury', 'away injury', 'def vs att', 'att vs def']
plays = ['total', 'attack', 'midfield', 'defence', 'home penalty', 'away penalty', 'home rc', 'away rc', 'def vs att', 'att vs def']

def upload_tactics():
    tactics.append({'name': '532', 'gk': 1, 'df': 5, 'mf': 3, 'fw': 2})
    tactics.append({'name': '442', 'gk': 1, 'df': 4, 'mf': 4, 'fw': 2})
    tactics.append({'name': '433', 'gk': 1, 'df': 4, 'mf': 3, 'fw': 3})
    tactics.append({'name': '343', 'gk': 1, 'df': 3, 'mf': 4, 'fw': 3})
    tactics.append({'name': '352', 'gk': 1, 'df': 3, 'mf': 5, 'fw': 2})