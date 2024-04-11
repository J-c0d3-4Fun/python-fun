#Simple Dictionary
#This simle dictionary stores information about a particular alien

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Now you can access either the color or the point value of alien_0. If a
# player shoots down this alien, you can look up how many points they should
# earn using code

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']

print(f"You earned {new_points} points!")

# Adding New Key-Value Pairs
# Dictionaries are dynamic structures, and you can add new key-value pairs
# to a dictionary at any time. To add a new key-value pair, you would give the
# name of the dictionary followed by the new key in square brackets, along
# with the new value.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Dictionaries retain the order in which they were defined. When you
# print a dictionary or loop through its elements, you will see the elements in
# the same order they were added to the dictionary.

# Starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Typically, you’ll use empty dictionaries when storing user-supplied data
# in a dictionary or when writing code that generates a large number of keyvalue
# pairs automatically.

#Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

#More intersting example
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Move the alien to the right
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

#Removing Key-value pairs
# When you no longer need a piece of information that’s stored in a dictionary,
# you can use the del statement to completely remove a key-value pair.
# All del needs is the name of the dictionary and the key that you want to
# remove.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Be aware that the deleted key-value pair is removed permanently.

# A Dictionary of Similar Objects
# You can also use a dictionary to store one kind of information about many objects.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

# When you know you’ll need more than one line to
# define a dictionary, press ENTER after the opening brace. Then indent the
# next line one level (four spaces) and write the first key-value pair, followed
# by a comma. From this point forward when you press ENTER, your text editor
# should automatically indent all subsequent key-value pairs to match the
# first key-value pair.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

languages = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {languages}")

# Using get() to Access Values

alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

# For dictionaries specifically, you can use the get() method to set
# a default value that will be returned if the requested key doesn’t exist.
# The get() method requires a key as a first argument. As a second optional
# argument, you can pass the value to be returned if the key doesn’t exist

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# If you leave out the second argument in the call to get() and the key doesn’t exist,
# Python will return the value None. The special value None means “no value exists.”
# This is not an error: it’s a special value meant to indicate the absence of a value.

#Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# To write a for loop for a dictionary, you create names for the two variables
# that will hold the key and value in each key-value pair. You can choose
# any names you want for these two variables. This code would work just as
# well if you had used abbreviations for the variable names
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for k, v in user_0.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

#Another Example
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {languages.title()}")

#The keys() method is useful when you don’t need to work with all of the values in a dictionary.

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())


#Alternative

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

for name in favorite_languages:
    print(name.title())

#You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if you wish.

#You can access the value associated with any key you care about inside the loop, by using the current key.

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}


friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
 
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


#You can also use the keys() method to find out if a particular person was polled.

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# The keys() method isn’t just for looping: it actually returns a sequence of
# all the keys, and the if statement simply checks if 'erin' is in this sequence.




# Looping Through a Dictionary's Keys in a Particular Order
# Looping through a dictionary returns the items in the same order they
# were inserted. Sometimes, though, you’ll want to loop through a dictionary
# in a different order.

#You can use the sorted() function to get a copy of the keys in order

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

#This tells Python to get all the keys in the dictionary and sort them before starting the loop.

# Looping Through All Values in a Dictionary
# If you are primarily interested in the values that a dictionary contains, you
# can use the values() method to return a sequence of values without any
# keys.

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# The for statement here pulls each value from the dictionary and assigns
# it to the variable language.
# This approach pulls all the values from the dictionary without checking
# for repeats. This might work fine with a small number of values, but in a
# poll with a large number of respondents, it would result in a very repetitive
# list. To see each language chosen without repetition, we can use a set. A set
# is a collection in which each item must be unique


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# When you wrap set() around a collection of values that contains duplicate
# items, Python identifies the unique items in the collection and builds a
# set from those items.

# NOTE You can build a set directly using braces and separating the elements with commas:
# >>> languages = {'python', 'rust', 'python', 'c'}
# >>> languages
# {'rust', 'python', 'c'}
# It’s easy to mistake sets for dictionaries because they’re both wrapped in braces.
# When you see braces but no key-value pairs, you’re probably looking at a set. Unlike
# lists and dictionaries, sets do not retain items in any specific order



































