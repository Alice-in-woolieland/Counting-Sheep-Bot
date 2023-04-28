import os
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
from dotenv import load_dotenv
import asyncio

load_dotenv()

app_id = os.getenv('APP_ID')
app_secret = os.getenv('APP_SECRET')
twitch_name = os.getenv('TWITCH_USER')

async def twitch_example():
    print("GOING")
    twitch = await Twitch(app_id, app_secret)
    user = await first(twitch.get_users(logins=twitch_name))
    print("TRYING")
    # print the ID of your user or do whatever else you want with it
    channel = await twitch.get_channel_information(user.id)
    channel.to_dict()
    print(channel.title)
    
    

asyncio.run(twitch_example())