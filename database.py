import psycopg2
import os
import main
from bestemmie import Bestemmie

def replaceIgnoreCase(text,textToReplace,repl):
    return text.lower().replace(textToReplace.lower(),repl.lower())

def insertData(paramList):

    for id in paramList:
        paramList[id]=replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(paramList[id],"DROP",""),"DELETE",""),"TRUNCATE",""),"SELECT",""),"UPDATE",""),"GRANT","")

    try:
        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgres_insert_query = "INSERT INTO t_sushi (telegram_user,name,qty,description) VALUES ('"+paramList[0]+"','"+paramList[1]+"',"+paramList[2]+",'"+" "  if len(paramList)<3  else paramList[3] +"')"
        cursor.execute(postgres_insert_query)
        connection.commit()
    except:
        main.logUsingPorchiddei("si è spaccato il db ")