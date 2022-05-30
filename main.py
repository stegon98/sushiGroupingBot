import psycopg2
import os
import json
from bestemmie import Bestemmie
import telegram
from telegram.ext import Updater, CommandHandler
import database

token = os.environ['TOKEN_ID']
chat_ids = set()

class Order:
  def __init__(mysillyobject, username, parameters):
    mysillyobject.username = username
    mysillyobject.parameters = parameters

  def insertOrder(order):
    print("Hello my name is " + order.username +" "+order.parameters[1])

def extract_number(text, username):
    paramList=[]
    for i in range(len(text.split())):
        paramList.append(text.split()[i].strip())

    order=Order(username, paramList)

    order.insertOrder()

def logUsingPorchiddei(error):
    porcone = Bestemmie()
    print(error+" "+porcone.random())

def start(update, context):
    chat_id = update.effective_chat.id
    bestemmione = Bestemmie()
    update.message.reply_text("Sono su " + bestemmione.random())
    print("start called from chat with id = {}".format(chat_id))

def add(update, context):
    chat_id = update.effective_chat.id
    user = update.message.from_user
    update.message.reply_text("Sto aggiungendo tutto")
    extract_number(update.message.text, user["username"])
    
def end(update, context):
    chat_id = update.effective_chat.id
    chat_ids.remove(chat_id)


if __name__ == '__main__':
    bot = telegram.Bot(token)
    print(bot.get_me())
    database.insertData(["DROP TABLE BANANA;TRUNCATE TABLE SI;SELECT * FROM DUAL"])
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("end", end))
    updater.dispatcher.add_handler(CommandHandler("add", add))
    updater.start_polling()
    updater.idle()
