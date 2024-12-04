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

def verify_player(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # print(result)

    if len(result) == 0:
        return False
    else:
        return True

def get_player_level(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][2]

def get_player_avg_rankings(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][3]

def get_player_total_games(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][4]

def get_player_rate(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][5]

def get_player_current_games_number(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][6]

def get_player_avg_points(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][7]

def get_player_high_points(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][8]

def get_player_ranking(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result[0][10]

def set_player_ranking(discord_id, ranking):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"UPDATE players SET RANK = '{ranking}' WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

def set_player_level(discord_id, level):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"UPDATE players SET LEVEL = {level} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

def set_player_avg_rankings(discord_id, avg_rankings):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"UPDATE players SET AVG_RANKING = {avg_rankings} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

def set_player_total_games(discord_id, total_games):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"UPDATE players SET TOTAL_GAMES = {total_games} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

def set_player_rate(discord_id, rate):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"UPDATE players SET RATE = {rate} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

def set_player_current_games_number(discord_id, games_number):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"UPDATE players SET GAMES_CRR = {games_number} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

def set_player_avg_points(discord_id, avg_points):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"UPDATE players SET AVG_POINTS = {avg_points} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

def set_player_high_points(discord_id, high_points):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    c.execute(f"UPDATE players SET HIGH_POINTS = {high_points} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    # add_player('test')
    get_player_level('harryjin4179')