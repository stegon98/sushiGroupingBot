import psycopg2
import os
from bestemmie import Bestemmie
import telegram
from telegram.ext import Updater, CommandHandler
import database

token = os.environ['TOKEN_ID']
chat_ids = set()

def extract_number(text, username):
    paramList=[]
    for i in range(len(text.split())):
        if(i == 0):
            paramList.append(username)
        elif(i>0 & text.split()[i].strip() != "/add"):
            paramList.append(text.split()[i].strip())

    database.insertData(paramList)

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
#
# TODO: implementare le query per le seguenti istruzioni da db
#
def myDishes(update, context):
    # funzione che estrarra solo i piatti ordinati da un utente
    user = update.message.from_user
    database.getMyDishes(user["username"])

def allDishes(update, context):
    # funzione che estrarra tutti i piatti ordinati
    database.geAllDishes()

def removeDish(update, context):
    # funzione per la rimozione del piatto inserito
    database.removeDish()

def removeAllDishes(update, context):
    # funzione per rimuovere tutti i piatti di un utente
    database.removeAllDishes()

def removeAll(update, context):
    # funzione di cancellazione di tutti i piatti
    database.removeAll()

if __name__ == '__main__':
    bot = telegram.Bot(token)
    print(bot.get_me())
    database.insertData(["stegon","94","2","sashimi"])
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("end", end))
    updater.dispatcher.add_handler(CommandHandler("add", add))
    updater.dispatcher.add_handler(CommandHandler("myDishes", myDishes))
    updater.dispatcher.add_handler(CommandHandler("allDishes", allDishes))
    updater.dispatcher.add_handler(CommandHandler("remove", removeDish))
    updater.dispatcher.add_handler(CommandHandler("removeAll", removeAllDishes))
    updater.dispatcher.add_handler(CommandHandler("truncate", removeAll))
    updater.start_polling()
    updater.idle()
