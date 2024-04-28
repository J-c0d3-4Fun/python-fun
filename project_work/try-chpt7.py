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
number = 13

while True:
    if number < 25:
        print(number)



# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for each order, such as I made
# your tuna sandwich. As each sandwich is made, move it to the list of finished
# sandwiches. After all the sandwiches have been made, print a message listing
# each sandwich that was made.

sandwich_orders = ['grilled cheese', 'turkey', 'tuna', 'chicken', 'chicken salad']
finished_sandwiches = [ ]

#takes the sandwich out of the sandwich_orders list and puts it into th finished sandwiches
while sandwich_orders:
    orders = sandwich_orders.pop()
    
    print(f"I made your {orders.title()} sandwich!")
    finished_sandwiches.append(orders)
    
print(f"these are all the order's I've completed: ")    
for finished in finished_sandwiches:
   print(f" {finished.title()}")

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['pastrami','grilled cheese', 'turkey','pastrami', 'tuna', 'chicken', 'chicken salad', 'pastrami']
finished_sandwiches = [ ]

print("Unfortunately we've run out of pastrami sandwiches")
# removing pastrami from the list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#takes the sandwich out of the sandwich_orders list and puts it into th finished sandwiches
while sandwich_orders:
    orders = sandwich_orders.pop()
    
    print(f"I made your {orders.title()} sandwich!")
    finished_sandwiches.append(orders)
    
print(f"these are all the order's I've completed: ")    
for finished in finished_sandwiches:
   print(f" {finished.title()}")



# 7-10. Dream Vacation: Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

responses = { }

prompt = "If you could visit one place in the world, where would you go? "

polling_active = True

while polling_active:
    name = input("What is your name? ")
# ask the user a question
    question = prompt
    response = input(prompt)
#stores the response
    responses[name] = response
# ask if they want to add to the list of dream vacations
    repeat = input("Do you want to add to the list of Dream vacations? ")
    if repeat == 'no':
        polling_active = False

print("Dream Vacation Choices: ")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}")