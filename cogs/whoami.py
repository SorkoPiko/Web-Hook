from discord_webhook import *
from time import sleep
import discord
from discord.ext import commands

global param1
global param2

#def activate(url):
#    global minutes
#    global content
#    avatar_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/1200px-Question_mark_%28black%29.svg.png'
#    username = 'Who am I?'
#    minutes = 11
#    content = (f'Who am I? @everyone, you have {str(minutes)} minutes to respond with an answer.')
#    for x in range(minutes):
#        minutes = (minutes - 1)
#        if minutes == 1:
#            content = (f'Who am I? @everyone, you have 1 minute to respond with an answer.')
#        elif minutes == 0:
#            content = (f"Time's up, @everyone! You didn't guess who I am!")
#        else:
#           content = (f'Who am I? @everyone, you have {str(minutes)} minutes to respond with an answer.')
#        webhook = DiscordWebhook(url=url, username=username, avatar_url=avatar_url, content=content)
#        response = webhook.execute()
#        sleep(60)
#activate('https://discord.com/api/webhooks/717872615842119731/dAZoZTpmDFvNApVpXv_EpBBLpXn_eqAdB9GhYrt0OsC-ZvikuvmeyL0FJ-UxVqXBk1fI')

class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #Events

    #Commands

    @commands.command(description="Play with Who am I?. Example: w.whoami play <your webhook url> ")
    async def whoami(self, ctx, param1, param2):
        if param1 == 'respond':
            username1 = param2
        def activate(url, *, username='Clyde'):
            avatar_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/1200px-Question_mark_%28black%29.svg.png'
            print(username)
            minutes = 11
            content = (f'Who am I? @everyone, you have {str(minutes)} minutes to respond with an answer.')
            for x in range(minutes):
                minutes = (minutes - 1)
                if minutes == 1:
                    content = (f'Who am I? @everyone, you have 1 minute to respond with an answer.')
                elif minutes == 0:
                    content = (f"Time's up, @everyone! You didn't guess who I am!")
                else:
                    content = (f'Who am I? @everyone, you have {str(minutes)} minutes to respond with an answer.')
                webhook = DiscordWebhook(url=url, username=username, avatar_url=avatar_url, content=content)
                response = webhook.execute()
                sleep(60)
        if param1 == 'play':
            activate(param2)
        elif param1 == 'respond':
            pass
        else:
            await ctx.send('`ERROR 404:` Command not found.')

def setup(client):
    client.add_cog(Fun(client))
