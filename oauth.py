import logging
import requests
import os
import configparser
from setupfile import *


config = configparser.ConfigParser()
config.read('database.ini')


discordtoken = input("Enter your discord token: ")

##############################
logging.basicConfig(
    level=logging.INFO,
    format="\t[%(asctime)s]  > %(message)s",
    datefmt="%H:%M:%S",
)
##############################
class CreateOauth:
    name = ""
    domain = ""
    session = requests.Session()
    baseurl = "https://discord.com/api/v9/applications"
    payload = {"name": "Member Backup"}
    headers = {
    "Authorization":
    f"{discordtoken}",
    "accept":
    "*/*",
    "accept-language":
    "en-US",
    "connection":
    "keep-alive",
    "cookie":
    f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
    "DNT":
    "1",
    "origin":
    "https://discord.com",
    "sec-fetch-dest":
    "empty",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-site":
    "same-origin",
    "referer":
    "https://discord.com/channels/@me",
    "TE":
    "Trailers",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
    "X-Super-Properties":
    "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

    @classmethod
    def set_info(cls, domain):
        cls.domain = domain

    @classmethod
    def create_app(cls):
        r = cls.session.post(cls.baseurl, json = cls.payload, headers = cls.headers)
        if r.status_code in (200, 201, 204):
            logging.info("Created Application")
            skid = r.json()
            botid = skid['id']
            return botid
        else:
            logging.error("Something Went Wrong!")

    @classmethod
    def enable_intents(cls, id: str):
        p = cls.session.patch(f"{cls.baseurl}/{id}", json = {"bot_public":"true","bot_require_code_grant":"false","flags":40960}, headers = cls.headers)
        if p.status_code in (200, 201, 204):
            logging.info("Added Intents")
            cls.add_oauth_redirect(id)
        else:
            logging.error("Something Went Wrong!")

    @classmethod
    def add_oauth_redirect(cls, id: str):
        o =  cls.session.patch(f"{cls.baseurl}/{id}", json = {"redirect_uris":[cls.domain]}, headers = cls.headers)
        if o.status_code in (200, 201, 204):
            logging.info("Added Domain To OAUTH Redirect")
            toekn = cls.get_token(id)
            secrt = cls.get_client_secret(id)
            config['botinfo']['bottoken'] = toekn
            config['apiinfo']['CLIENT_ID'] = id
            config['apiinfo']['CLIENT_SECRET'] = secrt
            with open('database.ini', 'w') as configfile:
                config.write(configfile)
            logging.info("Added Token To Database")
            
        else:
            logging.error("Something Went Wrong!")


    @classmethod
    def create_bot(cls):
        id = cls.create_app()
        endpoint = "/bot"
        t = cls.session.post(f"{cls.baseurl}/{id}{endpoint}", headers = cls.headers)
        if t.status_code in (200, 201, 204):
            logging.info("Created Bot")
            cls.enable_intents(id)
        elif t.status_code == 429:
            logging.error("Ratelimited")

    @classmethod
    def get_token(cls, id: str):
        tok = cls.session.post(f"{cls.baseurl}/{id}/bot/reset", headers = cls.headers)
        token = tok.json()['token']
        return token

    @classmethod
    def get_client_secret(cls, id: str):
        sec = cls.session.post(f"{cls.baseurl}/{id}/reset", headers = cls.headers)
        secret = sec.json()['secret']
        return secret

    @classmethod
    def main(cls):
        try:
            cls.create_bot()
            logging.info("Succesfully Setup Bot Application On Developer Page!")
        except Exception as e:
            print(e)
            pass


def startoauthdata(domaintogowith):
    url = domaintogowith + '/discordauth'
    CreateOauth.set_info(url)
    CreateOauth.main()
