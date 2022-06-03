import psycopg2
import os
import main
from bestemmie import Bestemmie
import functions
#provacommit


def replaceIgnoreCase(text, textToReplace, repl):
    return text.lower().replace(textToReplace.lower(), repl.lower())

def avoidSqlInjectionSingleParam(paramList):
    paramList=replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(
        replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(paramList, "DROP", ""), "DELETE", ""), "TRUNCATE",
                          ""), "SELECT", ""), "UPDATE", ""), "CREATE", ""), "ALTER", ""), "LIKE", ""), "=", ""), "AAAAAAAAAAAAAAAAAAAAA", "")
    return paramList

def avoidSqlInjection(paramList):
    for id in range(len(paramList)):
        paramList[id]=replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(
            replaceIgnoreCase(replaceIgnoreCase(replaceIgnoreCase(paramList[id], "DROP", ""), "DELETE", ""), "TRUNCATE",
                              ""), "SELECT", ""), "UPDATE", ""), "CREATE", ""), "ALTER", ""), "LIKE", ""), "=", ""), "AAAAAAAAAAAAAAAAAAAAA", "")
    return paramList

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
        functions.logUsingPorchiddei("si è spaccato il db!" + str(error) +" Tutta colpa di "+str(functionName))

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insertData(paramList):
    try:
        paramList = avoidSqlInjection(paramList)
        if(paramList[3].isalpha() and len(paramList)<5):
            paramList.append(paramList[3])
            paramList[3]="1"
        if len(paramList) == 5 and paramList[4]=="bb":
            paramList[4]= (functions.estraiUnPorchiddeo()).replace("'"," ")
        query = "INSERT INTO t_sushi (telegram_user,name,qty,description) VALUES ('" + paramList[0] + "','" + paramList[2] + "'," + paramList[3] + ",'" + ("') " if len(paramList) < 5 else paramList[4] + "')")
        queryBuilder(query, "insertData")
        return 0
    except:
        return -1

def deleteDish(paramList):
    try:
        paramList=avoidSqlInjection(paramList)

        query = "DELETE from t_sushi WHERE telegram_user='" + paramList[0] + "' AND name='" + paramList[2] + "'"
        queryBuilder(query, "deleteDish")
        return 0
    except:
        return -1


def deleteTranchee(user):
    try:
        user=avoidSqlInjectionSingleParam(user, 1)

        query = "DELETE from t_sushi WHERE telegram_user='" + user + "'"
        queryBuilder(query, "deleteTranchee")
        return 0
    except:
        return -1

def updateQty(paramList):
    try:
        paramList = avoidSqlInjection(paramList)

        query = "UPDATE t_sushi set qty=" + paramList[3] + " WHERE telegram_user='" + paramList[0] + "'" + " AND name='" + paramList[2] + "'"
        queryBuilder(query, "updateQty")
        return 0
    except:
        return -1

def removeAll():
    try:
        query = "DELETE from t_sushi "
        queryBuilder(query, "removeAll")
        return 0
    except:
        return -1

def getAllDishes():

    try:
        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT name, SUM(qty), MAX(description) FROM t_sushi GROUP BY name ORDER BY name"
        cursor.execute(postgreSQL_select_Query)
        orders = cursor.fetchall()
        orderArray=[]

        for i in range(len(orders)):
            orderArray.append(f"{orders[i][0]} {orders[i][1]} {orders[i][2]}\n")

        return orderArray

    except (Exception, psycopg2.Error) as error:
        functions.logUsingPorchiddei("si è spaccato il db!" + str(error) + " Tutta colpa della getAll")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def myDishes(user):

    try:
        user = avoidSqlInjectionSingleParam(user)


        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT name, qty, description FROM t_sushi WHERE telegram_user = '" + user + "' ORDER BY name"
        cursor.execute(postgreSQL_select_Query)
        orders = cursor.fetchall()
        orderArray = []

        for i in range(len(orders)):
            orderArray.append(f"{orders[i][0]} {orders[i][1]} {orders[i][2]}\n")

        return orderArray

    except (Exception, psycopg2.Error) as error:
        functions.logUsingPorchiddei("si è spaccato il db!" + str(error) + " Tutta colpa della getAll")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def whoOrdered(name):

    try:
        name[2]=avoidSqlInjectionSingleParam(name[2])

        connection = psycopg2.connect(user=os.environ['USER_DB'],
                                      password=os.environ['PASS_DB'],
                                      host=os.environ['HOST_DB'],
                                      port=os.environ['PORT_DB'],
                                      database=os.environ['NAME_DB'])
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT telegram_user, qty, description FROM t_sushi WHERE name = '" + name[2] + "' ORDER BY telegram_user"
        cursor.execute(postgreSQL_select_Query)
        orders = cursor.fetchall()
        orderArray = []

        for i in range(len(orders)):
            orderArray.append(f"{orders[i][0]} {orders[i][1]} {orders[i][2]}\n")

        return orderArray

    except (Exception, psycopg2.Error) as error:
        functions.logUsingPorchiddei("si è spaccato il db!" + str(error) + " Tutta colpa della getAll")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")