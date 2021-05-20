from tkinter import *
from random import *
def tiremot():
    fi= open('Mots.txt','r')
    num = randint(1,20)
    i=0
    while i < num :
        mot = fi.readline()
        i=i+1
    fi.close()
    return mot

def affichemot(mot,lettres):
    r=""
    for i in range(len(mot)) :
        if lettres.upper().count(mot.upper()[i])>0:
            r=r+mot.upper()[i]+" "
        else :
            r=r+"-"
    return r

mot = tiremot()
propos = mot[0]+mot[len(mot)-1]
erreur = 8

while affichemot(mot,propos) != affichemot(mot,mot) and erreur > 0:
    print ("Il vous reste", erreur, "chance(s).")
    print (affichemot(mot,propos))
    lettre = input("Proposez une lettre")
    propos = propos + lettre
    if lettre.lower() not in mot :
        erreur = erreur - 1
    if lettre.lower() in propos.lower() :
        print ("Cette lettre a déjà été proposée...")
if erreur == 0 :
    print ("Le mot était", mot)
else :
    print(mot)
    print ("Bravo")