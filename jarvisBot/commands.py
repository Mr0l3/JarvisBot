#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.constants import PARSEMODE_HTML

def send_message(update, context, msg, parse_HTML = False) -> None:
    if parse_HTML:
        context.bot.send_message(chat_id=update.effective_chat.id, text = msg, parse_mode = PARSEMODE_HTML)
    else: 
        context.bot.send_message(chat_id=update.effective_chat.id, text = msg)


def c_bot(update, context) -> None:
    # /bot
    send_message(update, context, 'Hello there! I\'m JarvisBot, a bot for group management.\n\nFor a list of commands, type /commands')


def c_commands(update, context) -> None:
    # /commands
    send_message(update, context, 'Command list for JarvisBot:\n/bot - Display general info about the bot\n/commands - Display a list of commands\n/lyrics - Display the lyrics of a song')


def c_kick(update, context) -> None:
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


def kick_member(bot, chat_id, user_id) -> int:
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
