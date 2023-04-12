import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

pingRole = "React to this message with 💜 to be notified when Alice streams. React to this message with 💗 if you follow Alice on twitch!"
TWITCHROLE = "TWITCH NOTIFICATION"
FOLLOWROLE = "Follower"

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@bot.command()
async def test(ctx, arg):
    print(arg)
    await ctx.send(arg)
    
@client.event
async def on_raw_reaction_add(payload):
     username = str(payload.member)
     emoji = str(payload.emoji)
     messageid = payload.message_id
     guildid = payload.guild_id
     guild = discord.utils.get(client.guilds, id=guildid)
     channelid = payload.channel_id
     message = discord.utils.get(guild.message, id=messageid)
     print(payload.reaction)
     print(username)
     if message.content == pingRole and emoji == "💜":
          print('purpl.')
          RoleSnowFlake = discord.utils.get(guild.roles, name=TWITCHROLE)
          await payload.member.add_roles(RoleSnowFlake, reason="reactionrole")
     if message.content == pingRole and emoji == "💗":
          print('pink..')
          RoleSnowFlake = discord.utils.get(guild.roles, name=FOLLOWROLE)
          await payload.member.add_roles(RoleSnowFlake, reason="reactionrole")

async def roleSetup(message):
    await message.channel.send(pingRole)

async def roleVarSet(message):
    await message.channel.send('Send the name of the role')

    
commandList = {'roleMessage': roleSetup, 'roleSetup': roleVarSet}

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    if username.lower() == "wooly" and user_message[0:2] == "w!":
            if user_message[2:] in commandList:
                await commandList[user_message[2:]](message)      

client.run(TOKEN)