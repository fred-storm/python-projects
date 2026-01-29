import random


def computer_choice ():
    comp_decision = random.randint(1,3)
    computer_hand = "unassigned"
    match comp_decision:
        case 1:
            computer_hand = "rock"
        case 2:
            computer_hand = "paper"
        case 3:
            computer_hand = "scissors"
        case _:
            computer_hand = "null"
    return computer_hand

def player_choice():
    player_pick = int(input("""Pick 1 for rock:
    2 for paper:
    3 for scissors:
    your choice?: """))
    player_hand = "unassigned"
    match player_pick:
        case 1:
            player_hand = "rock"
        case 2:
            player_hand = "paper"
        case 3:
            player_hand = "scissors"
        case _:
            player_hand = "null"

    return player_hand

game_choice = input("Do you want to play a game?")
if game_choice == "yes":
    print("Lets play rock, paper, scissors!")
else:
    print("Ok, bye!")


player_pick = player_choice()
computer_pick = computer_choice()
print(computer_pick, player_pick)
if player_pick == computer_pick:
    print("Its a tie!")
    print("You picked:", player_pick, " The computer picked;", computer_pick)
elif player_pick == "rock" and  computer_pick =="scissors":
    print("Player wins!")
    print("You picked:", player_pick, " The computer picked;", computer_pick)
elif player_pick == "paper" and computer_pick == "rock":
    print("Player wins!")
    print("You picked:", player_pick, " The computer picked;", computer_pick)
elif player_pick == "scissors" and computer_pick == "paper":
    print("Player wins!")
    print("You picked:", player_pick, " The computer picked;", computer_pick)
else:
    print("Computer wins!")
    print("You picked:", player_pick, " The computer picked;", computer_pick)
