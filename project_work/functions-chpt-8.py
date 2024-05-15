# Defining a Function

# Simple function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# The first line
# uses the keyword def to inform Python that you’re defining a function. This
# is the function definition, which tells Python the name of the function and, if
# applicable, what kind of information the function needs to do its job. The
# parentheses hold that information. In this case, the name of the function is
# greet_user(), and it needs no information to do its job, so its parentheses are
# empty. (Even so, the parentheses are required.) Finally, the definition ends
# in a colon.
# Any indented lines that follow def greet_user(): make up the body of the
# function. The text on the second line is a comment called a docstring, which
# describes what the function does. When Python generates documentation
# for the functions in your programs, it looks for a string immediately after
# the function's definition. These strings are usually enclosed in triple quotes,
# which lets you write multiple lines.
# The line print("Hello!") is the only line of actual code in the body of
# this function, so greet_user() has just one job: print("Hello!").
# When you want to use this function, you have to call it. A function call
# tells Python to execute the code in the function. To call a function, you write
# the name of the function, followed by any necessary information in parentheses.


# Passing Information to a Function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# If you modify the function greet_user() slightly, it can greet the user by
# name. For the function to do this, you enter username in the parentheses of
# the function’s definition at def greet_user(). By adding username here, you
# allow the function to accept any value of username you specify. The function
# now expects you to provide a value for username each time you call it. When
# you call greet_user(), you can pass it a name, such as 'jesse', inside the
# parentheses


# Arguments and Parameters 
# The variable username in the definition of greet_user() is an example of a
# parameter, a piece of information the function needs to do its job. The value
# 'jesse' in greet_user('jesse') is an example of an argument. An argument is
# a piece of information that’s passed from a function call to a function.
# When we call the function, we place the value we want the function to work
# with in parentheses. In this case the argument 'jesse' was passed to the
# function greet_user(), and the value was assigned to the parameter username.



# Passing Arguments

#Posistional Arguments

# When you call a function, Python must match each argument in the function call with a parameter in the function definition. 
# The simplest way to do this is based on the order of the arguments provided. 
# Values matched up this way are called positional arguments.

def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')

# The definition shows that this function needs a type of animal and the animal’s name 1. 
# When we call describe_pet(), we need to provide an animal type and a name, in that order. 
# For example, in the function call, the argument 'hamster' is assigned to the parameter animal_type and the argument 'harry' is assigned to the parameter pet_name 2. 
# In the function body, these two parameters are used to display information about the pet being described.


# Multiple Function Calls
# You can call a function as many times as needed

def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog', 'willie')


# Calling a function multiple times is a very efficient way to work. The
# code describing a pet is written once in the function. Then, anytime you
# want to describe a new pet, you call the function with the new pet’s information.
# Even if the code for describing a pet were to expand to 10 lines, you
# could still describe a new pet in just one line by calling the function again.


# Keyword Arguments

# A keyword argument is a name-value pair that you pass to a function. You
# directly associate the name and the value within the argument, so when you
# pass the argument to the function, there’s no confusion (you won’t end up
# with a harry named Hamster). Keyword arguments free you from having
# to worry about correctly ordering your arguments in the function call, and
# they clarify the role of each value in the function call.

def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster',pet_name='harry')

# The order of keyword arguments doesn’t matter because Python knows where each value should go.

#Default Values

# When writing a function, you can define a default value for each parameter. 
# If an argument for a parameter is provided in the function call, Python uses the argument value. 
# If not, it uses the parameter’s default value. 
# So when you define a default value for a parameter, you can exclude the corresponding argument you’d usually write in the function call. 
# Using default values can simplify your function calls and clarify the ways your functions are typically used.

def describe_pet(pet_name, animal_type='dog'):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# Note that the order of the parameters in the function definition had to be changed. 
# Because the default value makes it unnecessary to specify a type of animal as an argument, the only argument left in the function call is the pet’s name. 
# Python still interprets this as a positional argument, so if the function is called with just a pet’s name, 
# that argument will match up with the first parameter listed in the function’s definition.
# This is the reason the first parameter needs to be pet_name.

# The simplest way to use this function now is to provide just a dog’s
# name in the function call

describe_pet('willie')

