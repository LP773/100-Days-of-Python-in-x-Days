import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alpha = {row.letter:row.code for (index, row) in nato_dataframe.iterrows()}

while True:
    user_input = input("Enter a word: ").upper()
    try:
        nato_output = [nato_alpha[letter] for letter in user_input]
    except KeyError:
        print("Invalid input")
    else:
        print(nato_output)
        exit(0)

