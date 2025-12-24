# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)

continue_bid = "yes"

data_dict = {}

while continue_bid == "yes":
    user = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    data_dict[user] = bid

    continue_bid = input("Are there any other bidders? Type \'yes\' or \'no\'.\n").lower()

    print("\n" * 20)

highest_bid_user = max(data_dict, key=data_dict.get)

print(f"The winner is {highest_bid_user} with a bid of ${data_dict[highest_bid_user]}")
