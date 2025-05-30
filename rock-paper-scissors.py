import random

# Emoji and name mapping
moves = {
    1: ("rock", "🪨"),
    2: ("paper", "📄"),
    3: ("scissors", "✂️")
}

# Determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "🤝 It's a tie!"
    elif (player == 1 and computer == 3) or \
         (player == 3 and computer == 2) or \
         (player == 2 and computer == 1):
        return "🎉 You win!"
    else:
        return "😢 Computer wins!"

# Main game
def play_game():
    print("👊 Welcome to Rock, Paper, Scissors!")
    print("Choose your move:")
    print("1 - Rock 🪨")
    print("2 - Paper 📄")
    print("3 - Scissors ✂️")
    print("0 - Quit")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3 or 0 to quit): "))
            if choice == 0:
                print("👋 Thanks for playing!")
                break
            if choice not in moves:
                print("⚠️ Invalid number. Try again.\n")
                continue

            computer_choice = random.randint(1, 3)

            player_name, player_emoji = moves[choice]
            comp_name, comp_emoji = moves[computer_choice]

            print(f"\nYou chose: {player_emoji} ({player_name})")
            print(f"Computer chose: {comp_emoji} ({comp_name})")

            result = determine_winner(choice, computer_choice)
            print(result + "\n")

        except ValueError:
            print("⚠️ Please enter a valid number.\n")

# Run the game
play_game()