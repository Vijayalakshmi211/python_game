import random

# Define the game images
game_images = ["rock", "paper", "scissors"]

# Get user choice
user_choice = int(input("What do you choose? type 0 for rock, 1 for paper or 2 for scissors \n"))

# Check for invalid input
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You chose:", game_images[user_choice])
    
    # Generate computer choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:", game_images[computer_choice])
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")