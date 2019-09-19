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

city_game_config = dict()

with open('bot_token.txt') as f:
    token = f.read()

def talk_to_me(bot, update):
    upd = update
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

def wordcount(bot, update):
    text = update.message.text.replace('/wordcount','').replace('-','').strip()

    words = 0
    for word in text.split():
        if len(list(filter(lambda x: x.isalpha(), word))) == len(word):
            words += 1
            print(word)
    update.message.reply_text(f'В строке "{text}" {words} слов')     

def next_full_moon(bot, update):
    text_list = update.message.text.split()    
    text = text_list[-1]  
    try:
        date = datetime.datetime.strptime(text, '%Y-%m-%d')
        update.message.reply_text(str(ephem.next_full_moon(date)))
    except ValueError as e:
#         update.message.reply_text(str(e))
        update.message.reply_text("Cannot understand date. Try something like /next_full_moon 2019-01-01")

def init_city_game(bot, update):
    with open('cities') as f:
        city_list = f.read().lower()
    city_list = city_list.split(',')
    username = update.message.chat.username
    city_game_config[username] = {'cities_whitelist':city_list, 'last_letter': 'any', 'cities_blacklist':[]}
    print(3)
    update.message.reply_text("Created new game.\n To create new game type /init_city_game \n To check your city letter type /remind_city_game \n To make your move type /m 'city'")

def remind_city_game(bot, update):
    username = update.message.chat.username
    if username in city_game_config.keys():
        letter = city_game_config[username].get('last_letter', 'somthing go wrong init new game')
        update.message.reply_text(f"Your word should be on letter '{letter}'")
    else:
        update.message.reply_text("Cannot find current game. Init new game with /init_city_game")
        
def m(bot, update):
    username = update.message.chat.username
    if username not in city_game_config.keys():
        update.message.reply_text("Can't find current game. Intit new game with /init_city_game")
        return

    whitelist = city_game_config[username]['cities_whitelist']
    blacklist = city_game_config[username]['cities_blacklist']
    last_letter = city_game_config[username]['last_letter']
    user_city = update.message.text.replace('/m','').lower().strip()
    update.message.reply_text(f'Your city is "{user_city}"')
    if len(user_city) == 0:
        update.message.reply_text(f'There is no city "{user_city}"')    
        return
    if user_city in whitelist and (user_city[0] == last_letter or last_letter == 'any'):
        update.message.reply_text('Your city is ok')
        for letter in 'ьъыё':
            user_city = user_city.replace(letter,'')
        last_letter = user_city[-1]
        answer = list(filter(lambda x: x.startswith(last_letter), whitelist))
        if len(answer) == 0:
            update.message.reply_text('You won!')
            with open('cities') as f:
                city_list = f.read().lower()
            city_list = city_list.split(',')
            city_game_config[username] = {'cities_whitelist':city_list, 'last_letter': 'any', 'cities_blacklist':[]}
        else:
            answer = answer[0]
            update.message.reply_text(f'My city is {answer}')
            city_game_config[username]['cities_whitelist'].remove(answer)
            city_game_config[username]['cities_blacklist'].append(answer)
            for letter in 'ьъыё':
                user_city = answer.replace(letter,'')
            city_game_config[username]['last_letter'] = answer[-1]
            update.message.reply_text(f'You shiuld type city on "{answer[-1]}"')                              
    elif user_city in whitelist and user_city[0] != last_letter:
        update.message.reply_text(f'You should type city on {last_letter}')
    elif user_city in blacklist:
        update.message.reply_text(f'We already used "{user_city}"')    
    else:
        update.message.reply_text(f'There is no city "{user_city}"')    
                              
                              
                              
def main():
    mybot = Updater(token, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))    
    dp.add_handler(CommandHandler("init_city_game", init_city_game))
    dp.add_handler(CommandHandler("remind_city_game", remind_city_game))
    dp.add_handler(CommandHandler("m", m))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
    
    
main()