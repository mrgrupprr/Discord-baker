import discord
import configparser
import argparse
import os
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import discord.utils
import requests
ap = argparse.ArgumentParser()
ap.add_argument("--id", required=True, help="Discord users id")
ap.add_argument("--ip", required=True, help="Discord users ip")
args = vars(ap.parse_args())
config = configparser.ConfigParser()
config.read('botdatabase.ini')
token = str(config['botinfo']['bottoken'])
guild = config['botinfo']['guildid']
memberrole = config['botinfo']['memberrole']
domain = config['botinfo']['domain']
exchangepass = config['botinfo']['exchangepass']
intents = discord.Intents.default()
intents.members = True
bot = Bot(command_prefix = '!', intents=intents)
@bot.event
async def on_ready():
    server = bot.get_guild(int(guild))
    userid=int(args["id"])
    userip=str(args["ip"])
    role = discord.utils.get(server.roles, id=int(memberrole))
    member = server.get_member(userid)
    await verify(userid,userip)

def checkifverifydone(idofuser):
    try:
        r3 = requests.post(f'{domain}/checkifverifydone', json={'key': exchangepass, 'id': idofuser})
        return r3.text
    except Exception as e:
        print(e)
        return 'error'

async def verify(userid,userip):
    server = bot.get_guild(int(guild))
    role = discord.utils.get(server.roles, id=int(memberrole))
    member = server.get_member(userid)
    if checkifverifydone(userid) == 'true':
        #role user as verified
        user = await bot.fetch_user(userid)
        await member.add_roles(role)
        await user.send("You are verified, have fun!")
        os._exit(1)
    elif checkifverifydone(userid) == 'error':
        user = await bot.fetch_user(userid)
        await user.send("Error verifying. Please contact a moderator.")
        os._exit(1)
    else:
        user = await bot.fetch_user(userid)
        await user.send("Your not verified. Please contact a administrator.")
        os._exit(1)

bot.run(token)