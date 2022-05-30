import psycopg2
import os
from bestemmie import Bestemmie
import telegram

token=os.environ['TOKEN_ID']

def logUsingPorchiddei(error):
    porcone = Bestemmie()
    print(error+" "+porcone.random())


if __name__ == '__main__':
    bot = telegram.Bot(token)

    print(bot.get_me())
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