# NOTE When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don’t have default values. This allows Python to continue
# interpreting positional arguments correctly


# Equivalent Function Calls

# Because positional arguments, keyword arguments, and default values can
# all be used together, you’ll often have several equivalent ways to call a function.



def describe_pet(pet_name, animal_type='dog'):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Each of these function calls would have the same output as the previous
# examples.
# It doesn’t really matter which calling style you use. As long as your function
# calls produce the output you want, just use the style you find easiest to
# understand.



# Avoiding Argument Errors
# When you start to use functions, don’t be surprised if you encounter errors about unmatched arguments. 
# Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work.

def describe_pet(pet_name, animal_type='dog'):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()

# Return Values
# A function doesn’t always have to display its output directly. Instead, it can
# process some data and then return a value or set of values. The value the
# function returns is called a return value. The return statement takes a value
# from inside a function and sends it back to the line that called the function.
# Return values allow you to move much of your program’s grunt
# work into functions, which can simplify the body of your program.

# Returning a Simple Value 
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# The function combines these two names, adds a space between
# them, and assigns the result to full_name 1. 
# The value of full_name is converted to title case, and then returned to the calling line 2.
# When you call a function that returns a value, you need to provide a
# variable that the return value can be assigned to. In this case, the returned
# value is assigned to the variable musician 3.

# Making an Argument Optional
# Sometimes it makes sense to make an argument optional, 
# so that people using the function can choose to provide extra information only if they want to. 
# You can use default values to make an argument optional.


def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# But middle names aren’t always needed, 
# and this function as written would not work if you tried to call it with only a first name and a last name. 
# To make the middle name optional, we can give the middle_name argument an empty default value 
# and ignore the argument unless the user provides a value. 
# To make get_formatted_name() work without a middle name,
# we set the default value of middle_name to an empty string and move it to the end of the list of parameters

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# In the body of the function, we check to see if a middle name has been
# provided. Python interprets non-empty strings as True, so the conditional
# test if middle_name evaluates to True if a middle name argument is in the
# function call 1. 
# If a middle name is provided, the first, middle, and last
# names are combined to form a full name. This name is then changed to
# title case and returned to the function call line, where it’s assigned to the
# variable musician and printed. If no middle name is provided, the empty
# string fails the if test and the else block runs 2. 
# The full name is made
# with just a first and last name, and the formatted name is returned to the
# calling line where it’s assigned to musician and printed.
# Calling this function with a first and last name is straightforward. If
# we’re using a middle name, however, we have to make sure the middle
# name is the last argument passed so Python will match up the positional
# arguments correctly 3.

# Returning a Dictionary

def build_person(first_name, last_name):
    """Return a dictionary of informatiion about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# The function build_person() takes in a first and last name, and puts
# these values into a dictionary 1. The value of first_name is stored with the
# key 'first', and the value of last_name is stored with the key 'last'. Then,
# the entire dictionary representing the person is returned 2. The return
# value is printed 3 with the original two pieces of textual information now
# stored in a dictionary

# You can easily extend this function to accept optional values like a middle name, an age, an occupation, or any other information you want to store about a person.

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# We add a new optional parameter age to the function definition and assign the parameter the special value None, which is used when a variable has no specific value assigned to it. 
# You can think of None as a placeholder value. 
# In conditional tests, None evaluates to False. If the function call includes a value for age, that value is stored in the dictionary.
# This function always stores a person’s name, but it can also be modified to store any other information you want about a person.


# using a Function with a while loop 

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#This is an ifinte loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input('Last name: ')

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")



# For this example, we use a simple version of get_formatted_name() that doesn’t involve middle names. 
# The while loop asks the user to enter their name, and we prompt for their first and last name separately 1.
# But there’s one problem with this while loop: We haven’t defined a quit condition. 
# Where do you put a quit condition when you ask for a series of
# inputs? We want the user to be able to quit as easily as possible, so each
# prompt should offer a way to quit. The break statement offers a straightforward
# way to exit the loop at either prompt

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True: 
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}")

# Passing a list
# You’ll often find it useful to pass a list to a function, whether it’s a list of names, numbers, or more complex objects, such as dictionaries. 
# When you pass a list to a function, the function gets direct access to the contents of the list. 
# Let’s use functions to make working with lists more efficient.

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)




