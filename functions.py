import random

choix=["pierre","feuille","ciseaux"]

#
def start():
    name=input("Veuillez entrer votre nom pour jouer :")
    while checkstart(name) is False:
        print("votre nom mais en mieux")
        name=input("votre nom")
    return name

def checkstart(name):
    try:
        assert len(name) > 1 and len(name) < 15
    except AssertionError as a:
        return False
        
def answer():
    user=input("Veuillez choisir entre pierre, feuille ou ciseaux : ").lower()#player enter choice
    while controle_answer(user) is False :
        print("Veuillez choisir entre pierre, feuille ou ciseaux : ")
        user=input("Veuillez choisir entre pierre, feuille ou ciseaux : ").lower()#player enter choice  
    return user

def controle_answer(user):
    try:
        assert user in choix
    except AssertionError as e :
        return False

def computer():
    return choix[random.randint(0,len(choix)-1)]

def compare(computer_choice, player_choice, score):
    if player_choice != computer_choice:
        if player_choice == "pierre" and computer_choice == "ciseaux"\
        or player_choice == "feuille" and computer_choice == "pierre"\
        or player_choice == "ciseaux" and computer_choice == "feuille":
            score["player"] +=1
        else :
            score["computer"] +=1
    return score

