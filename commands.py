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

pingRole = "React to this message with 💜 to be notified when Alice streams. React to this message with 💗 if you follow Alice on twitch!"
TWITCHROLE = "TWITCH NOTIFICATION"
FOLLOWROLE = "Follower"
moderatorRole = "@everyone"
reactionRole = {}

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
async def modRoles(ctx, role, add=True):
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
async def reactionRoleAdd(ctx, role, reaction):
    global reactionRole
    if is_emoji(reaction) == True:
        if discord.utils.get(ctx.guild.roles, name=role) != None:
            reactionRole[str(role)] = str(reaction)
            await ctx.send(f'Reaction Role Added/Changed: {role} - {reaction}')
        elif discord.utils.get(ctx.guild.roles, name=role) == None:
            await ctx.send(f'No role under that name.')
        else:
            await ctx.send(f'Error. Try again by typing `w!reactionRoleAdd <role> <reaction>`')
    else:
         await ctx.send(f'Error. Reaction MUST be a single Emoji.')

@bot.command()
async def reactionRoleRemove(ctx, role):
    global reactionRole
    if str(role) in reactionRole:
        if reactionRole[str(role)] != None:
                del(reactionRole[str(role)])
                await ctx.send(f'Reaction Role Removed: {role}')
    else:
            await ctx.send(f'Error, role not found, roles are casesensitive, so check for that or any misspellings :3 baaaa')
            await ctx.send(f'Please check the role list by doing `w!reactionRoleList`')

@bot.command()
async def reactionRoleList(ctx):
    global reactionRole
    if reactionRole == {}:
        await ctx.send("No reaction roles added ;-;")
        await ctx.send("add reactions by typing `w!reactionRoleAdd <role> <reaction>`")
    else:
        roleList1, roleList2 = dictToLists(reactionRole)
        emb = discord.Embed(title = "Here is a list of the roles! :3", description="")
        for i in range(len(roleList1)):
            emb.description += f"{roleList1[i]} : {roleList2[i]}"
            emb.description += "\n"
        await ctx.send(embed=emb)

@bot.command()
async def reactionRoleSetup(ctx):
    global reactionRole
    if reactionRole == {}:
        await ctx.send("No reaction roles added ;-;")
        await ctx.send("add reactions by typing `w!reactionRoleAdd <role> <reaction>`")
    else:
        roleList1, roleList2 = dictToLists(reactionRole)
        emb = discord.Embed(title = "React to this message in order to get roles!", description="")
        for i in range(len(roleList1)):
            emb.description += f"{roleList1[i]} : {roleList2[i]}"
            emb.description += "\n"
        await ctx.send(embed=emb)

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