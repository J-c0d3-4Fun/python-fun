# TRY IT YOURSELF


# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

pizza = 'cheese'
print("Is pizza == 'cheese'? I predict True " )
print(pizza == 'cheese' )

pizza = 'pineapple'
print("\nIs pizza == 'anchovies'? I predict False " )
print(pizza == 'anchovies')


pizza = 'chicken'
print("\nIs pizza == 'chicken'? I predict True " )
print(pizza == 'chicken')

pizza = 'veggie'
print("\nIs pizza == 'cheese'? I predict False " )
print(pizza == 'cheese')

pizza = 'double cheese'
print("\nIs pizza == 'double cheese'? I predict True " )
print(pizza == 'double cheese')

city = 'atlanta'


# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create
# to 10. If you want to try more comparisons, write more tests and add them
# to conditional_tests.py. Have at least one True and one False result for each of
# the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

#inequality testing
car = 'bmw'
print(car == 'audi')

town = 'atlanta'
print(town == 'atlanta')

#lower method
town = 'Atlanta'
print(town.lower())

#numerical values
hour = 5
minute = 19

if hour > 6:
      print("its getting late")
else:
      print("its too early to goto bed")

if minute < 25:
      print("what time is it?")

if hour <= 6:
    print("it's time to goto sleep")

if minute >= 8:
        print("the clock is moving slow")

#OR

time = 5
money = 100

time <= 2 or money >= 100

#list test
city = ['atlanta', 'stone mountain', 'lithonia']
'atlanta' in city
'conyers' in city







# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)
alien_color = 'green'
if 'green' in alien_color:
      print("You earned 5 points!")

if 'red' in alien_color:
      print("")



# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
# and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned 5
# points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# • Write one version of this program that runs the if block and another that
# runs the else block.

alien_color = 'red'
if 'red' in alien_color:
      print("you earned 5 points!")
else:
    print("you've earned 10 points!") 
      
alien_color = 'green'
if 'red' in alien_color:
      print("you earned 5 points!")
else:
    print("you've earned 10 points!") 



# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
# chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.
alien_color = 'green'
if alien_color == 'green':
      print("you have earned 5 points!")
elif alien_color == 'yellow':
      print("You have earned 10 points!")
else: 
      print("You have earned 15 points!")

alien_color = 'yellow'
if alien_color == 'green':
      print("you have earned 5 points!")
elif alien_color == 'yellow':
      print("You have earned 10 points!")
else: 
      print("You have earned 15 points!")

alien_color = 'red'
if alien_color == 'green':
      print("you have earned 5 points!")
elif alien_color == 'yellow':
      print("You have earned 10 points!")
else: 
      print("You have earned 15 points!")
      





# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage
# of life. Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is
# a baby.
# • If the person is at least 2 years old but less than 4, print a message that the
# person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# • If the person is age 65 or older, print a message that the person is an elder.
      
age = 22
if age < 2:
      print("your a baby")
elif age  < 4:
      print("your a toddler")
elif age < 13: 
      print("your a kid")
elif age < 20:
      print("your a teenager")
elif age <65:
      print("your an adult")
else:
      print("your an elder")



# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!


fruit = ['apples', 'strawberries', 'blueberries', 'grapes']
if 'apples' in fruit:
      print(f"I really like {fruit[0]}")

if 'pineapples' in fruit:
      print(f"I really like pineapples")

if 'blueberries' in fruit:
      print(f"I really like {fruit[2]}")

if 'grapes' in fruit:
      print(f"I really like {fruit[3]}")

if 'cherries' in fruit:
      print('I really like cherries')


# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user.
# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.

usernames = ['jaden', 'will', 'jim', 'dave', 'admin']

for users in usernames:
      if users == 'admin' :
            print(f"Hello {users.title()}, would you like to see a status report?")
      else:
            print(f"Hello {users.title()}, welcome back to the dashboard")

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message
# is printed.
usernames = [ ]

if usernames:
    for users in usernames:
        if users == 'admin' :
                print(f"Hello {users.title()}, would you like to see a status report?")
        else:
                print(f"Hello {users.title()}, welcome back to the dashboard")
else:
      print("We need to find some users!")




# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)

current_users = ['jaden', 'will', 'jim', 'dave', 'tom']
new_users = ['jaden', 'tammy', 'timmy', 'josh', 'tom']

for users in new_users:
      if users in current_users:
            print("You will need to enter a new username!")
        
      else: 
            print(f"That username is available!")



# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as
# 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending
# for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th
# 8th 9th", and each result should be on a separate line.

ordinal = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]

for numbers in ordinal:
    if numbers == 1:
        print(f"1st")
    elif numbers == 2:
        print(f"2nd")
    elif numbers == 3:
        print(f"3rd")
    else:
          print(f"{numbers}th")


