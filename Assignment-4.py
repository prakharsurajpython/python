import random

# Step 1: Function to get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Step 2: Function to determine the winner
def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

# Step 3: Function to display the score
def display_score(wins, losses, ties):
    print("\nScoreboard")
    print("Wins:", wins)
    print("Losses:", losses)
    print("Ties:", ties)
    print("---------------------")

# Step 4: Function to save the score to a file
def save_score_to_file(wins, losses, ties):
    try:
        file = open("game_score.txt", "w")
        try:
            file.write("Rock-Paper-Scissors Final Score\n")
            file.write(f"Wins: {wins}\n")
            file.write(f"Losses: {losses}\n")
            file.write(f"Ties: {ties}\n")
        finally:
            file.close()
        print("Final score saved to 'game_score.txt'")
    except Exception as e:
        print("Error saving score:", e)

# Step 5: Main game loop
def play_game():
    wins = 0
    losses = 0
    ties = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Enter rock, paper, scissors or type 'quit' to end the game.")

    while True:
        try:
            user_input = input("Your move: ").lower()

            if user_input == "quit":
                break

            if user_input not in ["rock", "paper", "scissors"]:
                raise ValueError("Invalid input. Please enter rock, paper, or scissors.")

            computer_input = get_computer_choice()
            print(f"Computer chose: {computer_input}")

            result = get_winner(user_input, computer_input)

            if result == "win":
                print("You win!")
                wins += 1
            elif result == "lose":
                print("You lose!")
                losses += 1
            else:
                print("It's a tie!")
                ties += 1

            display_score(wins, losses, ties)

        except ValueError as e:
            print("Error:", e)

    #Display Final Score and Save to a File
    print("\nThanks for playing!")
    display_score(wins, losses, ties)
    save_score_to_file(wins, losses, ties)

# Step 6: Run the game
play_game()
