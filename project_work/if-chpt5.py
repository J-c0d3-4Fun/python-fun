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















