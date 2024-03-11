# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.

names = [ 'goku', 'ichigo', 'jack', 'luffy']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.

names = [ 'goku', 'ichigo', 'jack', 'luffy']
print(f"Hello {names[0].title()} it is nice to see you again!")
print(f"Hello {names[1].title()} it is nice to see you again!")
print(f"Hello {names[2].title()} it is nice to see you again!")
print(f"Hello {names[3].title()} it is nice to see you again!")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

cars = ['bmw', 'mercedes', 'aston martin', 'rolls royce']
print(f"My favorite car is a {cars[0].upper()}")
print(f"I've never driven a {cars[1].title()}")
print(f"I think the {cars[2].title()} looks cool!")
print(f"I want to use the {cars[3].title()} as my daily driver")