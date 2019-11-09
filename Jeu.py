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
print("Voici les regles du jeu :\n-La pierre bat le ciseau. \n-Le ciseau bat la feuille.\n-La feuille bat la pierre.\n-Si les choix sont les mêmes il y a égalité.")

#
choix=["pierre","feuille","ciseaux"]
def joueur():
    joueur=input("Veuille choisir entre pierre, feuille ou ciseaux : ").lower()
    while joueur !=choix[0] and joueur !=choix[1] and joueur !=choix[2]:
        joueur=input("Je repete veuillez choisir entre pierre, feuille ou ciseaux : ").lower()
joueur()


def computeur():
    joueur=randint(0, 2)
    print("l'ordinateur à choisi", choix[joueur])
    return (choix[joueur])
computeur()


