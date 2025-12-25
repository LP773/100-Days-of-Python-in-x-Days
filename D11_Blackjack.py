import art
import random

def blackjack():
    # Deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Hands
    player_hand = []
    dealer_hand = []

    def player_draw():
        player_hand.append(random.choice(cards))

    def dealer_draw():
        dealer_hand.append(random.choice(cards))

    def calculate_scores():
        p_score = sum(player_hand)
        d_score = sum(dealer_hand)
        return p_score, d_score

    print(art.logo)
    player_draw(),player_draw()
    dealer_draw()
    player_score, dealer_score = calculate_scores()
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {dealer_hand}")

    # Player Phase
    while player_score <= 21:
        hit = input("\nType 'y' to get another card, type 'n' to pass: ")
        if hit == "y":
            player_draw()
            player_score, dealer_score = calculate_scores()
            print(f"Your cards: {player_hand}, current score: {player_score}")
            print(f"Computer's first card: {dealer_hand}")
        else:
            break

    # Dealer Phase
    while dealer_score < 17:
        dealer_draw()
        player_score, dealer_score = calculate_scores()

    # Score Phase
    player_score, dealer_score = calculate_scores()
    if player_score > 21:
        print(f"    Your final hand: {player_hand}, final score: {player_score}")
        print(f"    Computer's final hand: {dealer_hand}, final score {dealer_score}")
        print("You went over. You lose 😭\n")
    elif dealer_score > 21 and player_score < 21:
        print(f"    Your final hand: {player_hand}, final score: {player_score}")
        print(f"    Computer's final hand: {dealer_hand}, final score {dealer_score}")
        print("Your opponent went over. You win 😁\n")
    elif dealer_score == player_score:
        print(f"    Your final hand: {player_hand}, final score: {player_score}")
        print(f"    Computer's final hand: {dealer_hand}, final score {dealer_score}")
        print("Draw\n")
    elif 21 >= dealer_score > player_score:
        print(f"    Your final hand: {player_hand}, final score: {player_score}")
        print(f"    Computer's final hand: {dealer_hand}, final score {dealer_score}")
        print("Opponent wins.\n")
    elif 21 >= player_score > dealer_score:
        print(f"    Your final hand: {player_hand}, final score: {player_score}")
        print(f"    Computer's final hand: {dealer_hand}, final score {dealer_score}")
        print("You win 😁\n")

playing = True
while playing:
    response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': " )
    if response == "y":
        blackjack()
    else:
        playing = False

