import random
import art

def guess_the_number():
    attempts = 0

    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = (input("Choose a difficulty: Type 'easy' or 'hard': ")).lower()
    
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
        
    print(f"You have {attempts} attempts remaining to guess the number.")
    
    while attempts > 0:
    guess = int(input("Guess the number: "))
        if guess < number:
            print("\nToo low")
            print("Guess again")
            attempts -= 1
            print("You have " + str(attempts) + " attempts remaining to guess the number.\n")
        elif guess > number:
            print("\nToo high")
            print("Guess again")
            attempts -= 1
            print("You have " + str(attempts) + " attempts remaining to guess the number.\n")
        else:
            print(f"You got it! The answer was {number}")
            break
    if attempts == 0:
        print("You've run out of guesses, you lose.")

    print(f"You got it! The answer was {number}")
    
guess_the_number()
