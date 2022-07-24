from discord.ext import commands
import discord
import os
from bottoken import bot_token,Pass
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',intents = intents)
# bot.db = mysql.connector.connect(
#     host = "127.0.0.1",
#     user = "root",
#     password = Pass,
#     database = "firstdb")
# cursor = bot.db.cursor(dictionary = True)
# cursor.execute("CREATE TABLE IF NOT EXISTS warns(user_id varchar(250),reason varchar(250),time int, guild_id int,primary key(user_id));")

@bot.event
async def on_ready():
    print("------------------------------")
    print("Bot is ready to use for hehe")
    print("------------------------------")




initial_extension = []

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extension.append(f"cogs.{filename[:-3]}")
if __name__ == "__main__":
    for extension in initial_extension:
        bot.load_extension(extension)
print("this has been execute too")

bot.run(bot_token)