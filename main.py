import psycopg2
import os
from bestemmie import Bestemmie



def logUsingPorchiddei(error):
    porcone = Bestemmie()
    print(error+" "+porcone.random())


if __name__ == '__main__':
    logUsingPorchiddei('start')

    connection = psycopg2.connect(user=os.environ['USER_DB'],
                                  password=os.environ['PASS_DB'],
                                  host=os.environ['HOST_DB'],
                                  port=os.environ['PORT_DB'],
                                  database=os.environ['NAME_DB'])
    cursor = connection.cursor()
    postgres_insert_query = "INSERT INTO t_bestemmie ( bestemmia) VALUES ('" + row[i]["bestemmia"] + "')"
    cursor.execute(postgres_insert_query)
    connection.commit()