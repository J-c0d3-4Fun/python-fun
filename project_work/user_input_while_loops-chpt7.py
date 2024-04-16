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










