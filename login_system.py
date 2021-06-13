username = "robert"
password = "testpas123"

user_name = input("Username:")
user_password = input("Password:")


if user_name == username and user_password == password:
    print(f"You are logged in {username}.")
else:
    print("Invalid credentials.")