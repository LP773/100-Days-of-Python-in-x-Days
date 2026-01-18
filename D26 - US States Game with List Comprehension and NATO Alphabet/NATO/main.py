import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alpha = {row.letter:row.code for (index, row) in nato_dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
letters = list(user_input)
nato_output = [nato_alpha[letter] for letter in letters if letter in nato_alpha]
# My above solution is more complicated than if I'd done
# nato_output = [nato_alpha[letter] for letter in letters]
print(nato_output)
