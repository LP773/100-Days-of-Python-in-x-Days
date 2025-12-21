import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_pw = []
symbol_pw = []
numbers_pw = []
combined = []
ez_password = ""
password = ""
hd_password = ""

### Very Easy Level ###
# Overthought things through
for letter in letters[0:nr_letters]:
    letter_pw.append(letter)
for symbol in symbols[0:nr_symbols]:
    symbol_pw.append(symbol)
for number in numbers[0:nr_numbers]:
    numbers_pw.append(number)

combined = letter_pw + symbol_pw + numbers_pw

for items in combined:
    ez_password += items

print("Very Easy Level Password: " + str(ez_password))

### Easy Level ###
# Watched the video solution to doing it the easy way + hard way and saw I overthought things
for char in range(0, nr_letters):
    password += random.choice(letters)
for char in range(0, nr_symbols):
    password += random.choice(symbols)
for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(f"Easy Level Password: {password}")

### Harder Level ###
# Did this after Very Easy Level
i = 0
if i < nr_letters:
    letter_pw += random.choice(letters)
    i+= 1
if i < nr_symbols:
    symbol_pw += random.choice(symbols)
    i+= 1
if i < nr_numbers:
    numbers_pw += random.choice(numbers)
    i+= 1

combined = letter_pw + symbol_pw + numbers_pw
random.shuffle(combined)
for items in combined:
    hd_password += items
print("Hard Level Password: " + str(hd_password))


