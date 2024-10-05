# TRY IT YOURSELF

# 10-1. Learning Python: Open a blank file in your text editor and write a few lines
# summarizing what you’ve learned about Python so far. Start each line with the
# phrase In Python you can. . . . Save the file as learning_python.txt in the same
# directory as your exercises from this chapter. Write a program that reads the file
# and prints what you wrote two times: print the contents once by reading in the
# entire file, and once by storing the lines in a list and then looping over each line.
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)


# 10-2. Learning C: You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as C. Print each modified line to the screen.

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
changed = contents.replace('Python','Java')
print(changed)




# 10-3. Simpler Code: The program file_reader.py in this section uses a temporary variable, lines, to show how splitlines() works. You can skip the temporary variable and loop directly over the list that splitlines() returns:
# for line in contents.splitlines():
# Remove the temporary variable from each of the programs in this section, to make them more concise.

# file_reader.py
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)

# pi_string.py
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line

print(pi_string)
print(len(pi_string))

# pi_string.py part 2
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}....")
print(len(pi_string))




# 10-4. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
from pathlib import Path

prompt = input("What is your name?: ")

path = Path('guest.txt')
path.write_text(prompt) 






# 10-5. Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, 
# and then write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file.
from pathlib import Path

contents = ''

while True:
    prompt = input("What is your name?: ")
    if prompt == '':
        break
    contents += prompt + "\n"
path = Path("guest_book.txt")
path.write_text(contents)

# 10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. 
# Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. 
# Test your program by entering two numbers and then by entering some text instead of a number.

print("I can add numbers for you!")
 
def adding():
    try:
        first = input("What is the first number you want to add?: ")
        second = input("What is the second number you want to add?: ")
        addition = int(first) + int(second)
    except ValueError:
        print("That is not an interger!")
    else:
        print(f"The answer is {addition}!")
    
adding()


# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers, even if they make a mistake and enter text instead of a number.
 
print("I can add numbers for you!")
 
def adding():
    while True:
            try:
                first = input("What is the first number you want to add?: ")
                second = input("What is the second number you want to add?: ")
                addition = int(first) + int(second)
            except ValueError:
                print("That is not an interger!")
                break
            else:
                print(f"The answer is {addition}!")
            
adding()
 
 
 
# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read 
# these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. 
# Move one of the files to a different location on your system, and make sure the code in the except block executes properly.
from pathlib import Path

def reader():
    try:
        filenames = ['cats.txt', 'dogs.txt']
        for filename in filenames:
            path = Path(filename)
            contents = path.read_text()
            print(contents)
    except FileNotFoundError:
        print('We cannot find this file')
reader()

### Option for one file
from pathlib import Path

def reading():
    try:
        path = Path('cats.txt')
        contents = path.read_text()
    except FileNotFoundError:
        print('We cannot find this file')
    else:
        print(contents)

reading()


### I created a more flexible program that allows the user to input any file
from pathlib import Path

def reading():
    try:
        q1 = input('What file are you looking for?')
        path = Path(q1)
        contents = path.read_text()
    except FileNotFoundError:
        print('We cannot find this file')
    else:
        print(contents)

reading()


# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.

from pathlib import Path

def reader():
    try:
        filenames = ['cats.txt', 'dogs.txt']
        for filename in filenames:
            path = Path(filename)
            contents = path.read_text()
            print(contents)
    except FileNotFoundError:
        
reader()


# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org ) and find a few texts you’d like to analyze. Download the text files for these works, 
# or copy the raw text from your browser into a text file on your computer.You can use the count() method to find out how many times a word or phrase appears in a string. For example, 
# the following code counts the number of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, regardless of how it’s formatted.
# Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. This will be an approximation because it will also count words such 
# as 'then' and 'there'. Try counting 'the ', with a space in the string, and see how much lower your count is.


# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number. 
# Use json.dumps() to store this number in a file. Write a separate program 
# that reads in this value and prints the message “I know your favorite
# number! It’s _____.”

from pathlib import Path
import json

def favorite_number():
    prompt = input("What is your favorite number?")
    path = Path("numbers.json")
    contents = json.dumps(prompt)
    path.write_text(contents)

favorite_number()


def read_number():
    path = Path("numbers.json")
    contents = path.read_text() 
    reading = json.loads(contents)
    print(f"I know your favorite number! It's {reading}")
    
read_number()


# 10-12. Favorite Number Remembered: Combine the two programs you wrote in Exercise 10-11 into one file. 
# If the number is already stored, report the favorite number to the user. 
# If not, prompt for the user’s favorite number and store it in a file. 
# Run the program twice to see that it works.

from pathlib import Path
import json

def favorite_number():
    """Asking for the favorite number"""
    prompt = input("What is your favorite number?")
    path = Path("numbers.json")
    contents = json.dumps(prompt)
    path.write_text(contents)
    return prompt

def read_number():
    """Reading numbers from a file"""
    path = Path("numbers.json")
    if path.exists():
        contents = path.read_text() 
        reading = json.loads(contents)
        print(f"I know your favorite number! It's {reading}")
    else:
        number = favorite_number()
        print(f"We now have stored your favorite number, {number}")

read_number()


# 10-13. User Dictionary: The remember_me.py example only stores one piece of information, the username. 
# Expand this example by asking for two more pieces of information about the user, then store all
# the information you collect in a dictionary. Write this dictionary to a file using json.dumps(), 
# and read it back in using json.loads(). Print a summary showing exactly what your program remembers about the user.

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    # contents = json.dumps(username)
    # path.write_text(contents)
    return username 

def get_location():
    """ask user where they live"""
    prompt = input("What city and state do you live in? ")
    # contents = json.dumps(prompt)
    # path.write_text(contents)
    return prompt

def get_age():
    """ask for age""" 
    prompt = input("How old are you? ")
    # contents = json.dumps(prompt)
    # path.write_text(contents)
    return prompt


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}! ")
    return username


def dictionary(path): 
    """putting info into a dictionary"""
    path = Path("dictionary.json")
    info = {}
    info['username'] = greet_user()
    info['city and state'] = get_location()
    info['age'] = get_age()
    contents = json.dumps(info) 
    path.write_text(contents)
    return_dictionary(path)
    
    
    

def return_dictionary(path):
    """returns the info in the dictionary"""
    contents = path.read_text()
    dictionary = json.loads(contents)
    print(f"This is what we currently have stored as your info: {dictionary}")
    return dictionary


dictionary('dictionary.json')


# 10-14. Verify User: The final listing for remember_me.py assumes either that the user has already 
# entered their username or that the program is running for the first time. We should modify it in 
# case the current user is not the person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user if this is the correct username. 
# If it’s not, call get_new_username() to get the correct username.

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username 

def check_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        prompt = input(f"Please confirm if this is the correct username?(y/n):{username} ")
        if prompt.lower() == 'y':
            greet_user()
        else:
            get_new_username()
        return username
    else:
        return None
    
    

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    elif username:
        check_stored_username(path)
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}! ")
    return username


greet_user()








