#The following example shows how if tests let you respond to special situations correctly.
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


#Conditional Tests
#At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test. 
#Python uses the values True and False to decide whether the code in an if statement should be executed. 
#If a conditional test evaluates to True, Python executes the code following the if statement. If the test evaluates to False, Python ignores the code following the if statement.

car = 'bmw'
car == 'bmw'

#A double equal sign (==) equality operator returns True if the values on the left and right side of the operator match, and False if they don’t match.
# The values in this example match, so Python returns True.
# When the value of car is anything other than 'bmw', this test returns False

#Ignoring case when checking for equality
#two values with different capitalization are not considered equal

car = 'Audi'
car = 'audi'

#if case doesn’t matter and instead you just want to test the value of a variable, you can convert the variable’s value to lowercase before doing the comparison

car = 'Audi'
car.lower() == 'audi'

#The lower() method doesn’t change the value that was originally stored in car, so you can do this kind of comparison without affecting the original variable

#Checking for Inequality
#When you want to determine whether two values are not equal, you can use the inequality operator (!=)

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Numerical Comparisons
age = 18
age == 18

#You can also test to see if two numbers are not equal

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

#You can include various mathematical comparisons in your conditional statements as well, such as less than, less than or equal to, greater than, and greater than or equal to

age = 19
age < 21

age <= 21

age > 21

age >= 21

# Checking Multiple Conditions
# using and to Check Multiple Conditions
#To check whether two conditions are both True simultaneously, use the keyword and to combine the two conditional tests; if each test passes, the overall expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

age_1 = 22
age_0 >= 21 and age_1 >= 21

#using or to Check Multiple Conditions
#The keyword or allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass. An or expression fails only when both individual tests fail

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

age_0 = 18
age_0 >= 21 or age_1 >= 21

#Checking whether a Value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

'pepperoni' in requested_toppings

#Checking Whether a value is Not in a List

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

#Boolean Expressions
#A Boolean expression is just another name for a conditional test. A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.

game_active = True
can_edit = False

#Boolean values provide an efficient way to track the state of a program or a particular condition that is important in your program.


#If Statements
#simple if statements
#The simplest kind of if statement has one test and one action

age = 19
if age >= 18:
    print("You are old enough to vote!")

#All indented lines after an if statement will be executed if the test passes, and the entire block of indented lines will be ignored if the test does not pass.


age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#if else statements
# Python’s if-else syntax makes this possible. An if-else block is similar to a simple if statement, but the else statement allows you to define an action or set of actions that are executed when the conditional test fails.

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote")
    print("Please register to vote as soon as you turn 18!")
# The if-else structure works well in situations in which you want Python to always execute one of two possible actions.

#if-elif-else Chain
# Often, you’ll need to test more than two possible situations, and to evaluate these you can use Python’s if-elif-else syntax. 
#Python executes only one block in an if-elif-else chain. It runs each conditional test in order, until one passes. 
# When a test passes, the code following that test is executed and Python skips the rest of the tests.

age = 12
if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40")

#if-elif-else chain
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

#Using Multiple elif Blocks

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

#Omitting the else Block
#Python does not require an else block at the end of an if-elif chain. Sometimes, an else block is useful. Other times, it’s clearer to use an additional elif statement that catches the specific condition of interest

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:    #<---- elif ends the loop
    price = 20

print(f"Your admission cost is ${price}.")

#The else block is a catchall statement. It matches any condition that wasn’t matched by a specific if or elif test, and that can sometimes include invalid or even malicious data. 
#If you have a specific final condition you’re testing for, consider using a final elif block and omit the else block. 
#As a result, you’ll be more confident that your code will run only under the correct conditions.

#Testing Multiple Conditions
#sometimes it’s important to check all conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks.
#This technique makes sense when more than one condition could be True, and you want to act on every condition that is True.

requested_toppings = ['mushroom', 'extra cheese' ]

if 'mushroom' in requested_toppings:
    print('Adding mushrooms')

if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')


if 'extra cheese' in requested_toppings:
    print('extra cheese')

print("\nFinished making your pizza!")


# Using if statements with List

requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

#Checking that a list is not empty

requested_toppings = []

if requested_toppings: 
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
#When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False.

#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requesting_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
else: 
    print(f"Sorry, we don't have {requested_topping}")

print("\nFinished making your pizza!")
    

















































