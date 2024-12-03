'''
CREATE TABLE players (
	ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	USERNAME TEXT NOT NULL,
	"LEVEL" INTEGER DEFAULT (0) NOT NULL,
	AVG_RANKING REAL DEFAULT (0) NOT NULL,
	TOTAL_GAMES INTEGER DEFAULT (0) NOT NULL,
	RANKINGS BLOB,
	RATE REAL DEFAULT (1500.00) NOT NULL,
	GAMES_CRR_RANKING INTEGER DEFAULT (0) NOT NULL,
	AVG_POINTS INTEGER DEFAULT (0) NOT NULL,   
    HIGH_POINTS INTEGER DEFAULT (0));
'''

import sqlite3

def add_player(username, discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"INSERT INTO players (USERNAME, DISCORD_ID) VALUES ('{username}', '{discord_id}')")

    conn.commit()
    conn.close()

def get_player_level(username):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE USERNAME = '{username}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][2]

def get_player_avg_rankings(username):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE USERNAME = '{username}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][3]

def get_player_total_games(username):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE USERNAME = '{username}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][4]

def get_player_rate(username):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE USERNAME = '{username}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][6]

def get_player_current_games_number(username):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE USERNAME = '{username}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][7]

def get_player_avg_points(username):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE USERNAME = '{username}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][8]

def get_player_high_points(username):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE USERNAME = '{username}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][9]

if __name__ == '__main__':
    # add_player('test')
    pass