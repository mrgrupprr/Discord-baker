import configparser
import requests
from telegram.ext import Updater, CommandHandler

config = configparser.ConfigParser()
config.read('database.ini')

token = config['telegram'].get('TOKEN', 'your-telegram-token')
domain = config['apiinfo']['DOMAIN']
api_key = config['apiinfo']['exchangepass']


def backup(update, context):
    r = requests.post(f"{domain}/backup", json={"key": api_key})
    update.message.reply_text(r.text)


def restore(update, context):
    r = requests.post(f"{domain}/restore", json={"code": api_key})
    update.message.reply_text(r.text)


def main():
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("backup", backup))
    dp.add_handler(CommandHandler("restore", restore))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
