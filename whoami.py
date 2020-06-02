from discord_webhook import *
from time import sleep
def activate(url):
    global minutes
    global content
    avatar_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/1200px-Question_mark_%28black%29.svg.png'
    username = 'Who am I?'
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
activate('https://discord.com/api/webhooks/717288716850167872/sK2ZEz2T4AjSMFr8pUpI1yS1YQGL0xW97Ov5HR9SBHXCJlqcBlszP5gr-6t0-dElaIFc')
