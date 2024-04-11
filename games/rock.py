import random

while True:
    choices = ["rock", "paper", "scissor"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("\nrock , paper or scissor ? ").lower()

    if player == computer:
        print("\ncomputer : ",computer)
        print("player : ",player)
        print("\nTie!")
    elif player =="rock":
        if computer == "paper":
            print("\ncomputer : ",computer)
            print("player : ",player)
            print("\nYou lose!")
        if computer == "scissor":
            print("\ncomputer : ",computer)
            print("player : ",player)
            print("\nYou won!")
    elif player =="paper":
        if computer == "scissor":
            print("\ncomputer : ",computer)
            print("player : ",player)
            print("\nYou lose!")
        if computer == "rock":
            print("\ncomputer : ",computer)
            print("player : ",player)
            print("\nYou won!")
    elif player =="scissor":
        if computer == "rock":
            print("\ncomputer : ",computer)
            print("player : ",player)
            print("\nYou lose!")
        if computer == "paper":
            print("\ncomputer : ",computer)
            print("player : ",player)
            print("\nYou won!")
    play_again = input("\nWant to play again? (Y/N): ").lower()
    
    if play_again !="y":
        break

print("Bye!\n")