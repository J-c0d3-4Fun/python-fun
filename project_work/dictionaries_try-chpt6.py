# TRY IT YOURSELF


# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each piece
# of information stored in your dictionary.

person = {'first_name': 'michael', 'last_name': 'scott', 'age': 40, 'city': 'scranton'}
print(person['first_name'])
print(person['last_name'])
print(person['city'])
print(person['age'])
# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favorite_numbers ={
    'tim': 4,
    'james': 23,
    'angela': 7,
    'pam': 45,
    'dwight': 10000
}

print(favorite_numbers['tim'])
print(favorite_numbers['james'])
print(favorite_numbers['angela'])
print(favorite_numbers['pam'])
print(favorite_numbers['dwight'])

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    'dictionary': 'dictionary :is a collection of key-value pairs.',
    'key-value pair': 'key-value pair :is a set of values associated with each other.',
    'key': 'key :is connected to a value, and you can use a key to access the value associated with that key',
    'blank lines': 'blank lines :group parts of your program visually, use blank lines',
    'list': 'list :is a collection of itmes in a particular order'
}

print(f" I've learned so much from the Python learning, here are some definitions. \n{glossary['blank lines']}. \n{glossary['dictionary']}. \n{glossary['key']}. \n{glossary['key-value pair']}. \n{glossary['list']} ")


# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = {
    'dictionary': 'is a collection of key-value pairs.',
    'key-value pair': 'is a set of values associated with each other.',
    'key': 'is connected to a value, and you can use a key to access the value associated with that key',
    'blank lines': 'group parts of your program visually, use blank lines',
    'list': 'is a collection of itmes in a particular order',
    'loops': 'When you want to do the same action with every item in a list, you can use Python’s for loop',
    'float': 'any number with a decimal point a float.',
    'integer': 'You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.',
    'constant': 'A constant is a variable whose value stays the same throughout the life of a program',
    

}

for words in glossary.items():
    print(words)




# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {'nile': 'egypt', 'yangtze': 'beijing', 'bow': 'canada'}

for r,c in rivers.items():
    print(f"\n{r} runs through {c}")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# 6-6. Polling: Use the code in favorite_languages.py (page 96).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

take_poll = {'timmy', 'sarah', 'phil', 'lucy', 'chad'}

for name in take_poll:
    if name not in set(favorite_languages):
        print(f"{name.title()} take the poll please!")
    else:
        print(f"Thank you {name.title()} for taking our poll!") 



# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionaries
# in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.
   
person_1 = {'first name': 'michael', 'last name': 'scott', 'age': 40, 'city': 'scranton',}
person_2 = {'first name': 'dwight', 'last name': 'schrute', 'age': 45, 'city': 'beet farms',}
person_3 = {'first name': 'Jim', 'last name': 'halpert', 'age': 35, 'city': 'scranton'}

people = [person_1, person_2, person_3]

for person in people:
    print(person)





# 6-8. Pets: Make several dictionaries, where each dictionary represents a different
# pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.
pet_1 = {'animal': 'dog', 'owner': 'jim'}  
pet_2 = {'animal': 'cat', 'owner': 'dwight'}
pet_3 = {'animal': 'bird', 'owner': 'michael'}  

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(pet)


# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places for
# each person. To make this exercise a bit more interesting, ask some friends to
# name a few of their favorite places. Loop through the dictionary, and print each
# person’s name and their favorite places.
    
favorite_places = {
    'paul': ['canada', 'orlando'],
    'christine': ['texas', 'japan'], 
    'james': ['africa']
    }

for name, place in favorite_places.items():
    print(f"\n{name.title()}'s favorite place to visit are: ")
    print(f"\t{place}")

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_numbers ={
    'tim': [4, 25, 44],
    'james': [23, 32, 33],
    'angela': [7, 14, 21],
    'pam': [45, 65, 105],
    'dwight': [10000, 1000000, 10000000]
}

for name, number in favorite_numbers.items():
    print(f"\n{name.title()} favorite numbers are listed here:")
    print(f"{number}")


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.
    
cities = {'atlanta': '', 'charlotte': '', 'los angeles': ''}
# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program, or improving the formatting of the output.



