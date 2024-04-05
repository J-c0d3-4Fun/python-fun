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

