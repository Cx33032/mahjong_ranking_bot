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

# Function to add a player to the database
def add_player(username, discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Insert the player's username and discord ID into the players table
    c.execute(f"INSERT INTO players (USERNAME, DISCORD_ID) VALUES ('{username}', '{discord_id}')")

    conn.commit()
    conn.close()

# Function to verify if a player exists in the database
def verify_player(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Select all players with the given discord ID
    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # print(result)

    # If no players are found, return False, otherwise return True
    if len(result) == 0:
        return False
    else:
        return True

# Function to get a player's level
def get_player_level(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Select all players with the given discord ID
    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # Return the player's level
    return result[0][2]

# Function to get a player's average rankings
def get_player_avg_rankings(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Select all players with the given discord ID
    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # Return the player's average rankings
    return result[0][3]

# Function to get a player's total games
def get_player_total_games(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Select all players with the given discord ID
    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # Return the player's total games
    return result[0][4]

# Function to get a player's rate
def get_player_rate(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Select all players with the given discord ID
    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # Return the player's rate
    return result[0][5]

# Function to get a player's current games number
def get_player_current_games_number(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Select all players with the given discord ID
    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # Return the player's current games number
    return result[0][6]

# Function to get a player's average points
def get_player_avg_points(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Select all players with the given discord ID
    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # Return the player's average points
    return result[0][7]

# Function to get a player's high points
def get_player_high_points(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Select all players with the given discord ID
    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # Return the player's high points
    return result[0][8]

# Function to get a player's ranking
def get_player_ranking(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Select all players with the given discord ID
    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # Return the player's ranking
    return result[0][10]

# Function to get a player's points
def get_player_points(discord_id):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Select all players with the given discord ID
    c.execute(f"SELECT * FROM players WHERE DISCORD_ID = '{discord_id}'")

    result = c.fetchall()

    conn.commit()
    conn.close()

    # Return the player's points
    return result[0][11]

# Function to set a player's points
def set_player_points(discord_id, point):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Update the player's points in the players table
    c.execute(f"UPDATE players SET POINT = '{point}' WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

# Function to set a player's ranking
def set_player_ranking(discord_id, ranking):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Update the player's ranking in the players table
    c.execute(f"UPDATE players SET RANK = '{ranking}' WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

# Function to set a player's level
def set_player_level(discord_id, level):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Update the player's level in the players table
    c.execute(f"UPDATE players SET LEVEL = {level} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

# Function to set a player's average rankings
def set_player_avg_rankings(discord_id, avg_rankings):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Update the player's average rankings in the players table
    c.execute(f"UPDATE players SET AVG_RANKING = {avg_rankings} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

# Function to set a player's total games
def set_player_total_games(discord_id, total_games):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Update the player's total games in the players table
    c.execute(f"UPDATE players SET TOTAL_GAMES = {total_games} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

# Function to set a player's rate
def set_player_rate(discord_id, rate):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Update the player's rate in the players table
    c.execute(f"UPDATE players SET RATE = {rate} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

# Function to set a player's current games number
def set_player_current_games_number(discord_id, games_number):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Update the player's current games number in the players table
    c.execute(f"UPDATE players SET GAMES_CRR = {games_number} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

# Function to set a player's average points
def set_player_avg_points(discord_id, avg_points):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Update the player's average points in the players table
    c.execute(f"UPDATE players SET AVG_POINTS = {avg_points} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()

# Function to set a player's high points
def set_player_high_points(discord_id, high_points):
    conn = sqlite3.connect('testDB.db')
    c = conn.cursor()

    # Update the player's high points in the players table
    c.execute(f"UPDATE players SET HIGH_POINTS = {high_points} WHERE DISCORD_ID = '{discord_id}'")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    # add_player('test')
    get_player_level('harryjin4179')