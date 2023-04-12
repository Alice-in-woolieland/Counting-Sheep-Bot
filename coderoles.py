import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from emoji import is_emoji
from plugins import *

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='w!', intents=intents)

moderatorRole = "@everyone"
roleList = []

@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))

@bot.command()
async def repeat(ctx, *args):
    await ctx.message.delete()
    arguments = ' '.join(args)
    arguments += f" - {ctx.message.author.display_name}"
    await ctx.send(arguments)

@bot.command()
async def setMod(ctx, role, add=True):
    global moderatorRole
    if add==True and role != None:
        moderatorRole = discord.utils.get(ctx.guild.roles, name=role)
        await ctx.send(f'Moderator Role Changed: {moderatorRole}')
    elif add==False and role != None:
        moderatorRole = "@everyone"
        await ctx.send(f'Moderator Role Changed: {moderatorRole}')
    else:
        await ctx.send(f'Critical Error (Tag Alice)')

@bot.command()
async def roleAdd(ctx, role):
    if moderatorRole in ctx.author.roles:
        global roleList
        if role in roleList:
            await ctx.send('Role already in list. Check roles by typing `w!roles')
        if discord.utils.get(ctx.guild.roles, name=role) != None:
                roleList.append(str(role))
                await ctx.send(f'Role Added/Changed: {role}')
        elif discord.utils.get(ctx.guild.roles, name=role) == None:
                await ctx.send(f'No role under that name. Discord is case sensitive, so check for that or any misspellings.')
    else:
        await ctx.send(f'Error, you must be a moderator to do this command.')

@bot.command()
async def roleRemove(ctx, role):
    if moderatorRole in ctx.author.roles:
        global roleList
        if str(role) in roleList:
            roleList.remove(str(role))
            await ctx.send(f'Role Removed: {role}')
        else:
            await ctx.send(f'Role not in list. Discord is case sensitive, so check for that or any misspellings.')
            await ctx.send(f'Please check the role list by doing `w!roles`')
    else:
        await ctx.send(f'Error, you must be a moderator to do this command.')

@bot.command()
async def roles(ctx):
    global roleList
    if roleList == []:
        await ctx.send("No roles added ;-;")
        await ctx.send("add roles by typing `w!roleAdd <role>`")
    else:
        emb = discord.Embed(title = "Here is a list of the roles! :3", description="")
        for i in range(len(roleList)):
            emb.description += roleList[i]
            emb.description += "\n"
        await ctx.send(embed=emb)

@bot.command()
async def roleGive(ctx, *args):
    global roleList
    inputRoles = args
    discUser = ctx.author
    if inputRoles == []:
            await ctx.send("No roles specified ;-;")
            await ctx.send("See the roles by typing `w!roles`")
    for i in range(len(inputRoles)):
        if inputRoles[i] in roleList:
            role = discord.utils.get(ctx.guild.roles, name=inputRoles[i])
            await discUser.add_roles(role)
            await ctx.send(f"{inputRoles[i]} has been added to {discUser.name}")
        else:
            await ctx.send(f"{inputRoles[i]} is not on the role list.")
            await ctx.send('Please check the role list by doing `w!roles`')

@bot.command()
async def explode(ctx):
    gif = generateExplosion()
    emb = discord.Embed()
    emb.set_image(url = str(gif))
    detonate = ctx.author.name
    if ctx.message.mentions == []:
        title = str(f"{detonate} exploded themself!")
    else:
        explodee = ctx.message.mentions[0].mention
        title = f"{detonate} exploded {explodee}"
    await ctx.send(title, embed=emb)

@bot.command()
async def flip(ctx):
    gif = generateFlip()
    emb = discord.Embed()
    emb.set_image(url = str(gif))
    detonate = ctx.author.name
    if ctx.message.mentions == []:
        title = str(f"{detonate} get flipped bitch")
    else:
        explodee = ctx.message.mentions[0].mention
        title = f"{explodee} get flipped bitch"
    await ctx.send(title, embed=emb)

bot.run(TOKEN)