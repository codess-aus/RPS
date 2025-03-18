import secrets

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return secrets.choice(choices)

# Function to get the user's choice
def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice

# Function to determine the winner of a single game
def determine_winner(user_choice, computer_choice):
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if user_choice == computer_choice:
        return 'tie'
    elif winning_combinations[user_choice] == computer_choice:
        return 'user'
    else:
        return 'computer'

# Main function to play the best of 3 games
def play_best_of_three():
    user_wins = 0
    computer_wins = 0

    # Play until one of the players wins 2 games
    while user_wins < 2 and computer_wins < 2:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        # Output the result of the current game
        print(f"You chose {user_choice}, computer chose {computer_choice}.")
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            print("You win this round!")
            user_wins += 1
        else:
            print("Computer wins this round!")
            computer_wins += 1

        # Output the current score
        print(f"Score: You {user_wins} - Computer {computer_wins}")

    # Congratulate the final winner
    if user_wins == 2:
        print("Congratulations! You won the best of 3 games! You are the Rock, Paper, Scissors champion!")
    else:
        print("Computer wins the best of 3 games. Better luck next time!")

# Start the game
if __name__ == "__main__":
    play_best_of_three()