#change the case of the words in a string
name = "ada lovelace"
print(name.title())


# The variable name refers to the lowercase string "ada lovelace".
# The method title() appears after the variable in the print() call. 
# A method is an action that Python can perform on a piece of data. The dot (.) after name in name.title() tells Python to make the title() method act on the variable name.
# Every method is followed by a set of parentheses, because methods often need additional information to do their work. That information is provided inside the parentheses. 
# The title() function doesn’t need any additional information, so its parentheses are empty


# You can change a string to all uppercase or all lowercase
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#The lower() method is particularly useful for storing data.