import discord
from discord.ext import commands
from database import *
from constants import *
from ranking import *
from utils import *
import atexit

# TODO: add a command to check the ranking of a player

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')

@bot.event
async def on_ready():
    runtime_logs("Bot is online")
    print(f"Logged in as {bot.user}")

@bot.command(name="register", description="Register a new player")
async def register(ctx):
    runtime_logs(ctx.author, ctx.author.id, "!register")

    # Check if the player has already been registered
    if verify_player(ctx.author.id):
        await ctx.send(ctx.author.mention + " has already been registered")
        return

    # Add the player to the database
    try:
        add_player(ctx.author, ctx.author.id)
        await ctx.send(ctx.author.mention + " has been registered") # return the person who invocates the command
    except:
        await ctx.send(ctx.author.mention + " has already been registered")

# AR -> Average Ranking
@bot.command(name="profile", description="Check your profile")
async def profile(ctx):
    runtime_logs(ctx.author, ctx.author.id, "!profile")

    # Check if the player has been registered
    if not verify_player(ctx.author.id):
        await ctx.send(ctx.author.mention + " has not been registered yet")
    else:
        await ctx.send(ctx.author.mention)

        # Create an embed to display the player's profile
        embed = discord.Embed(title='Current Profile', color=0x66ccff)

        # Add the player's level to the embed
        embed.add_field(name="Level", value=MAHJONG_LEVEL[get_player_level(ctx.author.id)], inline=True)

        # Add the player's rate to the embed
        embed.add_field(name="Rate", value='{:.2f}'.format(get_player_rate(ctx.author.id)), inline=True)

        # Add the player's total games to the embed
        embed.add_field(name="Total Games", value=get_player_total_games(ctx.author.id), inline=True)

        # Add the player's current AR to the embed
        embed.add_field(name="Current AR", value='{:.2f}'.format(get_player_avg_rankings(ctx.author.id)), inline=True)  

        # Add the number of games to play to the embed
        embed.add_field(name="No. of Games to Play", value= GAMES_TO_LEVEL_UP[get_player_level(ctx.author.id)] - get_player_current_games_number(ctx.author.id), inline=True)

        # Add the AR to level up to the embed
        embed.add_field(name="AR to Level Up", value=AVG_RANKINGS[get_player_level(ctx.author.id)], inline=True)
        
        # Add the player's average points to the embed
        embed.add_field(name="Average Points", value=get_player_avg_points(ctx.author.id), inline=True)

        # Add the player's highest points to the embed
        embed.add_field(name="Highest Points", value=get_player_high_points(ctx.author.id), inline=True)

        # Send the embed to the channel
        await ctx.send(embed=embed)

@bot.command(name="record", description="Record the points after the game")
async def record(ctx, player1, player1_points, player2, player2_points, player3, player3_points, player4, player4_points):
    # await ctx.send(player1.id)
    runtime_logs(ctx.author, ctx.author.id, f"!record {player1} {player1_points} {player2} {player2_points} {player3} {player3_points} {player4} {player4_points}")

    # Check if the points are valid
    if player1_points + player2_points + player3_points + player4_points == 100000:
        player1_points += 5000
        player2_points += 5000
        player3_points += 5000
        player4_points += 5000
    elif player1_points + player2_points + player3_points + player4_points != 120000:
        await ctx.send("Points are not valid. Please check again!")
        return

    flag = True

    # Get the player's ID from their mention
    player1_id = player1.replace('<','').replace('>','').replace('@','')
    if not verify_player(player1_id):
        await ctx.send(player1 + " has not been registered yet")
        flag = False

    # Get the player's ID from their mention
    player2_id = player2.replace('<','').replace('>','').replace('@','')
    if not verify_player(player2_id):
        await ctx.send(player2 + " has not been registered yet")
        flag = False

    # Get the player's ID from their mention
    player3_id = player3.replace('<','').replace('>','').replace('@','')
    if not verify_player(player3_id):
        await ctx.send(player3 + " has not been registered yet")
        flag = False

    # Get the player's ID from their mention
    player4_id = player4.replace('<','').replace('>','').replace('@','')
    if not verify_player(player4_id):
        await ctx.send(player4 + " has not been registered yet")
        flag = False

    # If any of the players have not been registered, return
    if not flag:
        return
    
    # Set the players' points in the database
    set_players(player1_id, player1_points, player2_id, player2_points, player3_id, player3_points, player4_id, player4_points)

@bot.command(name="test", description="Check your rank")
async def test(ctx, player):
    print(player)

@atexit.register
def clean():
    runtime_logs("Bot is offline")

bot.run(TOKEN)  # Replace with your bot token