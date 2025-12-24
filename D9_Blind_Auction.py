import art

print(art.logo)
more_bids = "yes"
bid_dictionary = {}

while more_bids == "yes":

    name = input("Enter your name: ")
    bid = input("Enter your bid: $")

    bid_dictionary[name] = bid
    more_bids = input("Are there any other bidders? Types 'yes' or 'no': ")

    if more_bids == "yes":
        print("\n" * 20)

max_key = max(bid_dictionary, key=bid_dictionary.get)
print(f"The highest bidder was {max_key} with a bid of ${bid_dictionary[max_key]}.")
