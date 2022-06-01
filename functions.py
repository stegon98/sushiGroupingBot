import telegram
from telegram.ext import Updater, CommandHandler
from bestemmie import Bestemmie
import database
import main

chat_ids = set()

def extract_number(text, username):
    paramList = []
    paramList.append(username)
    for i in range(len(text.split())):
        paramList.append(text.split()[i].strip())

    return paramList


def logUsingPorchiddei(error):
    porcone = Bestemmie()
    print(error + " " + porcone.random())

def estraiUnPorchiddeo():
    porcone = Bestemmie()
    return porcone.random()


def start(update, context):
    chat_id = update.effective_chat.id
    bestemmione = Bestemmie()
    update.message.reply_text("Sono su " + bestemmione.random())
    print("start called from chat with id = {}".format(chat_id))


def end(update, context):
    chat_id = update.effective_chat.id
    chat_ids.remove(chat_id)

def add(update, context):
    chat_id = update.effective_chat.id
    user = update.message.from_user
    update.message.reply_text("Sto aggiungendo tutto")
    database.insertData(extract_number(update.message.text, user["username"]))

def myDishes(update, context):
    # funzione che estrarra solo i piatti ordinati da un utente
    user = update.message.from_user
    dishes = database.myDishes(user["username"])
    message=""
    for dish in dishes:
        message=message+dish

    update.message.reply_text("I tuoi piatti " + user["username"] + " sono i seguenti: \n" + message)

def allDishes(update, context):
    dishes = database.getAllDishes()
    message=""
    for dish in dishes:
        message=message+dish
    update.message.reply_text("I piatti di tutti sono i seguenti: \n" + message)

def removeDish(update, context):
    user = update.message.from_user
    database.deleteDish(extract_number(update.message.text, user["username"]))
    update.message.reply_text("Piatto " + params[2] + " rimosso")


def removeAllDishes(update, context):
    user = update.message.from_user
    database.deleteTranchee(user["username"])
    update.message.reply_text("Piatti rimossi")

def removeAll(update, context):
    user = update.message.from_user
    username = user["username"]

    if username.lower() in ("edoshin98", "stegon998"):
        database.removeAll()
        update.message.reply_text("Tabella svuotata")

    else:
        photo = open("./volevi.gif")
        bot = telegram.Bot(main.token)
        bot.send_animation(update.effective_chat.id, photo)


def updateQty(update, context):
    user = update.message.from_user
    database.updateQty(extract_number(update.message.text, user["username"]))
    update.message.reply_text("Quantità del piatto: " + params[2] + " portata a: " + params[3])

def getHelp(update, context):
    messagge = "/add o /a Comando per aggiungere un piatto (formato OBBLIGATORIO: numero del piatto quantita evventuale descrizione) Mirko ti tengo d'occhio\n\n"+ \
               "/myDishes Comando per vedere i piatti che ho ordinato\n\n"+\
               "/allDishes Comando per vedere tutti i piatti ordinati da tutti\n\n"+\
               "/remove o /rm Comando per togliere un piatto da inserire numero del piatto dopo il comando... EX /remove 11b\n\n"+\
               "/removeAll Comando per rimuovere l'intera lista di piatti ordinati\n\n"+\
               "/truncate Comando per i veri pro (io e ste) NON USARE\n\n"+\
               "/updateQuantity /uq Comando per modificare la quantita dell'ordine. Da passare nome piatto e nuova quantita... EX /updateQuantity 11b 10\n"

    update.message.reply_text(messagge)
