LETTER_FILE = open("./Input/Letters/starting_letter.txt", "r")
NAMES_FILE = open("./Input/Names/invited_names.txt", "r")
OUTPUT_DIR = "./Output/ReadyToSend/"
LETTER_CONTENTS = LETTER_FILE.read()

for name in NAMES_FILE:
    invitation = LETTER_CONTENTS.replace("[name]", name.strip( ))
    with open(f"{OUTPUT_DIR}letter_for_{name.strip()}.txt", "w") as f:
        f.write(invitation)
LETTER_FILE.close()
NAMES_FILE.close()
