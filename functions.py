import telegram
from telegram.ext import Updater, CommandHandler
from bestemmie import Bestemmie
import database
import json

chat_ids = set()

def extract_number(text, username):
    paramList = []
    for i in range(len(text.split())):
        if (i == 0):
            paramList.append(username)
        elif (i > 0 & text.split()[i].strip() != "/add"):
            paramList.append(text.split()[i].strip())

    database.insertData(paramList)


def logUsingPorchiddei(error):
    porcone = Bestemmie()
    print(error + " " + porcone.random())


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
    extract_number(update.message.text, user["username"])

def myDishes(update, context):
    # funzione che estrarra solo i piatti ordinati da un utente
    user = update.message.from_user
    dishes = database.myDishes(user["username"])
    for dish in dishes:
        print(dish)

    update.message.reply_text("I tuoi piatti " + user["username"] + " sono i seguenti: \n" + dishes)

def allDishes(update, context):
    dishes = database.getAllDishes()
    update.message.reply_text("I piatti di tutti sono i seguenti: \n" + dishes)

def removeDish(update, context):
    user = update.message.from_user
    paramlist=[]
    paramlist.append(update.message.text)
    paramlist.append(user)
    database.deleteDish(paramlist)

def removeAllDishes(update, context):
    user = update.message.from_user
    database.deleteTranchee(user["username"])

def removeAll(update, context):
    user = update.message.from_user
    username = user["username"]

    if username.lower() in ("edoshin98", "stegon98"):
        database.removeAll()
    else:
        update.message.reply_text("Eh volevih!")


def updateQty(update, context):
    user = update.message.from_user
    paramlist = []
    paramlist.append(update.message.text)
    paramlist.append(user)
    database.updateQty(paramlist)

def getHelp(update, context):
    text = {{"name": "", "description": ""}}
    functions = [
        "/add",
        "/myDishes"
        "/allDishes",
        "/remove",
        "/removeAll",
        "/truncate",
        "/updateQuantity"
    ]

    descriptions = [
        "Comando per aggiungere un piatto (formato OBBLIGATORIO: numero del piatto quantita evventuale descrizione) " +
        "\nMirko ti tengo d'occhio",
        "Comando per vedere i piatti che ho ordinato",
        "Comando per vedere tutti i piatti ordinati da tutti",
        "Comando per togliere un piatto da inserire numero del piatto dopo il comando... EX: /remove 11b",
        "Comando per rimuovere l'intera lista di piatti ordinati",
        "Comando per i veri pro (io e ste) NON USARE",
        "Comando per modificare la quantità dell'ordine. Da passare nome piatto e nuova quantità... " +
        "\nEX: /updateQuantity 11b 10"

    ]

    for function in functions:
        text["name"] = function

    for description in descriptions:
        text["description"] = description

    update.message.reply_text(text)
