###Générer un nombre aléatoire
import random

nombre_secret = random.randint(0,9)

response = None

while response != nombre_secret:

      response = int(input("Entrez un nombre entre 0 et 9:"))

if response < nombre_secret:

      print("Le nombre secret est plus grand")

elif response > nombre_secret:

      print("Le nombre secret est plus petit")

else:

      print("Bravo !")
