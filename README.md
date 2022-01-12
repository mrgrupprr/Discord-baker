# 🤑Discord-backer🤑
A open-source Discord member backup and restore tool for your server.
This can help you get all your members in 5 Seconds back after a raid if someone destroyed your server.


🛑IMPORTANT🛑:What you will need is a discord bot, a discord application, and a server.





# 1. Setup
First, we are gonna need your discord bot token, Client ID, Client Secret.
This we can do at the [discord developers site](https://discord.com/developers/applications)
Now we are gonna make a new application

![opera_F9NGA2EeV9](https://user-images.githubusercontent.com/70100389/147709401-feb1c02b-d02f-46df-8fa9-5c89f0f8e590.png)


Once we have our application set up, we are gonna click on OAuth2, here we will find our Client ID, Secret Token, and our redirect URL. These we will need for later so save them.


![opera_vXfFJ1nWUU](https://user-images.githubusercontent.com/70100389/147709519-9332234a-b11f-43cc-abdc-06a970e97389.png)

At last we are gonna need a bot token watch [this on how to make a bot](https://youtu.be/dCkYje6B-io)

## Redirect

Now we are gonna add the redirect. Press on Add Redirect and paste: https://yourdomainhere.com/discordauth
AND NOW SAVE IT!!!!!
![opera_f22iKehJjl](https://user-images.githubusercontent.com/70100389/147709654-c2eb9cb7-6e96-4823-8c46-33add2f3a75c.png)
For now, we are done here.

## Installation FLASK API PART 1
This will be very easy
First, open up application.py in there we will need to edit 4 things: CLIENT_ID, CLIENT_SECRET, CLIENT_TOKEN (this is the bot token) , DOMAIN
![Code_0y0g98DHkN](https://user-images.githubusercontent.com/70100389/147709827-a6b63068-7b4b-43ea-be86-09dba949a230.png)

INSERT the things from the discord dashboard

NOW THIS IS VERY IMPORTANT GO INTO database.ini with any text editor and ADD YOUR SERVER ID UNDER guildid
![Code_qLuYfrIB23](https://user-images.githubusercontent.com/70100389/147711090-62a23267-8c57-46b4-9794-cb0534354c3b.png)
```
guildid = 825892582
```


If you want to test some stuff or add some go ahead but be sure to leave a like.
Now save this file.

## Installation Discord bot PART 2
INFO❗: You can make your own discord bot if you want this whole process is API-based so if you want you can even make a telegram bot whatever you wish suits you best.

We are now going to open bot.py
Now we are going to edit 6 things: token(bot token), guild(put your guild ID there), welcome_channel(were new people are getting greeted), memberrole(this is the verified role that will be added after passing verification), 
clientid(From discord dashboard), domain(your domain).

![Code_AzXE5UdUt4](https://user-images.githubusercontent.com/70100389/147710141-6d482942-a5af-48d5-87df-cb13f5ace2de.png)
Now Save this.

We are here now done

## Starting the system
FIRST WERE GONNA INSTALL THE REQUIREMENTS on your flask server/ discord linux server

```bash
pip install -r requirements.txt
```

first, we are gonna make a flask server if you don't know how to [watch this](https://www.youtube.com/watch?v=goToXTC96Co&t=3266s) 


After flask server deployment your gonna run the bot:
```bash
python bot.py
```

Now your all set.
You will need to set your server so you can only see channels if you have the verified role

# Endnote
Please leave a like this took lots of time to code and it wasn't easy.
If you have any questions dm me on discord: 
Ha̶ze#2293

Have fun using this I hope it will help

# Update roadmap
These are the plans what I am trying to add.

- Web GUI for restoring/backuping the members
- Telegram bot For restoring/backuping
- Easier instalation, via batch or via linux instalation file

# Advanced
This is for the PRO coders
You can edit the discordauth HTML template if you want. It is located in the folder template

Also this system is API based so you can also make your own discord bot if you want.
