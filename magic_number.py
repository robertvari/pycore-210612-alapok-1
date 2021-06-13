import random

min_number = 0
max_number = 10
max_tries = 3

magic_number = random.randint(min_number, max_number)
print("="*50, "MAGIC NUMBER", "="*50)
print(f"I'm thinking of number between {min_number} and {max_number}. Can you guess it?")
print(f"You have {max_tries} tries.")