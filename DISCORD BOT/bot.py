import discord
import asyncio
import requests
import os
import threading
import discord.utils
import configparser
from discord.ext import commands
from discord.utils import get
from discord.ext import commands
from discord import Option
from discord.commands import slash_command
from discord.ext.commands import Bot


config = configparser.ConfigParser()
config.read('botdatabase.ini')
intents = discord.Intents.default()
intents.members = True
bot = Bot(command_prefix = '!', intents=intents)
    
def fetchurlcorectly():
    domainnormalized = domain
    domainwithoutslash = domainnormalized[:-1]
    if domain.endswith('/'):
        return domainwithoutslash
    else:
        return domainnormalized

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
url = f'https://discord.com/oauth2/authorize?response_type=code&client_id={clientid}&scope=identify+guilds.join&state=15773059ghq9183habn&redirect_uri={fetchurlcorectly()}/discordauth'

        

        
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
    role = discord.utils.get(server.roles, id=int(memberrole))
    channel = discord.utils.get(server.channels, id=int(welcome_channel))
    if checkifverifydone(member.id) == 'true':
        await channel.send(f'Welcome {member.mention} to the {server} !.')
        print('Verified')
        await member.add_roles(role)
        embed3=discord.Embed(title=f"Welcome back to {server}", description=f"You are verified.", color=0xfbff00)
        embed3.set_footer(text="Made with ❤️ by exinty")
        await member.send(embed=embed3)

    else:
        await channel.send(f'Welcome {member.mention} to the {server} !. Please check your DMs for verify yourself.')
        embed=discord.Embed(title="Verification", description=f"Welcome, to proceed in the server, follow the link below to verify.\n[Click Here!]({url})", color=0xfbff00)
        embed.set_footer(text="Made with ❤️ by exinty")
        class View(discord.ui.View):
            @discord.ui.button(label="Press me after verification!", style=discord.ButtonStyle.primary, emoji="✔️") 
            async def button_callback(self, button, interaction):
                await interaction.response.send_message("Checking Roles...")
                if checkifverifydone(member.id) == 'true':
                    await member.add_roles(role)
                    await member.send("Verified!")
                else:
                    await member.send("You are not verified!")
        await member.send(embed=embed, view=View())
        sendrequestforpending(member.id)

        
@bot.event
async def on_message(message):
    print("New message: " + message.content + " - " + message.author.name)
    if message.author == bot.user:
        pass
    await bot.process_commands(message)

@bot.slash_command(guild_ids=[guild], name='restore', aliases=['restore'], description='Restore`s all of the users.')
async def restore(
    ctx,
    key: Option(str, "Enter your Restore key.", required=True),
):
    if key == therestorekey:
        await ctx.respond('Starting restore process!', ephemeral=True)
        if restoremember() == 'succsess':
            await ctx.author.send('Restore process is done!')
        else:
            await ctx.author.send('Not restored.')
    else:
        await ctx.respond('Key is wrong!', ephemeral=True)

def sendrequestforpending(idofuser):
    try:
        r1 = requests.post(f'{domain}/requestid', json={'key': exchangepass, 'id': idofuser})
        print(r1.text)
        return r1.text
    except:
        return 'error sending'

def checkifverifydone(idofuser):
    try:
        r3 = requests.post(f'{domain}/checkifverifydone', json={'key': exchangepass, 'id': idofuser})
        print(r3.text)
        return r3.text
    except:
        return 'error'

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
    r1 = requests.post(f'{domain}/data', json={'dataset': 'CLIENT_ID'})
    r3 = requests.post(f'{domain}/data', json={'dataset': 'bottoken'})
    r5 = requests.post(f'{domain}/data', json={'dataset': 'exchangepass'})
    r6 = requests.post(f'{domain}/data', json={'dataset': 'welcomechannel'})
    r7 = requests.post(f'{domain}/data', json={'dataset': 'verifiedrole'})
    r8 = requests.post(f'{domain}/data', json={'dataset': 'restorekey'})
    r9 = requests.post(f'{domain}/data', json={'dataset': 'guildid'})
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
    print('Setup complete. Please restart the BOT')
    waitformesweety = input()
    quit()

if __name__ == '__main__':
    cls()
    bot.run(token)
