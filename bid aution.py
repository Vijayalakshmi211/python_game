import os  # Import os for clearing the console

bidding_finished = False
bids = {}  # Initialize the bids dictionary

def find_highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:  # Iterate through the bidding records
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:  # Check if the current bid is higher than the highest bid
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}")  # Print the winner and their bid

while not bidding_finished:
    name = input("What is your name? ")  # Get the name of the bidder
    price = int(input("What is your bid? $"))  # Get the bid amount
    bids[name] = price  # Store the bid in the bids dictionary

    # Check if there are any previous bids to compare
    if len(bids) > 1:
        current_highest_bid = max(bids.values())  # Get the current highest bid
        if price > current_highest_bid:
            print(f"Your bid of ${price} is currently the highest bid!")
        else:
            print(f"Your bid of ${price} is lower than the current highest bid of ${current_highest_bid}.")

    should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n")  # Ask if there are more bidders
    
    if should_continue.lower() == "no":  # Check if there are no more bidders
        bidding_finished = True  # Set the flag to stop the loop
    elif should_continue.lower() == "yes":  # If there are more bidders
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for a clean slate

# After exiting the loop, find the highest bidder
find_highest_bidder(bids)  # Call the function to find the highest bidder