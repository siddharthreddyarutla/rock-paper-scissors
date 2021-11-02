import random
#for generating random numbers

user_points  = 0
computer_points = 0

choice = ["rock", "paper", "scissors"]
#list for indexing
while True:
    user_input = input("\nRock/Paper/Scissors or none: ").lower()
    
    if user_input == "none":
        quit()

    if user_input not in choice:
        continue

    random_number = random.randint(0, 2)
    # 0 for rock
    # 1 for paper
    # 2 for scissor
    computer_pick = choice[random_number]
    print("\nComputer choosed", computer_pick)

    if user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_points += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_points += 1
    
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_points += 1
    
    elif user_input == "rock" and computer_pick == "rock":
        print("Try again!")

    elif user_input == "paper" and computer_pick == "paper":
        print("Try again!")

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Try agian!")

    else:
        print("You lost!")
        computer_points += 1


    print("You won", user_points, "times.")
    print("The computer won", computer_points, "times.")
    print("Better luck next time!")