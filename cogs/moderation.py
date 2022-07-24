from discord.ext import commands
import discord
import asyncio
class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

     #Mute command to mute th people 
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def mute(self,ctx, member:discord.Member,*,reason = None):
        role = discord.utils.get(member.guild.roles, name='Muted')
        if not reason:
            await member.add_roles(role)
            await ctx.send(f"{member} has been muted indefinalty \n **Reason:No Reason Given**")
        elif role in member.roles:
            await ctx.send(f"{member.mention} is already muted")
        else:
            await member.add_roles(role)
            await ctx.send(f"{member} has been muted indefinaotlry \n **Reason: {reason}**")
    @mute.error
    async def mute_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You Dont have permission to run this commmand")
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unmute(self,ctx,member:discord.Member):
        role = discord.utils.get(member.guild.roles , name = "Muted")
        for i in member.roles:
            if i  == role:
                await member.remove_roles(role)
                await ctx.send(f"{member.mention} has been unmuted")
        else:
            await ctx.send(f"{member.mention} is not muted")


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def tempmute(self, ctx, member: discord.Member,time):
        muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
        time_convert = {"s":1, "m":60, "h":3600,"d":86400}
        tempmute= int(time[0]) * time_convert[time[-1]]
        await ctx.message.delete()
        await member.add_roles(muted_role)
        embed = discord.Embed(description= f"✅ **{member.display_name}#{member.discriminator} muted successfuly**", color=discord.Color.green())
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(tempmute)
        await member.remove_roles(muted_role)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def tempban(self,ctx,member:discord.Member,time,*, reason = None):
        time_convert = {"s":1,"m":60,"h":3600,"d":86400}
        tempmute = int(time[0]) * time_convert[time[-1]]
        await ctx.message.delete()
        await member.ban(reason = reason)
        await ctx.send(f"{member.mention} has been banned successfully for {time} of time")
        await asyncio.sleep(tempmute)
        await member.unban()
    @commands.Cog.listener()
    async def on_message(self,message):
        lis = ["fuck","bitch","nigga","gando"]
        for i in lis:
            if message.content == i:
                await message.delete()
                await self.bot.process_commands(message)
        await message.channel.send("Dont say this word again!")