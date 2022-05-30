import psycopg2
import os
from bestemmie import Bestemmie
import telegram
from telegram.ext import Updater, CommandHandler

token=os.environ['TOKEN_ID']
chat_ids = set()

def start(update, context):
    chat_id = update.effective_chat.id
    update.message.reply_text("start")
    print("start called from chat with id = {}".format(chat_id))

def add(update, context):
    chat_id = update.effective_chat.id
    update.message.reply_text("add")
    print("adddaaa".format(chat_id))

def end(update, context):
    chat_id = update.effective_chat.id
    chat_ids.remove(chat_id)



def logUsingPorchiddei(error):
    porcone = Bestemmie()
    print(error+" "+porcone.random())


if __name__ == '__main__':
    bot = telegram.Bot(token)
    start
    print(bot.get_me())

    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("end", end))
    updater.dispatcher.add_handler(CommandHandler("add", add))
    updater.start_polling()
    updater.idle()

    try:
        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgres_insert_query = "INSERT INTO t_sushi (telegram_user,name,qty,description) VALUES ('"+telegramUser+"','"+dishNum+"',"+dishCount+",'"+dishDescr+"')"
        cursor.execute(postgres_insert_query)
        connection.commit()
    except:
        logUsingPorchiddei("errore contattando il db")