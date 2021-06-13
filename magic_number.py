import random

min_number = 0
max_number = 10
max_tries = 3

magic_number = str(random.randint(min_number, max_number))

print(f"<<<DEBUG>>> {magic_number}")

print("="*50, "MAGIC NUMBER", "="*50)
print(f"I'm thinking of a number between {min_number} and {max_number}. Can you guess it?")
print(f"You have {max_tries} tries.")
print("="*100, "\n")

# str
player_guess = input("Your guess:")

while player_guess != magic_number:
    max_tries -= 1

    if max_tries == 0:
        print("You have no more tries :(((")
        break

    print(f"Wrong! :( You have {max_tries} tries left.")
    player_guess = input("Your guess:")


if player_guess == magic_number:
    print(f"You win! My number was {magic_number}")
else:
    print("Game Over :(((")