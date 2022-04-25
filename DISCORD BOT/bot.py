import discord
import asyncio
import requests
import os
import discord.utils
import configparser
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot

config = configparser.ConfigParser()
config.read('botdatabase.ini')
intents = discord.Intents.default()
intents.members = True
bot = Bot(command_prefix = '!', intents=intents)

#ignore this 
token = str(config['botinfo']['bottoken'])
guild = config['botinfo']['guildid']
welcome_channel = config['botinfo']['welcome_channel']
memberrole = config['botinfo']['memberrole']
clientid = config['botinfo']['client_id']
therestorekey = config['botinfo']['therestorekey']
domain = config['botinfo']['domain']
exchangepass = config['botinfo']['exchangepass']
tempkey = config['botinfo']['tempkey']
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
    server = bot.get_guild(int(guild))
    channel = discord.utils.get(server.channels, id=int(welcome_channel))
    if checkifverifydone(member.id) == 'true':
        print('Verified')
        role = discord.utils.get(bot.get_guild(guild).roles, id=int(memberrole))
        await member.add_roles(role)
        await member.send(f'Your verified.')
        await member.send(f'Welcome back to {server}!')
    else:
        await channel.send(f'Welcome {member.mention} to the {server} ! Please look into your dms in order to get verified.')
        await member.send(f'Welcome to {server}! Please verify here: ' + url)
        await member.send(f'If you have any questions, please contact a moderator.')
        await member.send(f'After succsesful verify please enter !verify.')
        sendrequestforpending(member.id)
        

@bot.command()
async def restore(ctx, key):
    await ctx.message.delete()
    if key == therestorekey:
        if restoremember() == 'succsess':
            await ctx.send('Restored.', delete_after=3)
        else:
            await ctx.send('Not restored.', delete_after=3)
    else:
        await ctx.send('Nice try bozo.', delete_after=3)

@bot.command()
async def verify(ctx):
        if checkifverifydone(ctx.author.id) == 'true':
            #role user as verified
            role = discord.utils.get(bot.get_guild(guild).roles, id= memberrole)
            await ctx.author.add_roles(role)
            await ctx.send(f'Your verified. have fun!')
        else:
            await ctx.send(f'Your not verified. Please contact a administrator.')

@bot.command()
async def test(ctx):
    await ctx.send('test')

def sendrequestforpending(idofuser):
    r1 = requests.post(f'{domain}/requestid', json={'key': exchangepass, 'id': idofuser})
    print(r1.text)
    return r1.text

def checkifverifydone(idofuser):
    r2 = requests.post(f'{domain}/checkifverifydone', json={'key': exchangepass, 'id': idofuser})
    print(r2.text)
    return r2.text

def restoremember():
    r2 = requests.post(f'{domain}/restore', json={'code': exchangepass})
    print(r2.text)
    return r2.text


def start():
    if config['setup']['setup'] == 'no':
        setup()
    else:
        r = requests.post(f'{domain}/working')
        if r.text == 'true':
            bot.run(token)
        else:
            print('Server is not running correctly. Please check your Flask web server.')


def setup():
    cls()
    print("Welcome to the bot setup be sure to setup first teh flask server")
    print("If you have not setup the flask server yet, please do so now.")
    print("")
    print("If you have setup the flask server, please enter the following information.")
    print("")
    print("Enter the domain/ip of the flask server: ")
    domain = input()
    r = requests.post(f'{domain}/working')
    if r.text == 'true':
        pass
    else:
        print('Server is not running correctly. Please check your Flask web server.')
        waitformesweety = input()
    r2 = requests.post(f'{domain}/data', json={'key': 'test', 'dataset': 'pass'})
    config['botinfo']['tempkey'] = r2.text
    with open('botdatabase.ini', 'w') as configfile:
        config.write(configfile)
    r1 = requests.post(f'{domain}/data', json={'key': tempkey, 'dataset': 'CLIENT_ID'})
    r3 = requests.post(f'{domain}/data', json={'key': tempkey, 'dataset': 'bottoken'})
    r5 = requests.post(f'{domain}/data', json={'key': tempkey, 'dataset': 'exchangepass'})
    r6 = requests.post(f'{domain}/data', json={'key': tempkey, 'dataset': 'welcomechannel'})
    r7 = requests.post(f'{domain}/data', json={'key': tempkey, 'dataset': 'verifiedrole'})
    r8 = requests.post(f'{domain}/data', json={'key': tempkey, 'dataset': 'restorekey'})
    r9 = requests.post(f'{domain}/data', json={'key': tempkey, 'dataset': 'guildid'})
    config['botinfo']['bottoken'] = r3.text
    config['botinfo']['welcome_channel'] = r6.text
    config['botinfo']['memberrole'] = r7.text
    config['botinfo']['therestorekey'] = r8.text
    config['botinfo']['exchangepass'] = r5.text
    config['botinfo']['domain'] = domain
    config['botinfo']['client_id'] = r1.text
    config['botinfo']['guildid'] = r9.text
    config['setup']['setup'] = 'yes'
    with open('botdatabase.ini', 'w') as configfile:
        config.write(configfile)
    print('Setup complete. Please press any button to start the bot')
    waitformesweety = input()
    start()

start()
