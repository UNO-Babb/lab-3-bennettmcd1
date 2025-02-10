#RPS.py
#Name:Bennett
#Date: 2/9/25
#Assignment: rock Paper scissor
import random

# Main game loop
def play_game():
    wins = 0
    losses = 0
    ties = 0

    while True:
        # Computer's random choice
        computer_choice = random.choice(['R', 'P', 'S'])

        # Prompt user for their choice
        user_choice = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()

        # If the input is invalid, prompt again
        if user_choice not in ['R', 'P', 'S']:
            print("Invalid choice, try again!")
            continue

        # Determine the winner
        if user_choice == computer_choice:
            print(f"Computer chose {computer_choice}. It's a tie!")
            ties += 1
        elif (user_choice == 'R' and computer_choice == 'S') or \
             (user_choice == 'P' and computer_choice == 'R') or \
             (user_choice == 'S' and computer_choice == 'P'):
            print(f"Computer chose {computer_choice}. You win!")
            wins += 1
        else:
            print(f"Computer chose {computer_choice}. You lose!")
            losses += 1

        # Ask if the user wants to play again
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    # Print final stats
    print(f"\nFinal Stats - Wins: {wins}, Losses: {losses}, Ties: {ties}")

# Start the game
play_game()
