import random 

choice = ("rock", "paper", "scissor")
game = True

while game:

    player= ""
    comp = random.choice(choice)


    while player not in choice:
        player = input("Choose an option (rock, paper, scissor): ")

    print(f"computer chose {comp}")
    print(f"player chose {player}")

    if player==comp:
        print ("It's a tie.")
    elif player== "paper" and comp == "rock":
        print ("Player wins")
    elif player == "rock" and comp == "scissor":
        print("Player wins")
    elif player == "scissor" and comp == "paper":
        print("Player wins")
    else:
        print("Computer wins")
    
    if input("Play again? (yes/no): ") != "yes":
        game = False

print("Thanks for playing!\nHave a good day!!!")