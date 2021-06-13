data_file = "user_data.txt"


user_name = input("Your name?")
user_age = input("Your age?")

# write data into file
with open(data_file, "a") as f:
    f.write(f"\n\nUsername: {user_name}\nUser age: {user_age}")

# read data from file
with open(data_file) as f:
    print(f.read())

# old style file handling
# # w= write/owerride a=append r=read
# f = open(data_file, "a")
# f.write(f"\n\nUsername: {user_name}\nUser age: {user_age}")
# f.close()

# read file
# f = open(data_file)
# print(f.read())
# f.close()

