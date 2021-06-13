my_list = [1, "Robert", 3, "Kriszta", 5]

# simple loop
for item in my_list:
    print(item)
    print(f"The item value is: {item}")

# exit loop
for item in my_list:
    if item == 3:
        break

# skip item
for item in my_list:
    if item == 3:
        continue
    print(item)

print("End of code")