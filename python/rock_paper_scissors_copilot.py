# This game was created with the assistance of co-pilot, following the guide here: https://github.com/blackgirlbytes/rock-paper-scissors-copilot

# Write a rock, paper, scissors, game
# import random module
import random

# define main function that handles all the logic
def main():
    # define variables
    user_choice = ""
    computer_choice = ""
    user_score = 0
    computer_score = 0
    # define a list of choices
    choices = ["rock", "paper", "scissors"]
    # define a loop that runs until the user quits
    while user_choice != "quit":
        # get user choice
        user_choice = input("Enter rock, paper, scissors, or quit: ")
        # get computer choice
        computer_choice = random.choice(choices)
        # determine winner
        if user_choice == "rock":
            if computer_choice == "rock":
                print("Tie!")
            elif computer_choice == "paper":
                print("Computer wins!")
                computer_score += 1
            elif computer_choice == "scissors":
                print("You win!")
                user_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
                user_score += 1
            elif computer_choice == "paper":
                print("Tie!")
            elif computer_choice == "scissors":
                print("Computer wins!")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Computer wins!")
                computer_score += 1
            elif computer_choice == "paper":
                print("You win!")
                user_score += 1
            elif computer_choice == "scissors":
                print("Tie!")
        # print score
        print("You: " + str(user_score) + " Computer: " + str(computer_score))

# call main function
main()
