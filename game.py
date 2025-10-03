import random

def get_computer_choice():
    """Generates a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """Prompts the user for their choice and validates the input."""
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the game rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

def play_game():
    """Main function to run the Rock-Paper-Scissors game."""
    print("---------------------------------------")
    print("    Welcome to Rock-Paper-Scissors!    ")
    print("---------------------------------------")

    while True:
        # Get choices
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"\nYou chose: **{user.upper()}**")
        print(f"The computer chose: **{computer.upper()}**")

        # Determine and display result
        result = determine_winner(user, computer)
        print(f"\n**{result}**")
        print("-" * 35)

        # Ask to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye. 👋")
            break

# Run the game
if __name__ == "__main__":
    play_game()
