import discord
import asyncio
import requests
import os
import discord.utils
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.members = True
bot = Bot(command_prefix = '!', intents=intents)


token = 'TOKEN HERE' #enter your bot token here
guild = 'Your guild ID' # YOUR INTEGER GUILD ID HERE
welcome_channel = 'Welcome Channel ID' # YOUR WELCOME CHANNEL ID HERE
memberrole = 'Verified role' # YOUR MEMBER ROLE ID HERE
clientid = 'clientidhere' #enter your client id here
therestorekey = 'crackers' #enter your restore key here so only admin can run the command
domain = 'https://domain-or-ip.com' #this is for the flask server we set up (RESTORE API) / Please don`t add a slash at the end.


#ignore this 
url = f'https://discord.com/oauth2/authorize?response_type=code&client_id={clientid}&scope=identify+guilds.join&state=15773059ghq9183habn&redirect_uri={domain}/discordauth'


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')



@bot.event
async def on_ready():
    cls()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Verification')) # you can change this if you want
    print('Bot is ready.')
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

@bot.event
async def on_member_join(member):
    server = bot.get_guild(guild)
    if checkifverifydone(member.id) == 'true':
        print('Verified')
        role = discord.utils.get(bot.get_guild(guild).roles, id= memberrole)
        await member.add_roles(role)
        await member.send(f'Your verified.')
        await member.send(f'Welcome back to {server}!')
    else:
        await bot.get_channel(welcome_channel).send(f'Welcome {member.mention} to the {server}! Please look into your dms in order to get started.')
        await member.send(f'Welcome to {server}! Please verify here: ' + url)
        await member.send(f'If you have any questions, please contact a moderator.')
        await member.send(f'After succsesful verify please enter !verify.')
        



@bot.event
async def on_message(message):
    print(message)

@bot.command
async def restore(ctx, key):
    if key == therestorekey:
        if restoremember() == 'succsess':
            await ctx.send('Restored.')
        else:
            await ctx.send('Not restored.')
    else:
        await ctx.send('Nice try bozo.')

@bot.command
async def verify(ctx):
    if checkifverifydone(ctx.author.id) == 'true':
        await ctx.send('You are already verified.')
    else:
            if checkifverifydone(ctx.author.id) == 'true':
                #role user as verified
                role = discord.utils.get(bot.get_guild(guild).roles, id= memberrole)
                await ctx.author.add_roles(role)
                await ctx.send(f'Your verified.')
            else:
                await ctx.send(f'Your not verified. Please contact a administrator.')

def sendrequestforpending(idofuser):
    r1 = requests.post(f'{domain}/requestid', json={'key': 'thisisthekey', 'id': idofuser})
    print(r1.text)
    return r1.text

def checkifverifydone(idofuser):
    r2 = requests.post(f'{domain}/checkifverifydone', json={'key': 'waiting', 'id': idofuser})
    print(r2.text)
    return r2.text

def restoremember():
    r2 = requests.post(f'{domain}/restore', json={'code': 'crackers'})
    print(r2.text)
    return r2.text


def start():
    r = f'{domain}/working'
    if r.text == 'true':
        bot.run(token)
    else:
        print('Server is not running correctly. Please check your Flask web server.')
