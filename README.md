# 🤑Discord-backer🤑
A open-source Discord member backup and restore tool for your server.
This bot gets users to Authorize themselves upon joining your server, and then later on, if your server is raided, or deleted, you can rejoin all the users who Authorized to a new server.

You will need is a discord application, and a bot within said application. You will also need a server, and a role to be given to users that verify. You will also need a way to host the API. We recommend a VPS from [this seller](https://bit.ly/vpsshop).


# 🛑IMPORTANT NOTICE🛑
TO USE MULTIPLE SERVERS THE VERIFIED ROLE NEEDS TO HAVE ON BOTH SERVERS THE SAME ROLE NAME


# AUTOMATED Setup
Run setup.py and enter your ACCOUNT TOKEN and the server relevent stuff, add your bot to the server and the setup is done.  credits to @swishyw for the oauth.py file.

# 1. Setup
First, we are gonna need your discord bot token, Client ID, Client Secret.
This we can do at the [discord developers site](https://discord.com/developers/applications)
Now we are gonna make a new application

![opera_F9NGA2EeV9](https://user-images.githubusercontent.com/70100389/147709401-feb1c02b-d02f-46df-8fa9-5c89f0f8e590.png)


Once we have our application set up, we are gonna click on OAuth2, here we will find our Client ID, Secret Token, and our redirect URL. These we will need for later so save them.


![opera_vXfFJ1nWUU](https://user-images.githubusercontent.com/70100389/147709519-9332234a-b11f-43cc-abdc-06a970e97389.png)

Finally, we are going to need a bot token. Watch [this](https://youtu.be/dCkYje6B-io) video if you need help.

## Redirect

Now, we need to allow a redirect to our domain/api.
Add a new redirect for the following:
- https://yourdomainhere.com/discordauth
- http://yourdomainhere.com/discordauth
Obviously, replace `yourdomainhere.com` with your own domain/ip.

![opera_f22iKehJjl](https://user-images.githubusercontent.com/70100389/147709654-c2eb9cb7-6e96-4823-8c46-33add2f3a75c.png)
We are done on the discord developers site for now.

## PART 1 - Installation FLASK API 

First install the requirements: 

```
pip install -r requirements.txt
``` 

Then, open setup.py. It will ask you for the following: CLIENT_ID, CLIENT_SECRET, CLIENT_TOKEN (your bot's token), DOMAIN, Member-role (name of the role eg verified). 

Say yes to running the API.


## PART 2 - Installation DISCORD BOT
INFO❗: This whole process is routed via the API (application.py), thus you can code the bot yourself.

Change directories to the DISCORD BOT folder, then run bot.py
## Starting the system

You will need the program running 24/7, again, we recommend a VPS from [this seller](https://bit.ly/vpsshop).

First, run application.py
Secondly, if you see no errors, move to the DISCORD BOT folder and run bot.py

If no errors are shown, you are good to go! make sure your bot is in your server, and has administrator permissions. (also make sure it's role is at the top of the role list)

Make sure to let @everyone only see a single channel where they cant type, and in said channel, write a message that goes along the lines of "Check your DMs with @(your bots name) to verify.".

To restore users who have verified:
- restart the API (application.py) and the BOT
- run `!restore YOURRESTOREKEY `

The bot will attempt to add back all users who have authorized and are in the database.

# Endnote
Please **Star** this repo if you like it! This project has taken and continues to take lots of time! <3
Add me if you need more help: `haze#2603`


# Roadmap
List of things i'm planning to add:

- Web GUI for restoring/backuping the members
- Telegram bot For restoring/backuping
- Command less verify (give roles as soon as user authorizes)

# Advanced
Feel free to modify this code, but remember to credit this repo.
