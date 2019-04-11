####Trouver un nombre aléatoire sans boucle

import random
n = random.randint (0,9) 
nombre_alea= int(input("saisir un nombre compris entre 0 et 9 : "))
if n == nombre_alea:
    print("Bravo ! C'est gagnez")
else:
    print("Désolé ! C'est perdu")


