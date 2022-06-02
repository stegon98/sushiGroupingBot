import psycopg2
import os
import telegram
from telegram.ext import Updater, CommandHandler
import functions

token = os.environ['TOKEN_ID']


if __name__ == '__main__':
    bot = telegram.Bot(token)
    print(bot.get_me())
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", functions.start))
    updater.dispatcher.add_handler(CommandHandler("end", functions.end))
    updater.dispatcher.add_handler(CommandHandler("add", functions.add))
    updater.dispatcher.add_handler(CommandHandler("a", functions.add))
    updater.dispatcher.add_handler(CommandHandler("myDishes", functions.myDishes))
    updater.dispatcher.add_handler(CommandHandler("allDishes", functions.allDishes))
    updater.dispatcher.add_handler(CommandHandler("remove", functions.removeDish))
    updater.dispatcher.add_handler(CommandHandler("rm", functions.removeDish))
    updater.dispatcher.add_handler(CommandHandler("removeAll", functions.removeAllDishes))
    updater.dispatcher.add_handler(CommandHandler("truncate", functions.removeAll))
    updater.dispatcher.add_handler(CommandHandler("updateQuantity", functions.updateQty))
    updater.dispatcher.add_handler(CommandHandler("uq", functions.updateQty))
    updater.dispatcher.add_handler(CommandHandler("help", functions.getHelp))
    updater.dispatcher.add_handler(CommandHandler("wo", functions.whoOrdered))
    updater.dispatcher.add_handler(CommandHandler("whoOrdered", functions.whoOrdered))
    updater.start_polling()
    updater.idle()
