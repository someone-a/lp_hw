from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import ephem
import datetime
dttm = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )



PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

with open('bot_token.txt') as f:
    token = f.read()

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
    
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planet(bot, update):
    text_list = update.message.text.split()
    if len(text_list) == 1:
        update.message.reply_text('Try message like')
        update.message.reply_text("/planet Mars")
        return
    else:
        text = text_list[-1]
    try:
        dttm = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        planet = getattr(ephem ,text.lower().capitalize())
        update.message.reply_text(f'Current constellation of {text} is {ephem.constellation(planet(dttm))}')
    except Exception as e:
        update.message.reply_text(f"Can't get constellation of {text} Try message like")
        update.message.reply_text("/planet Mars")
#         update.message.reply_text(f"error is {e}")
     
    
def main():
    print(1)
    mybot = Updater(token, request_kwargs=PROXY)
    print(2)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))    
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    print(3)    
    mybot.start_polling()
    mybot.idle()
    
    
main()