from data import data
import random
#from art import logo  # Assuming you have an art module with a logo

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

#print(logo)
score = 0
game_should_continue = True

# Start the game loop
while game_should_continue:
    account_b = random.choice(data)
    account_a = random.choice(data)

    # Ensure account_a and account_b are different
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print("VS")
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'a' or 'b': ").lower()
    #print("\n" * 20)
    #print(logo)

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers_count, b_followers_count)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False  # End the game if the answer is wrong