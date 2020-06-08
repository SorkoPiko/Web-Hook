import discord
from discord.ext import commands

class General(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #Events

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')
        await self.client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=(f"How Webhooks Work | w.help")))
	#discord.Activity(type=discord.ActivityType.listening, name=(f"How Webhooks Work | w.help"))

    #Commands

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! {round(self.client.latency * 1000)}ms :ping_pong:')

def setup(client):
    client.add_cog(General(client))
