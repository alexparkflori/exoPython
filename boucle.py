# depuis la bibliotheque random, on importe la formule (fonction) randrange
# qui permet de recuperer un chiffre aleatoire
from random import randrange

#---------------------------
# exemple 1

# je creer une variable phrase qui contient la chaine de caractere "bonjour a tous!"
phrase = "bonjour à tous !"

# la boucle for permet de parcourir la phrase en recuperant chaque
# caractere et la stoque temporairement dans lettre
for  lettre in phrase:
    
    # on compare la lettre recupere avec la liste de "Bbour"
    if lettre in "Bbour":
        print(lettre)

#----------------------------
#exemple 2

#input permet de demander de taper quelque chose au clavier
#ici, un entier : int()
#on stoque la variable tapez dans table

table = int(input("tapez un chiffre: "))
multiple = 1

#tant que la variable multiple est plus petit OU egal a 10
while multiple <=10:
    #on affiche la multiplication de la table choisie avec son multiplicateur
    print( table * multiple)
    #on augmente a chaque tour la variable multiple de +1 (incrementer)
    multiple = multiple + 1

#exemple 3
#on demande a randrange de nous donner un chiffre aleatoire compris:
# entre 0 à 100 puis on stoque le resultat dans chiffre
chiffre = randrange(101)

# on cree une variable boolean trouver qui vaut FAUX
trouver = False

#tant que trouver est egal a FAUX, on continue la boucle
while trouver == False:
    a = int(input("tapez un chiffre: "))
    if a < chiffre:
        print ("le chiffre est plus grand")
    elif a > chiffre:
        print ("le chiffre est plus petit")
    else: 
        print ("EUREKa")
        #si on a trouve, il faut penser a changer la valeur de
        #notre "Flag" trouver qui passe a VRAI et stop la boucle
        trouver = True
