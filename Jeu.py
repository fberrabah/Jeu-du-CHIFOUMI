from random import randint
#start
print("---------------------------------------------\n----------------Bienvenue--------------------\n------------dans votre jeu du----------------\n----------Pierre,Feuille,Ciseau--------------\n---------------------------------------------\n")

#input pour que le joueur indique son nom
nom=input("Veuillez entrer votre nom pour jouer :")
while  len(nom)<= 1: 
    print ("tu te fous de mois")  
    nom=input("Veuillez entrer votre nom pour jouer :")       
print ("Bonne chance "+nom)

#information avec les regle du jeu
print("Voici les regles du jeu :\n-La pierre bat le ciseau. \n-Le ciseaux bat la feuille.\n-La feuille bat la pierre.\n-Si les choix sont les mêmes il y a égalité.")

choix=["pierre","feuille","ciseaux"]
joueur=input("Veuillez choisir entre pierre, feuille ou ciseaux : ").lower()
while joueur !=choix[0] and joueur !=choix[1] and joueur !=choix[2]:
    joueur=input("bouh il sait pas écrire! veuillez choisir entre pierre, feuille ou ciseaux : ").lower()

chosen=randint(0, 2)
print("Le meilleur programmeur à choisi", choix[chosen])
if chosen==0:
    choix="pierre"
elif chosen==1:
    choix="feuille"
else: 
    choix="ciseaux"

if joueur == choix:
    print("Match nul comme toi!!")
elif joueur == "pierre" and choix=="feuille":
    print("Perdue!! serieusement une feuille arrive à te battre... laisse moi rire! ")  
elif joueur == "feuille" and choix== "pierre":      
    print("coup de chance vous avez gagné")
elif joueur == "ciseaux" and choix== "pierre": 
    print("Perdue!! je vous écrasse avec ma pierre!! ")
elif joueur == "pierre" and choix== "ciseau": 
    print("coup de chance vous avez gagné")
elif joueur == "feuille" and choix== "ciseau": 
    print("Perdue!! je vous découpe c'est tellement facile!! ")
elif joueur == "ciseaux" and choix== "feuille": 
    print("coup de chance vous avez gagné")