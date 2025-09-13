import random
from data import data
from art import logo
from art import vs


def format_person(person):
    person_name = person["name"]
    person_dscrp = person["description"]
    return f"{person_name}, {person_dscrp}"


def check_answer(user_guess, person_a_followers, person_b_followers):
    if person_a_followers > person_b_followers and user_guess == "a":
        return True
    elif person_b_followers > person_a_followers and user_guess == "b":
        return True
    elif person_a_followers > person_b_followers and user_guess == "b":
        return False
    else:
        return False


score = 0
keep_playing = True
print(logo)
person_b = random.choice(data)

while keep_playing:
    person_a = person_b
    person_b = random.choice(data)
    if person_a == person_b:
        person_b = random.choice(data)
    person_a_followers = person_a["follower_count"]
    person_b_followers = person_b["follower_count"]

    print(f"Compare A: {format_person(person_a)}")
    print(vs)
    print(f"Against B: {format_person(person_b)}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_right = check_answer(user_guess, person_a_followers, person_b_followers)
    if is_right:
        score += 1
        print(logo)
        print(f"You're right, Kya baat hai! Current score: {score}")

    else:
        keep_playing = False
        print(f"Sorry that's wrong. Final score: {score}")
        score = 0
        play_again = input("Do you want to play again? (y or n): ").lower()
        if play_again == "y":
            keep_playing = True
        else:
            print("Alright, Goodbye, and remember: Pakistan Zindabad!")


