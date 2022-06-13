# Rock-Paper-Scissors
# Game rules
# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper

import random

options = ["R", "P", "S"]

print("Rock-Paper-Scissors GAME")

play = True
# cpu_choice = random.choice(options)
# print("Available options: R for Rock, P for Paper, or S for Scissors")
# user_choice = input("Please choice an option: ")
# print("Player ("+user_choice+") : CPU ("+cpu_choice+")")

def startgame():
    print("Rock-Paper-Scissors GAME")
    print("Available options: R for Rock, P for Paper, or S for Scissors")
    user_choice = input("Please choice an option: ")
    print("Player ("+user_choice+") : CPU ("+cpu_choice+")")

def endgame():
    # print("Rock-Paper-Scissors GAME")
    print("END. THANKS FOR PLAYING")


def restart():
    # print("Rock-Paper-Scissors GAME")
    print("Restart GAME")


def game(user_choice, cpu_choice):
    print("Rock-Paper-Scissors GAME")
    if(((user_choice == "R") & (cpu_choice == "S"))):
        print("You won 😄")
        endgame()
        play = False
    elif(((user_choice == "P") & (cpu_choice == "R"))):
        print("You won 😄")
        endgame()
        play = False
    elif(((user_choice == "S") & (cpu_choice == "P"))):
        print("You won 😄")
        endgame()
        play = False
    else:
        print("Oops you lost 😩 (CPU WON)")
        endgame()
        play = False

# user_choice = input("Please choice an option: ")
# cpu_choice = random.choice(options)
# print("Player ("+user_choice+") : CPU ("+cpu_choice+")")

while play:
    # startgame()
    cpu_choice = random.choice(options)
    cpu_choice = "R"
    print("Available options: R for Rock, P for Paper, or S for Scissors")
    # user_choice = input("Please choice an option: ")
    user_choice = input("Please choice an option: ")
    print("Player ("+user_choice+") : CPU ("+cpu_choice+")")
    if user_choice in options:
        # print(user_choice)
        # print(cpu_choice)
        # play = False
        if user_choice != cpu_choice:
            print("Results")
            game(user_choice, cpu_choice)
            # if(((user_choice == "R") & (cpu_choice == "S"))):
            #     print("You won 😄")
            #     endgame()
            #     play = False
            # elif(((user_choice == "P") & (cpu_choice == "R"))):
            #     print("You won 😄")
            #     endgame()
            #     play = False
            # elif(((user_choice == "S") & (cpu_choice == "P"))):
            #     print("You won 😄")
            #     endgame()
            #     play = False
            # else:
            #     print("Oops you lost 😩 (CPU WON)")
            #     endgame()
            #     play = False
        else:
            print("Oops we got a tie!")
            play = False
    
if user_choice == cpu_choice:
    restart()
    play = True