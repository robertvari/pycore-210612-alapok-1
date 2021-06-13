number = 11

# True
if number == 10:
    print("Number is 10")
else:
    print("Number is not equal to 10")

if number < 10:
    print("Number is less than 10")

if number > 10:
    print("Number is greater than 10")

if number != 10:
    print("Number not equal to 10")


number2 = 20

#    True             True
if number2 >= 5 and number2 <= 10:
    print("Number2 is between 5-10")

#    False             False
if number2 <= 5 or number2 >= 10:
    print("Number2 is less than 5 OR greater than 10")


if number2 == 5:
    print("Number is equal to 5")
elif number2 == 10:
    print("Number is equal to 10")
elif number2 == 20:
    print("Number is equal to 20")