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






























