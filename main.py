import discord
from discord.ext import commands
from database import *
from constants import *

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="register", description="Register a new player")
async def register(ctx):
    try:
        add_player(ctx.author, ctx.author.id)
        await ctx.send(ctx.author.mention + " has been registered") # return the person who invocates the command
    except:
        await ctx.send(ctx.author.mention + " has already been registered")

@bot.command(name="profile", description="Check your profile")
async def profile(ctx):
    await ctx.send(ctx.author.mention)

    embed = discord.Embed(title='Current Profile', color=0x66ccff)

    embed.add_field(name="Level", value=MAHJONG_LEVEL[get_player_level(ctx.author)], inline=True)

    embed.add_field(name="Rate", value=get_player_rate(ctx.author), inline=True)

    embed.add_field(name="Total Games", value=get_player_total_games(ctx.author), inline=True)

    embed.add_field(name="Current AR", value=get_player_avg_rankings(ctx.author), inline=True)  

    embed.add_field(name="No. of Games to Play", value= GAMES_TO_LEVEL_UP[get_player_level(ctx.author)] - get_player_current_games_number(ctx.author), inline=True)

    embed.add_field(name="AR to Level Up", value=AVG_RANKINGS[get_player_level(ctx.author)], inline=True)
    
    embed.add_field(name="Average Points", value=get_player_avg_points(ctx.author), inline=True)

    embed.add_field(name="Highest Points", value=get_player_high_points(ctx.author), inline=True)

    await ctx.send(embed=embed)

# Not Finished
@bot.command(name="record", description="Record the points after the game")
async def record(ctx, player1, player1_points, player2, player2_points, player3, player3_points, player4, player4_points):
    # await ctx.send(player1.id)
    player1_id = player1.replace('<','').replace('>','').replace('@','')
    player2_id = player2.replace('<','').replace('>','').replace('@','')
    player3_id = player3.replace('<','').replace('>','').replace('@','')
    player4_id = player4.replace('<','').replace('>','').replace('@','')


bot.run("YOUR_TOKEN")  # Replace with your bot token