from random import randint
#from art import logo

# Number of turns for each level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Check answer with user guess
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high")
        return False  # Indicate that the guess was incorrect
    elif user_guess < actual_answer:
        print("Too low")
        return False  # Indicate that the guess was incorrect
    else:
        print(f"You got it! The answer was {actual_answer}")
        return True  # Indicate that the guess was correct

# Setting difficulty using a function
def set_difficulty():
    level = input("Choose a difficulty type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS  # Return the number of turns for easy level
    elif level == "hard":
        return HARD_LEVEL_TURNS  # Return the number of turns for hard level
    else:
        print("Invalid choice, defaulting to easy.")
        return EASY_LEVEL_TURNS  # Default to easy if input is invalid

def game():
    #print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)  # Generate a random number
    #print(f"psst, the correct answer is {answer}")  # Optional: reveal answer for testing

    turns = set_difficulty()  # Get the number of turns based on difficulty
    guess = 0  # Initialize guess variable

    # Loop until the user runs out of turns or guesses correctly
    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))  # Get user input for guess
        turns -= 1  # Decrease the number of turns after each guess
        if check_answer(guess, answer):  # Check if the guess is correct
            break  # Exit the loop if the guess is correct
        if turns == 0:
            print("You're out of guesses, you lose.")  # Notify user of loss
            print(f"The correct answer was {answer}.")  # Reveal the answer
            return  # Exit the game

    print("Thanks for playing!")  # End of game message

# Start the game
game()