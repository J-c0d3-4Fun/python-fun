#Try it yourself

# 2-3. Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

first_name = "eric"
last_name = "taylor"
full_name = f"{first_name} {last_name}"
message = f"Hello {full_name.title()}, would you like to learn some Python today?"
print(message)




# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.
first_name = "JAMES"
last_name = "BOND"
full_name = f"{first_name} {last_name}"
print(full_name.lower())

first_name = "james"
last_name = "bond"
full_name = f"{first_name} {last_name}"
print(full_name.upper())

first_name = "james"
last_name = "bond"
full_name = f"{first_name} {last_name}"
print(full_name.title())



# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never
# tried anything new.”

first_name = "thomas"
last_name = "edison"
full_name = f"{first_name} {last_name}"
quote = "I have not failed. I have just found 10,000 ways that won't work"
print(f"{full_name.title()} once said, {quote}")

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
# person’s name using a variable called famous_person. Then compose your message
# and represent it with a new variable called message. Print your message.
famous_person = "thomas edison"
message = "once said, I have not failed. I have just found 10,000 ways that won't work"
print(f"{famous_person.title()} {message}")


# 2-7. Stripping Names: Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().
name = "      \tjimmy          .    \nnuetron"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 2-8. File Extensions: Python has a removesuffix() method that works exactly
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called
# filename. Then use the removesuffix() method to display the filename without
# the file extension, like some file browsers do.
filename = 'python_notes.txt'
print(f"{filename.removesuffix('txt')}")