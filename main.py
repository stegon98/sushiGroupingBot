import psycopg2
from bestemmie import Bestemmie
#porcone=Bestemmie().random()
#print(porcone)


def logUsingPorchiddei(error):
    porcone = Bestemmie()
    print(error+" "+porcone.random())


if __name__ == '__main__':
    logUsingPorchiddei('errore x')

