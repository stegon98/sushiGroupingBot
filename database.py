import psycopg2
import os
import main
from bestemmie import Bestemmie

def replaceIgnoreCase(text,textToReplace,repl):
    return text.lower().replace(textToReplace.lower(),repl.lower())

def insertData(paramList):

    for id in range(len(paramList)):
        paramList[id]=replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(paramList[id],"DROP",""),"DELETE",""),"TRUNCATE",""),"SELECT",""),"UPDATE",""),"GRANT","")

    try:
        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgres_insert_query = "INSERT INTO t_sushi (telegram_user,name,qty,description) VALUES ('"+paramList[0]+"','"+paramList[1]+"',"+paramList[2]+",'"+(" "  if len(paramList)<4  else paramList[3] +"')")
        print(postgres_insert_query)
        cursor.execute(postgres_insert_query)
        connection.commit()
    except RuntimeError as err:
        main.logUsingPorchiddei(err+"si è spaccato il db ")

def deleteDish(paramList):

    for id in paramList:
        paramList[id]=replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(paramList[id],"DROP",""),"DELETE",""),"TRUNCATE",""),"SELECT",""),"UPDATE",""),"GRANT","")

    try:
        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgres_insert_query = "DELETE t_sushi WHERE telegram_user='"+paramList[1]+"' AND name='"+paramList[2]+"'"
        cursor.execute(postgres_insert_query)
        connection.commit()
    except:
        main.logUsingPorchiddei("si è spaccato il db ")

def deleteTranchee(paramList):

    for id in paramList:
        paramList[id]=replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(paramList[id],"DROP",""),"DELETE",""),"TRUNCATE",""),"SELECT",""),"UPDATE",""),"GRANT","")

    try:
        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgres_insert_query = "DELETE t_sushi WHERE telegram_user='"+paramList[1]+"'"
        cursor.execute(postgres_insert_query)
        connection.commit()
    except:
        main.logUsingPorchiddei("si è spaccato il db ")

def updateQty(paramList):

    for id in paramList:
        paramList[id]=replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(paramList[id],"DROP",""),"DELETE",""),"TRUNCATE",""),"SELECT",""),"UPDATE",""),"GRANT","")

    try:
        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgres_insert_query = "UPDATE t_sushi set qty="+paramList[3]+" WHERE telegram_user='"+paramList[1]+"'" +"name='"+paramList[2]+"'"
        cursor.execute(postgres_insert_query)
        connection.commit()
    except:
        main.logUsingPorchiddei("si è spaccato il db ")