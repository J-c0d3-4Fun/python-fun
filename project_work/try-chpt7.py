# TRY IT YOURSELF


# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

message = input("What kind of rental car would you like to purchase? ")
print(f"let me see if I can find you a {message}")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

users = input("How many people are in your dinner group? ")
users = int(users)
if users > 8:
    print("You will have to wait for a table")
else:
    print("your table is ready!")


# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

numbers = input("What is your favorite number? I will tell you if it's a multiple of ten ")

numbers = int(numbers)

if numbers % 10 == 0:
    print(f"This number is divisible by 10! ")
else:
    print(f"This number is not a  multiple of 10")