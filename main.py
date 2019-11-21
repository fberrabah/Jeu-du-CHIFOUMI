from functions import * #import fuctions
import sys #for exit program

#save the score in dictionary 
score= {
    "player": 0,
    "computer": 0
}

#show the rules 
print("Voici les regles du jeu :\n-La pierre bat le ciseau. \n-Le ciseaux bat la feuille.\n-La feuille bat la pierre.\n-Si les choix sont les mêmes il y a égalité.")

player_name = start()

#loop if score not 3 and show score
while score["player"] != 3 and score["computer"] != 3:
    player_choice = answer()
    computer_choice = computer()
    totaux= compare(computer_choice, player_choice, score)
    print("L'ordinateur a fait {}".format(computer_choice))
    print("Voici les scores {}:{} ordinateur score : {}".format(player_name, score["player"], score ["computer"]))

    if score["player"]>score["computer"] :
        print("bravo")

    else:
        print("perdue")

    #if score == 3 loops for ask if whant replay
    while score["player"] == 3 or score["computer"] == 3:
        restart=input("Voulez-vous rejouer? oui/non ").lower()
        if restart == "oui" :
            score["player"] = 0
            score["computer"] = 0
        elif restart == "non" :
            sys.exit()
        else:
            print("c'est oui ou non!!")
