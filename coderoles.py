import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from plugins import *
from guildinfo import guildInfo

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='w!', intents=intents)
guildDict = {}

@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))
    async for i in bot.fetch_guilds():
        info = guildInfo()
        info.setGuild(i)
        guildDict[i.id] = info

@bot.command()
async def setMod(ctx, role):
    moderatorRole = discord.utils.get(ctx.guild.roles, name=role)
    if moderatorRole != None:
        guildDict[ctx.guild.id].setModRole(moderatorRole)
        await ctx.send(f'Moderator Role Changed: {moderatorRole}')
    else:
        await ctx.send(f'No role under that name.')

@bot.command()
async def getMod(ctx):
    moderatorRole = guildDict[ctx.guild.id].modRole()
    await ctx.send(f'Moderator Role: {moderatorRole}')

@bot.command()
async def roleAdd(ctx, role):
    guild = guildDict[ctx.guild.id]
    if guild.modRole() in ctx.author.roles:
        roleList = guild.roleList()
        if role in roleList:
            await ctx.send('Role already in list. Check roles by typing `w!roles')
        if discord.utils.get(ctx.guild.roles, name=role) != None:
                guild.addRoleList(str(role))
                await ctx.send(f'Role Added/Changed: {role}')
        elif discord.utils.get(ctx.guild.roles, name=role) == None:
                await ctx.send(f'No role under that name. Discord is case sensitive, so check for that or any misspellings.')
    else:
        await ctx.send(f'Error, you must be a moderator to do this command.')

@bot.command()
async def roleRemove(ctx, role):
    guild = guildDict[ctx.guild.id]
    if guild.modRole() in ctx.author.roles:
        global roleList
        if str(role) in roleList:
            guild.removeRoleList(str(role))
            await ctx.send(f'Role Removed: {role}')
        else:
            await ctx.send(f'Role not in list. Discord is case sensitive, so check for that or any misspellings.')
            await ctx.send(f'Please check the role list by doing `w!roles`')
    else:
        await ctx.send(f'Error, you must be a moderator to do this command.')

@bot.command()
async def roles(ctx):
    guild = guildDict[ctx.guild.id]
    roleList = guild.roleList()
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
    guild = guildDict[ctx.guild.id]
    roleList = guild.roleList()
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

@bot.command()
async def explode(ctx):
    await ctx.message.delete()
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
    await ctx.message.delete()
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

@bot.command()
async def repeat(ctx, *args):
    await ctx.message.delete()
    arguments = ' '.join(args)
    arguments += f" - {ctx.message.author.display_name}"
    await ctx.send(arguments)

bot.run(TOKEN)