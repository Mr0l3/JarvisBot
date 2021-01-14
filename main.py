#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def send_message(update, context, msg):
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def c_bot(update, context):
    # /bot
    send_message(update, context, 'Hello there! I\'m JarvisBot, a bot for group management.\n\nFor a list of commands, type /commands')


def c_commands(update, context):
    # /commands 
    send_message(update, context, 'Command list for JarvisBot:\n/bot - Display general info about the bot\n/commands - Display a list of commands\n/lyrics - Display the lyrics of a song')

def c_lyrics(update, context):
    # /lyrics [artist]; [song-name]
    args = ' '.join(context.args)

    if len(args) > 1:
        artist = ''
        for l in args:
            # Remove the first character on each iteration
            args = args[1:]

            if l == ';':
                break;
            artist += l
        
        # Remove extra space on index 0
        song = args[1:].title()

        artist = artist.title()

        rq = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{song}')
        lyrics = rq.json()['lyrics'].strip()
        if lyrics:
            msg = f'{artist} - {song}\n\n{lyrics}'
        else:
            msg = 'Lyrics not found'
    else:
        msg = 'Usage: /lyrics artist; song-name\nExample: /lyrics drake; god\'s plan'

    send_message(update, context, msg)

def c_kick(update, context):
    chat_id = update.message.chat_id
    prev_msg = update.message.reply_to_message
    
    if not prev_msg:
        msg = 'Usage: reply to a message of the user you want to kick with /kick'
    else:
        user_id = prev_msg.from_user.id
        bot = context.bot
        code = kick_member(bot, chat_id, user_id)

        if code == 1:
            msg = 'User kicked succesfully. Good bye, bitch!'
        elif code == -1:
            msg = 'Couldn\'t kick the user'
        elif code == -2:
            msg = 'Not enough rights to kick chat member'
        elif code == -3:
            msg = 'User is an administrator of the chat'
        else:
            msg = 'Unknown error'

    send_message(update, context, msg)

def kick_member(bot, chat_id, user_id):
    return_code = 0
    try:
        user_data = bot.getChatMember(chat_id, user_id)
        if (user_data['status'] != "left") and (user_data['status'] != "kicked"):
            bot.kickChatMember(chat_id, user_id)
            bot.unbanChatMember(chat_id, user_id)
            return_code = 1
        else:
            return_code = -1
    except Exception as e:
        if str(e) == "Not enough rights to restrict/unrestrict chat member":
            return_code = -2
        elif str(e) == "User is an administrator of the chat":
            return_code = -3
    
    return return_code
        

def error(update, context):
    #Log Errors caused by Updates.
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater('1558636323:AAH3E_r8BwuXn5m-ta2Ow10bgoxM-K2hQ80', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('bot', c_bot))
    dp.add_handler(CommandHandler('commands', c_commands))
    dp.add_handler(CommandHandler('lyrics', c_lyrics, run_async = True))
    dp.add_handler(CommandHandler('kick', c_kick, run_async = True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Stop the bot grecefully. Do not remove this shit!
    updater.idle()


if __name__ == '__main__':
    main()