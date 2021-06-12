my_name = "Tom"
my_age = 34

# indexes:    0    1   2   3
my_numbers = [23, 56, 12, 46]

# mixed list
my_list = [
    "Robert",
    "Csaba",
    "Christina",
    32,
    3.14,
    my_name,
    my_age,
    my_numbers
]

# print(my_list[7][-1])
# print(my_list[0])


# add items to list
my_numbers.append("Csilla")
print(my_numbers)

my_numbers.insert(2, "Laci")
print(my_numbers)


# remove item from list
my_numbers.remove(56)
print(my_numbers)

del my_numbers[2]
print(my_numbers)

del my_numbers[my_numbers.index("Csilla")]
print(my_numbers)

print("Csilla" in my_numbers)

# clear
my_numbers.clear()
print(my_numbers)