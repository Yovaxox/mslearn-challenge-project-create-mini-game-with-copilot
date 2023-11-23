import os
import random

# Initialize scores
os.system('clear' if os.name == 'posix' else 'cls')
user_score = 0
computer_score = 0
keep_playing = True

print("Welcome to Rock, Paper, Scissors!")

# Play again?
while keep_playing:
    while True:
        print("Please choose one of the following options:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_choice = input("\nYour choice: ")
        user_choice = user_choice.lower()
        if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Invalid choice. Please try again.\n")
        else:
            break
    
    os.system('clear' if os.name == 'posix' else 'cls')
    print("You chose: " + user_choice.capitalize())

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("\nThe computer chose: " + computer_choice.capitalize())

    # Create a dictionary to determine the game outcome
    game_outcomes = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if user_choice == computer_choice:
        print("\nIt's a tie!")
    elif game_outcomes[user_choice] == computer_choice:
        print("\nYou win!")
        user_score += 1
    else:
        print("\nYou lose!")
        computer_score += 1

    print(f"\nScore: You - {user_score}, Computer - {computer_score}")
    
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again in ["y", "n"]:
            os.system('clear' if os.name == 'posix' else 'cls')
            break
        else:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("Invalid choice. Please try again.\n")
    
    # If the user chooses "n", stop the game
    if play_again == "n":
        keep_playing = False

print("Thanks for playing!")
print(f"\nFinal Score: You - {user_score}, Computer - {computer_score}")