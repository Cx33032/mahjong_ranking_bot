from database import *
from ranking import *
from constants import *
from typing import List
import json

def assign_rate(players: List[Ranking]):
    avg_rate = 0.0
    for player in players:
        avg_rate += player.get_rate()
    avg_rate /= len(players)

    for player in players:
        correction_val = (((avg_rate)if avg_rate > 1500 else 1500) - player.get_rate()) / 40
        delta_rate = ((1 - player.get_total_games() * 0.002) * (RATE_ORIGINAL[player.get_rank() - 1] + correction_val)) if player.get_total_games() < 400 else (0.2 * (RATE_ORIGINAL[player.get_rank() - 1] + correction_val))

        player.set_rate(player.get_rate() + delta_rate) 

def calculate_avg_points(player: Ranking):
    new_avg_points = (int)((player.get_avg_points() * player.get_total_games() + player.get_points()) / (player.get_total_games() + 1) / 100)
    player.set_avg_points(new_avg_points * 100)

def calculat_avg_rank(player: Ranking):
    rank_json = json.loads(get_player_ranking(player.get_id()))
    avg_rank = 0.0
    for i in range (len(rank_json['rank']) - player.get_current_games_number(), len(rank_json['rank'])):
        avg_rank += rank_json['rank'][i]
    avg_rank /= player.get_current_games_number()
    avg_rank = (float)((int)(avg_rank * 100) / 100)
    player.set_avg_ranking(avg_rank)

def calculate_high_points(player: Ranking):
    if player.get_points() > player.get_high_points():
        player.set_high_points(player.get_points())

def calculate_current_games_played(player: Ranking):
    if player.get_current_games_number() + 1 <= GAMES_TO_LEVEL_UP[player.get_level()]:
        player.set_current_games_number(player.get_current_games_number() + 1)

def calculate_level(player: Ranking):
    if player.get_current_games_number() == GAMES_TO_LEVEL_UP[player.get_level()] and player.get_avg_ranking() <= AVG_RANKINGS[player.get_level()]:
        player.set_level(player.get_level() + 1)
        player.set_current_games_number(0)
        player.set_avg_ranking(0)
        set_player_ranking(player.get_id(), RANK_ORIGINAL_DATA)

def update_rank(discord_id: str, rank: int):
    rank_json = json.loads(get_player_ranking(discord_id))
    rank_json['rank'].append(rank)
    set_player_ranking(discord_id, json.dumps(rank_json))

def write_data(discord_id: str, player: Ranking):
    set_player_rate(discord_id, player.get_rate())
    set_player_avg_points(discord_id, player.get_avg_points())
    set_player_high_points(discord_id, player.get_high_points())
    set_player_avg_rankings(discord_id, player.get_avg_ranking())
    set_player_total_games(discord_id, player.get_total_games())
    set_player_current_games_number(discord_id, player.get_current_games_number())
    set_player_level(discord_id, player.get_level())

if __name__ == '__main__':
    player1_id = '1017241390582870056'
    player1_points = 30000
    player = Ranking(player1_id, int(player1_points), get_player_rate(player1_id), get_player_total_games(player1_id), get_player_avg_rankings(player1_id), get_player_high_points(player1_id), get_player_avg_points(player1_id), get_player_level(player1_id), get_player_current_games_number(player1_id))
    player.set_rank(1)

    update_rank(player.get_id(), player.get_rank()) # pass
    calculate_current_games_played(player) # pass
    calculate_avg_points(player) # pass
    calculat_avg_rank(player)
    calculate_high_points(player)
    calculate_level(player)
    write_data(player.get_id(), player)

