import random

def generatore_password():
    eseguire = "s"

    while eseguire == "s":
        generatore()

        eseguire = input("Vuoi eseguire nuovamente il programma(inserire s per rieseguire il programma e n per terminare l'attività): ")

        while(eseguire != "s" and eseguire != "n"):
            eseguire = input("Inserisci n o s: ")

        if eseguire == "n":
            print("Grazie per aver usato il programma")


def generatore():

    print("\n---GENERATORE DI PASSWORD---")
    caratteri = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890QWERTYUIOPASDFGHJKLZXCVBNM!?/-_#@*"
    lunghezza = int(input("Inserisci di quanti caratteri deve essere composta la password: "))

    while(lunghezza < 1):
        print("ATTENZIONE! inserisci un numero di caratteri maggiore di 0")
        lunghezza = int(input("Inserisci di quanti caratteri deve essere composta la password: "))


    password = ""

    for i in range(lunghezza):
        password += random.choice(caratteri)

    print("La password generata è: " + password)

generatore_password()