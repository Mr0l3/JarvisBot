#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import commands


class Bot:
    __TOKEN = 'TOKEN HERE'
    __updater: Updater
    __logger: logging

    def __init__(self) -> None:
        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.__logger = logging.getLogger(__name__)

        # start updater
        self.updater = Updater(self.__TOKEN, use_context=True)

        # Get the dispatcher to register handlers
        dp = self.updater.dispatcher

        dp.add_handler(CommandHandler('bot', commands.c_bot))
        dp.add_handler(CommandHandler('commands', commands.c_commands))
        dp.add_handler(CommandHandler('lyrics', commands.c_lyrics, run_async=True))
        dp.add_handler(CommandHandler('kick', commands.c_kick, run_async=True))

        # log all errors
        dp.add_error_handler(self.error)

    def error(self, update, context) -> None:
        # Log Errors caused by Updates.
        self.__logger.warning(
            'Update "%s" caused error "%s"', update, context.error)

    def startBot(self) -> None:
        # Start the Bot
        self.updater.start_polling()

        # Stop the bot grecefully. Do not remove this shit!
        self.updater.idle()
