import discord
import asyncio
from discord.ext import commands
from easy_pil import Editor,load_image_async,Font
from discord import File

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self,ctx,member: discord.Member,*,limit = 50) ->None:
        await ctx.delete_original_message()
        msg = []
        try:
            limit = int(limit)
        except:
            return await ctx.send("Please pass in an integer as limit")
        if not member:
            await ctx.channel.purge(limit=limit)
            return await ctx.send(f"Purged {limit} messages", delete_after=3)
        async for m in ctx.channel.history():
            if len(msg) == limit:
                break
            if m.author == member:
                msg.append(m)
                await ctx.channel.delete_messages(msg)
                await ctx.send(f"Purged {limit} messages of {member.mention}", delete_after=3)
    @commands.Cog.listener()
    async def on_member_join(self,member):
        background = Editor("tech.jpg")
        profile_img = await load_image_async(str(member.avatar.url))

        profile = Editor(profile_img).resize((150,150)).circle_image()
        poppins =Font.poppins(size = 50,variant="bold")
        poppins_small = Font.poppins(size = 30,variant="regular")
        background.paste(profile,(325,90))
        background.ellipse((325,90),150,150,outline="white",stroke_width=10)
        background.text((400,260),f"WELCOME TO THE {member.guild}",font=poppins,color="white",align="center")
        background.text((400,325),f"{member.name}#{member.discriminator}",font=poppins_small,color="white",align="center")
        file = File(fp = background.image_bytes,filename="tech.jpg")

    # channel = bot.get_channel(839343878892683264)
        embed = discord.Embed(title ="Welcome to the Server", description = f"Welome {member} to the server,Hope oyu will enjoy the satb with us!")
        await member.send(embed = embed,file =file)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(839343878892683264)
        await channel.send(f"GoodBye{member} :( WE will miss you ")
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, user: discord.Member, *, reason = None):
        if not reason:
            await user.ban()
            await ctx.send(f"**{user}** has been banned permanently for **no reason**.")
        elif not user:
            await ctx.send("please clarify which user to ban!")
        else:
            await user.ban(reason=reason)
            await ctx.send(f"**{user}** has been banned for **{reason}**.")
    @ban.error
    async def ban_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You dont have Permission to ban the User")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"{user.mention} has been unbanned successfully!")
        else:
            await ctx.channel.send("Not a Proper Way to Unban ```!unban Gotcha#3080```")
    @unban.error
    async def unban_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You dont have Permission to Unban the User")
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, user: discord.Member, *, reason = None):
        if not reason:
            await user.kick()
            await ctx.send(f"**{user}** has been kicked for **no reason**.")
        else:
            await user.kick(reason=reason)
            await ctx.send(f"**{user}** has been kicked for **{reason}**.")
    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You dont have permission to Kick this User")

    


def setup(bot):
    bot.add_cog(Admin(bot))