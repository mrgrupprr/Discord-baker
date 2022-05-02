import subprocess
import os
import configparser
import string
import random
from oauth import *
config = configparser.ConfigParser()
config.read('database.ini')

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def mainmenu():
    cls()
    print("")
    print("Welcome to the main menu.")
    print("")
    print("For proper installation be sure to run the setup file in the same folder as the downloaded files!")
    print("")
    print("Please select an option.")

    print("""
    1. Fully automated setup
    2. Manual setup
    2. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        autosetup()
    if choice == "2":
        setup()
    elif choice == "2":
        exit()



def passwordgenerator():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(18))

def fetchurlcorectly(domaintogo):
    domainwithoutslash = domaintogo[:-1]
    if domaintogo.endswith('/'):
        return domainwithoutslash
    else:
        return domaintogo



def autosetup():
    checkfile1 = os.path.exists('application.py')
    checkfile2 = os.path.exists('database.ini')
    checkfile3 = os.path.exists('requirements.txt')
    if checkfile1 == True:
        pass
    else:
        print("The application.py file is missing.")
        print("Please download the file and place it in the same folder as this file.")
        type = input('Press enter to continue')
        exit()
    if checkfile2 == True:
        pass
    else:
        print("The database.ini file is missing.")
        print("Please download the file and place it in the same folder as this file.")
        type = input('Press enter to continue')
        exit()
    if checkfile3 == True:
        pass
    else:
        print("The requirements.txt file is missing.")
        print("Please download the file and place it in the same folder as this file.")
        type = input('Press enter to continue')
        exit()
    cls()
    domain = input("Enter your FLASK domain/ip: ")
    welcomechannel = input("Enter the welcome channel ID: ")
    memberrole = input("Enter the member role ID: ")
    therestorekey = input("Enter the restore key used to restore backups: ")
    guildid = input("Enter the guild ID: ")
    config['apiinfo']['DOMAIN'] = fetchurlcorectly(domain)
    config['botinfo']['welcome_channel'] = welcomechannel
    config['botinfo']['memberrole'] = memberrole
    config['botinfo']['therestorekey'] = therestorekey
    config['info']['guildid'] = guildid
    config['apiinfo']['exchangepass'] = passwordgenerator()
    config['apiinfo']['tempkey'] = passwordgenerator()
    with open('database.ini', 'w') as configfile:
        config.write(configfile)
    startoauthdata(fetchurlcorectly(domain))
    print("")
    print("Changes were saved now starting installing do you want to continue?  (y/n)")
    print("")
    choice = input("Enter your choice: ")
    if choice == "y":
        install()
    elif choice == "n":
        exit()


def setup():
    checkfile1 = os.path.exists('application.py')
    checkfile2 = os.path.exists('database.ini')
    checkfile3 = os.path.exists('requirements.txt')
    if checkfile1 == True:
        pass
    else:
        print("The application.py file is missing.")
        print("Please download the file and place it in the same folder as this file.")
        type = input('Press enter to continue')
        exit()
    if checkfile2 == True:
        pass
    else:
        print("The database.ini file is missing.")
        print("Please download the file and place it in the same folder as this file.")
        type = input('Press enter to continue')
        exit()
    if checkfile3 == True:
        pass
    else:
        print("The requirements.txt file is missing.")
        print("Please download the file and place it in the same folder as this file.")
        type = input('Press enter to continue')
        exit()
    cls()
    cls()
    print("")
    print("Welcome to the setup.")
    print("")
    print("Please enter the following information.")
    print("")
    print("")
    clientid = input("Enter Client ID from the discord developer dashboard: ")
    clientsecret = input("Enter Client Secret from the discord developer dashboard: ")
    bottoken = input("Enter your Bot token: ")
    domain = input("Enter your FLASK domain/ip: ")
    welcomechannel = input("Enter the welcome channel ID: ")
    memberrole = input("Enter the member role ID: ")
    therestorekey = input("Enter the restore key used to restore backups: ")
    guildid = input("Enter the guild ID: ")
    print("")
    print("")
    cls()
    print("Please wait while we save all of the changes!")
    print("")
    config['apiinfo']['CLIENT_ID'] = clientid
    config['apiinfo']['CLIENT_SECRET'] = clientsecret
    config['apiinfo']['DOMAIN'] = fetchurlcorectly(domain)
    config['botinfo']['bottoken'] = bottoken
    config['botinfo']['welcome_channel'] = welcomechannel
    config['botinfo']['memberrole'] = memberrole
    config['botinfo']['therestorekey'] = therestorekey
    config['info']['guildid'] = guildid
    config['apiinfo']['exchangepass'] = passwordgenerator()
    config['apiinfo']['tempkey'] = passwordgenerator()
    with open('database.ini', 'w') as configfile:
        config.write(configfile)
    print("")
    print("Changes were saved now starting installing do you want to continue?  (y/n)")
    print("")
    choice = input("Enter your choice: ")
    if choice == "y":
        install()
    elif choice == "n":
        exit()

def install():
    try:
        subprocess.call('pip install -r requirements.txt', shell=True)
    except:
        try:
            subprocess.call('pip3 install -r requirements.txt', shell=True)
        except:
            try:
                subprocess.call('python pip install -r requirements.txt', shell=True)
            except:
                try:
                    subprocess.call('python3 pip install -r requirements.txt', shell=True)
                except:
                        try:
                            subprocess.call('py pip install -r requirements.txt', shell=True)
                        except:
                            print("Could not install requirements.txt")
                            print("Error installing requirements please try manually.")
                            exit()
    print("Requirements installed")
    print("")
    print("Do you want to start the API?")
    print("")
    print("(y/n)")
    print("")
    choice = input("Enter your choice: ")
    if choice == "y":
        try:
            subprocess.call('python application.py', shell=True)
        except:
            print("Failed to execute please start manually.")
            typetocon = input("Please Press enter to continue")
            exit()
    elif choice == "n":
        exit()



if __name__ == '__main__':
    mainmenu()
