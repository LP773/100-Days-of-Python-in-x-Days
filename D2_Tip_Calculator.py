print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 15 18? "))
tip_amount = bill * (tip/100)
people = int(input("How many people to split the bill? "))
split = (bill + tip_amount) / people
print(round(split,2))

