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



# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

prompt = "What toppings would you like on your pizza?"
prompt += "\n(Enter 'quit' when you have completed your order)"

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:   
        print(f"we will be adding {toppings.title()} to your pizza!")
# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

prompt = "Welcome to the movie theater"
prompt += "\nWhat is your age?"

while True:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("Your ticket is free!")
    elif age < 12:
        print("the ticket is $10")
    else: 
        print("your ticket is $15")
        



# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
# each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.
prompt = "What's your favorite city?"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I would love to visit {city.title()}")



# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
# CTRL-C or close the window displaying the output.

prompt = "enter a number"
number = input(prompt)
number = int(number)




