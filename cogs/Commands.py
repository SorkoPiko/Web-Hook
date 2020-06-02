import discord
from discord.ext import commands

class Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #Events

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')
        await self.client.change_presence(status=discord.Status.online, activity=discord.Streaming(name='Webhooks for everyone!', url='https://www.twitch.tv/sorkopiko'))

def setup(client):
    client.add_cog(Commands(client))
