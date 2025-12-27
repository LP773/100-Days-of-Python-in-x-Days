import art
import random
import game_data as gd

score = 0
game_over = False

def get_data():
    a_rng = random.randint(0, len(gd.data) - 1)
    b_rng = random.randint(0, len(gd.data) - 1)
    while a_rng == b_rng:
        a_rng = random.randint(0, len(gd.data) - 1)
        b_rng = random.randint(0, len(gd.data) - 1)

    compare_a = {
        "name": gd.data[a_rng]["name"],
        "description": gd.data[a_rng]["description"],
        "country": gd.data[a_rng]["country"],
        "follower_count": gd.data[a_rng]["follower_count"]
    }
    compare_b = {
        "name": gd.data[b_rng]["name"],
        "description": gd.data[b_rng]["description"],
        "country": gd.data[b_rng]["country"],
        "follower_count": gd.data[b_rng]["follower_count"]
    }
    return compare_a, compare_b

def check_answer(ans, comp_a, comp_b):
    if ans == "a":
        if set_a["follower_count"] > set_b["follower_count"]:
            return True
    elif ans == "b":
        if set_a["follower_count"] < set_b["follower_count"]:
            return True
    return False

print(art.logo)
set_a, set_b = get_data()
print(f"Compare A: {set_a["name"]}, a {set_a["description"]}, from {set_a["country"]}")
print(art.vs)
print(f"Compare B: {set_b["name"]}, a {set_b["description"]}, from {set_b["country"]}")
answer = input(f"Who has more followers? Type 'A' or 'B': ").lower()
correct = check_answer(answer, set_a, set_b)
while not game_over:
    if correct == False:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
    elif correct:
        score += 1
        if answer == 'b':
            set_a = set_b
        _, set_b = get_data()
        print("\n" * 20)
        print(art.logo)
        print(f"You're right! Current score: {score}")
        print(f"Compare A: {set_a["name"]}, a {set_a["description"]}, from {set_a["country"]}")
        print(art.vs)
        print(f"Compare B: {set_b["name"]}, a {set_b["description"]}, from {set_b["country"]}")
        answer = input(f"Who has more followers? Type 'A' or 'B': ").lower()
        correct = check_answer(answer, set_a, set_b)
