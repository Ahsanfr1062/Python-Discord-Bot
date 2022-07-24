import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Subscription(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.add_item(nextcord.ui.Button(style=nextcord.ButtonStyle.link, url='https://www.youtube.com/watch?v=dQw4w9WgXcQ', label="Create Thread"))

    @nextcord.ui.button(label = "subscribe", style = nextcord.ButtonStyle.red)
    async def subscribe(self,button:nextcord.ui.Button,interaction:Interaction):
        await interaction.response.send_message("You have just subscribed to Premium Plan",ephemeral=False)
        self.value = True
        self.stop()

    @nextcord.ui.button(label = "like", style = nextcord.ButtonStyle.blurple)
    async def like(self,button:nextcord.ui.Button,interaction:Interaction):
        await interaction.response.send_message(f"You have just Liked our {interaction.guild} Premium Plan",ephemeral=False)
        self.value = True
        self.stop()
    nextcord.ui.button(label='Create a thread', style=nextcord.ButtonStyle.blurple)
    async def rickroll(self, button: nextcord.ui.Button, interaction: Interaction):
      await interaction.response.send_message('got rickrolled', ephemeral=False)
      self.value = True
      self.stop()


class UI(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    testserverid = 839342992719609877
    @nextcord.slash_command(name ="premium", description = "vgfcdgvfcdxsfvcdxszgvfcdxs",guild_ids = [testserverid])
    async def premium(self,interaction:Interaction):
        view = Subscription()
        await interaction.response.send_message("Here is the our Premium Plan Please Choose One:", view = view)
        await view.wait()
        if view.value is None:
            return
        elif view.value:
            print("htis is not timed out")
        else:
            print("timed out")


    



def setup(bot):
    bot.add_cog(UI(bot))

        

