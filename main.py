import psycopg2
import os
from bestemmie import Bestemmie
import telegram
from telegram.ext import Updater, CommandHandler

token=os.environ['TOKEN_ID']
chat_ids = set()


def extract_number(text):
    paramList=[]
    for i in range(len(text.split())):
        param=text.split()[i].strip()
        print(param)

def logUsingPorchiddei(error):
    porcone = Bestemmie()
    print(error+" "+porcone.random())

def start(update, context):
    chat_id = update.effective_chat.id
    update.message.reply_text("start")
    print("start called from chat with id = {}".format(chat_id))

def add(update, context):
    chat_id = update.effective_chat.id
    update.message.reply_text("add")
    extract_number(update.message.text)
    
def end(update, context):
    chat_id = update.effective_chat.id
    chat_ids.remove(chat_id)


if __name__ == '__main__':
    bot = telegram.Bot(token)
    print(bot.get_me())

    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("end", end))
    updater.dispatcher.add_handler(CommandHandler("add", add))
    updater.start_polling()
    updater.idle()
