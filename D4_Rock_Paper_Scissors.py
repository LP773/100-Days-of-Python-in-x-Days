import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
     ___
---'(___)______
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors")
choice = input("Think you can beat the RNG Bot? Pick Rock (1), Paper (2), or Scissors (3)? ")
robo = rock_paper_scissors[random.randint(0, 2)]
choice = int(choice)

print("\n=== You ===")
if choice == 1:
      print(rock_paper_scissors[0])
elif choice == 2:
    print(rock_paper_scissors[1])
else:
    print(rock_paper_scissors[2])
print("=== RNG Bot ===")
print(robo)

if choice == 1 and robo == scissors:
    print("You win!")
elif choice == 1 and robo == paper:
    print("You lose!")
elif choice == 1 and robo == rock:
    print("Draw!")
elif choice == 2 and robo == scissors:
    print("You lose!")
elif choice == 2 and robo == paper:
    print("Draw!")
elif choice == 2 and robo == rock:
    print("You win!")
elif choice == 3 and robo == scissors:
    print("Draw!")
elif choice == 3 and robo == paper:
    print("You win!")
elif choice == 3 and robo == rock:
    print("You lose!")
