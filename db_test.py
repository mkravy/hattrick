import sqlite3

from player import Player


def db_test():
    draft = []
    db_path = r"C:\Users\micha\DataGripProjects\test\test.sqlite"

    # создаем подключение
    con = sqlite3.connect(db_path, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True,
                          factory=sqlite3.Connection, cached_statements=128, uri=False)

    # получаем курсор
    cursor = con.cursor()

    cursor.execute("SELECT * FROM players_test")
    for player in cursor.fetchall():
        draft.append(Player(player[1], player[3], player[4], player[2]))
    return draft