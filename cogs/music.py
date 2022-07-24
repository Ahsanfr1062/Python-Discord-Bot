import discord
from discord.ext import commands
from discord import FFmpegAudio,FFmpegPCMAudio
import youtube_dl
import os
class Music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command(pass_context = True)
    async def join(ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
        for i in range(1,100):
            voice= await channel.connect()
            source = FFmpegPCMAudio("rizvi.mp3")
            player = voice.play(source)
            await ctx.send("joined the voice channel")
        else:
            await ctx.send("you are not in the voice channel you must be in the voice channel")
    @commands.command(pass_context = True)
    async def leave(ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("i have left the voice channel")
        else:
            await ctx.send("i am not in the Voice channel")
    @commands.command(pass_context = True)
    async def play(ctx,url:str):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice= await channel.connect()
            ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                    }],
                    }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file,"song.mp3")
            source = FFmpegPCMAudio("song.mp3")
            player = voice.play(source)
            await ctx.send("joined the voice channel")
    