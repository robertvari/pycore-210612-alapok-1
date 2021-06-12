# cast list into a set
my_list = [1, 2, 3, "csaba", 4, "csaba", 2, 1]
my_set = set(my_list)

# print(my_set)

# add items to set
new_set = {1, 2, 3}

# print(new_set)
new_set.add(4)
# print(new_set)

# add more items to set
new_set.update([5, 6, 7, 8])
# print(new_set)

new_set.remove(5)
new_set.discard(7)
# print(new_set)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
print(A & B)
print(A - B)