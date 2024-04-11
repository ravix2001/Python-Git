import random

while True:
    choice = random.randint(1,6)
    
    print("\n",choice)

    play_again = input("\nRoll again ? [y/n]    ")
    if play_again != "y":
        break
