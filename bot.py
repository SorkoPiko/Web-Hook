import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "w.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzE1Njc3NTIzMTE0OTgzNDc1.XtBW_g.u_wuNdNfCy-tsQGkzRlU-K_FxGI')
