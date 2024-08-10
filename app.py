import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return None

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    winner = get_winner(user_choice, computer_choice)

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

    return winner

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        result = play_round()

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()

        if play_again != "yes":
            break

    print("Thanks for playing! Final score:")
    print(f"You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
