#How the input() Function Works

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# The input() function takes one argument: the prompt that we want to
# display to the user, so they know what kind of information to enter. In this
# example, when Python runs the first line, the user sees the prompt Tell me
# something, and I will repeat it back to you: . The program waits while the
# user enters their response and continues after the user presses ENTER. The
# response is assigned to the variable message, then print(message) displays the
# input back to the user

#Writing Clear Prompts
# Each time you use the input() function, you should include a clear, easy-tofollow
# prompt that tells the user exactly what kind of information you’re
# looking for. Any statement that tells the user what to enter should work.

name = input("Please enter your name: ")
print(f"\nHello, {name}!")


# Add a space at the end of your prompts (after the colon in the preceding
# example) to separate the prompt from the user’s response and to make
# it clear to your user where to enter their text.


# Sometimes you’ll want to write a prompt that’s longer than one line.
# For example, you might want to tell the user why you’re asking for certain
# input. You can assign your prompt to a variable and pass that variable to the
# input() function. This allows you to build your prompt over several lines,
# then write a clean input() statement.

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")


# This example shows one way to build a multiline string. The first line
# assigns the first part of the message to the variable prompt. In the second
# line, the operator += takes the string that was assigned to prompt and adds
# the new string onto the end.
# The prompt now spans two lines, again with space after the question
# mark for clarity

#Using int() to Accept Numerical Input
# When you use the input() function, Python interprets everything the user
# enters as a string.

age = input("How old are you? ")

# if you try to use the input as a number, you’ll get an error:

age = input("How old are you? ")

age >= 18

# When you try to use the input to do a numerical comparison , Python
# produces an error because it can’t compare a string to an integer: the string
# '21' that’s assigned to age can’t be compared to the numerical value 18.


# We can resolve this issue by using the int() function, which converts the input string to a numerical value. This allows the comparison to run successfully

age = input("How old are you? ")

age = int(age)
age >= 18

# In this example, when we enter 21 at the prompt, Python interprets the number as a string, but the value is then converted to a numerical representation by int() 1. Now Python can run the conditional test: it compares age (which now represents the numerical value 21) and 18 to see if age is greater than or equal to 18. This test evaluates to True.


# How do you use the int() function in an actual program? Consider a program that determines whether people are tall enough to ride a roller coaster

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# When you use numerical input to do calculations and comparisons, be sure to convert the input value to a numerical representation first.


# The Modulo Operator
# A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder

4 % 3

5 % 3

6 % 3

7 % 3

# The modulo operator doesn’t tell you how many times one number fits
# into another; it only tells you what the remainder is.


# When one number is divisible by another number, the remainder is 0,
# so the modulo operator always returns 0. You can use this fact to determine
# if a number is even or odd

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThenumber {number} is even.")
else:
    print(f"\nThe number {number} is odd. ")

# Even numbers are always divisible by two, so if the modulo of a number
# and two is zero (here, if number % 2 == 0) the number is even. Otherwise,
# it’s odd.


# Introducing while loops
# The for loop takes a collection of items and executes a block of code once
# for each item in the collection. In contrast, the while loop runs as long as, or
# while, a certain condition is true.


# You can use a while loop to count up through a series of numbers
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# (The += operator is shorthand for current_number = current_number + 1.)

# Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program"

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# We first define a prompt that tells the user their two options: entering a message or entering the quit value (in this case, 'quit'). Then we set up a variable message to keep track of whatever value the user enters. We define message as an empty string, "", so Python has something to check the first time it reaches the while line. The first time the program runs and Python reaches the while statement, it needs to compare the value of message to 'quit', but no user input has been entered yet. If Python has nothing to compare, it won’t be able to continue running the program. 
# To solve this problem, we make sure to give message an initial value. Although it’s just an
# empty string, it will make sense to Python and allow it to perform the comparison
# that makes the while loop work. This while loop runs as long as the
# value of message is not 'quit'.


# This program works well, except that it prints the word 'quit' as if it
# were an actual message. A simple if test fixes this:

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program"

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)






