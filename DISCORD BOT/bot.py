import discord
import asyncio
import requests
import discord.utils
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.members = True
client = Bot(command_prefix = '!', intents=intents)


token = 'TOKEN HERE' #enter your bot token here
guild = 919201123123124334 # YOUR INTEGER GUILD ID HERE
welcome_channel = 919512312311222480 # YOUR WELCOME CHANNEL ID HERE
memberrole = 919556512517258 # YOUR MEMBER ROLE ID HERE
clientid = 'clientidhere'
domain = 'http://domain.com' #this is for the flask server we set up (RESTORE API)


#ignore this 
url = f'https://discord.com/oauth2/authorize?response_type=code&client_id={clientid}&scope=identify+guilds.join&state=15773059ghq9183habn&redirect_uri={domain}/discordauth'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Verification')) # you can change this if you want
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    server = client.get_guild(guild)
    if checkifverifydone(member.id) == 'true':
        print('Verified')
        role = discord.utils.get(client.get_guild(guild).roles, id= memberrole)
        await member.add_roles(role)
        await member.send(f'Your verified.')
        await member.send(f'Welcome back to {server}!')
    else:
        await client.get_channel(welcome_channel).send(f'Welcome {member.mention} to the {server}! Please look into your dms in order to get started.')
        await member.send(f'Welcome to {server}! Please verify here:' + url)
        await member.send(f'If you have any questions, please contact a moderator.')
        await member.send(f'You have two minutes to complete the verify.')
        if sendrequestforpending(member.id) == 'succsess':
            print('waiting 10sec')
            await asyncio.sleep(10)
            print('wait done')
            if checkifverifydone(member.id) == 'true':
                #role user as verified
                role = discord.utils.get(client.get_guild(guild).roles, id= 919556043393077258)
                await member.add_roles(role)
                await member.send(f'Your verified.')
            else:
                await member.send(f'Your not verified.')
        else:
            print("A error occured with the request.")



@client.event
async def on_message(message):
    if message.content == 'hi':
        await message.channel.send('Hello!')
    elif message.content == '!restore':  #if you want you add security
        restoremember()
        if restoremember() == 'succsess':
            await message.channel.send('Restored.')
        else:
            await message.channel.send('Not restored.')


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

client.run(token)
