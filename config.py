# tactics = ['5-3-2', '4-4-2', '4-3-3', '3-4-3', '3-5-2']
from tactic import Tactic

tactics = []
draft_count = {5: 1, 4: 2, 3: 3, 2: 4, 1: 4}
max_count_position = {'gk': 1, 'df': 5, 'mf': 5, 'fw': 3}
positions = ['gk', 'df', 'mf', 'fw']


def upload_tactics():
    tactics.append({'name': '532', 'gk': 1, 'df': 5, 'mf': 3, 'fw': 2})
    tactics.append({'name': '442', 'gk': 1, 'df': 4, 'mf': 4, 'fw': 2})
    tactics.append({'name': '433', 'gk': 1, 'df': 4, 'mf': 3, 'fw': 3})
    tactics.append({'name': '343', 'gk': 1, 'df': 3, 'mf': 4, 'fw': 3})
    tactics.append({'name': '352', 'gk': 1, 'df': 3, 'mf': 5, 'fw': 2})