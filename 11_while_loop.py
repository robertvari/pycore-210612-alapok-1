import random, time

numbers = []

while True:
    if len(numbers) == 11:
        break

    next_number = random.randint(0, 10)
    if next_number not in numbers:
        numbers.append(next_number)
        print(next_number)
    else:
        print(f"{next_number} already in numbers")

    print(numbers)
    time.sleep(3)
