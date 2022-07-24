import mysql.connector
import discord 
from discord.ext import commands
from bottoken import bot_token,Pass

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',intents = intents)

@bot.event
async def on_ready():
    print("------------------------------")
    print("Bot is ready to use for hehe")
    print("------------------------------")

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = Pass,
    database = "firstdb"
)

cursor = mydb.cursor(dictionary = True)

@bot.command()
async def set(ctx):
    sql = "INSERT INTO discord_hell (id,name) VALUES (%s,%s)"
    val = (ctx.author.id,ctx.author.name)
    cursor.execute(sql,val)

@bot.command()
async def check(ctx):
    cursor.execute(f"SELECT name FROM discord_hell where ID = {ctx.author.id}")
    rows = cursor.fetchall()
    for row in rows:
        await ctx.send(row["name"])

@bot.command()
async def ping(ctx):
    await ctx.send("PONG")

bot.run(bot_token)
