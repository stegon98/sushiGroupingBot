import psycopg2
import os
import main
from bestemmie import Bestemmie
import functions


def replaceIgnoreCase(text, textToReplace, repl):
    return text.lower().replace(textToReplace.lower(), repl.lower())

def queryBuilder(query, functionName):
    try:
        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgres_insert_query = query
        cursor.execute(postgres_insert_query)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        functions.logUsingPorchiddei("si è spaccato il db!" + error +" Tutta colpa di "+functionName)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def insertData(paramList):
    for id in range(len(paramList)):
        paramList[id] = replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(
            replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(paramList[id], "DROP", ""), "DELETE", ""), "TRUNCATE",
                              ""), "SELECT", ""), "UPDATE", ""), "GRANT", "")

    query = "INSERT INTO t_sushi (telegram_user,name,qty,description) VALUES ('" + paramList[0] + "','" + paramList[1] + "'," + paramList[2] + ",'" + (" " if len(paramList) < 4 else paramList[3] + "')")
    queryBuilder(query, "insertData")


def deleteDish(paramList):
    for id in paramList:
        paramList[id] = replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(
            replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(paramList[id], "DROP", ""), "DELETE", ""), "TRUNCATE",
                              ""), "SELECT", ""), "UPDATE", ""), "GRANT", "")

    query = "DELETE t_sushi WHERE telegram_user='" + paramList[2] + "' AND name='" + paramList[1] + "'"
    queryBuilder(query, "deleteDish")


def deleteTranchee(user):
    user = replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(
        replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(user, "DROP", ""), "DELETE", ""), "TRUNCATE", ""),
        "SELECT", ""), "UPDATE", ""), "GRANT", "")

    query = "DELETE t_sushi WHERE telegram_user='" + user + "'"
    queryBuilder(query, "deleteTranchee")

def updateQty(paramList):
    for id in paramList:
        paramList[id] = replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(
            replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(paramList[id], "DROP", ""), "DELETE", ""), "TRUNCATE",
                              ""), "SELECT", ""), "UPDATE", ""), "GRANT", "")

    query = "UPDATE t_sushi set qty=" + paramList[2] + " WHERE telegram_user='" + paramList[3] + "'" + "name='" + paramList[1] + "'"
    queryBuilder(query, "updateQty")

def removeAll():

    query = "DELETE t_sushi "
    queryBuilder(query, "removeAll")

def getAllDishes():

    try:
        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT name, SUM(qty), MAX(description) FROM t_sushi GROUP BY name, qty "
        cursor.execute(postgreSQL_select_Query)
        orders = cursor.fetchall()
        orderArray = []

        for order in orders:
            orderArray.append(order)
            orderArray.append("\n")

    except (Exception, psycopg2.Error) as error:
        functions.logUsingPorchiddei("si è spaccato il db!" + error + " Tutta colpa della getAll")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def myDishes(user):
    user = replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(
        replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(user, "DROP", ""), "DELETE", ""), "TRUNCATE", ""),
        "SELECT", ""), "UPDATE", ""), "GRANT", "")

    try:
        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT name, qty, MAX(description) FROM t_sushi WHERE telegram_user = '" + user + "'"
        cursor.execute(postgreSQL_select_Query)
        orders = cursor.fetchall()
        orderArray = []

        for order in orders:
            orderArray.append(order)
            orderArray.append("\n")

    except (Exception, psycopg2.Error) as error:
        functions.logUsingPorchiddei("si è spaccato il db!" + error + " Tutta colpa della getAll")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")