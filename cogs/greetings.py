from turtle import back
from discord.ext import commands
import discord
from PIL import ImageFont, ImageDraw,Image
from discord import File

class greetings(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self,message):
        if ("lun") in message.content:
            emoji = "😎"
            await message.add_reaction(emoji)
            self.bot.process_commands(message)
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction , member):
        channel = reaction.message.channel
        await channel.send(member.mention+"has sent:"+reaction.emoji)
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction,member):
        channel = reaction.message.channel
        await channel.send(member.mention + "has removed"+reaction.emoji)
    @commands.Command()
    @commands.has_permissions(manage_roles = True)
    async def addrole(self,ctx,user:discord.Member,role:discord.Role) -> None:
        if role in user.roles:
            await ctx.send(f"{user.mention} already has `{role}` role")
        else:
            await user.add_roles(role)
            await ctx.send(f"Added {role} to {user.mention}")
    @addrole.error
    async def addrole_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You Dont have permission to do this commmand")
    @commands.command()
    async def speak(self,ctx,*args):
        msg  =" ".join(args)
        font = ImageFont.truetype("Kanit-Bold.ttf",50)
        img = Image.open("cat.png")


        cx,cy =(300,150)
        draw =ImageDraw.Draw(img)
        draw.text((cx,cy),msg,(0,0,0),font=font)
        img.save("img-edited.jpg")

        with open("img-edited.jpg","rb") as f:
            img = File(f)
            await ctx.send(file = img)
    @commands.command()
    async def invites(self,ctx, user = None):
        if user == None:
            totalInvites = 0
            for i in await discord.guild.invites():
                if i.inviter == ctx.author:
                    totalInvites += i.uses
            await ctx.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")
        else:
            totalInvites = 0
            for i in await discord.guild.invites():
                member = ctx.message.guild.get_member_named(user)
                if i.inviter == member:
                    totalInvites += i.uses
            await ctx.send(f"{member} has invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")
    @commands.command()
    async def hello(self,ctx):
        await ctx.send("Hello! i am a bot from DarkLight!")
    @commands.command()
    async def ping(self,ctx):
        await ctx.send("PONG!")



def setup(bot):
    bot.add_cog(greetings(bot))