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

#Use a variable’s value inside a string
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#To insert a variable’s value into a string, place the letter f immediately before the opening quotation mark.
#Put braces around the name or names of any variable you want to use inside the string. 
#Python will replace each variable with its value when the string is displayed
#These strings are called f-strings.
#The f is for format, because Python formats the string by replacing the name of any variable in braces with its value.

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)


#In programming, whitespace refers to any nonprinting characters, such as spaces, tabs, and end-of-line symbols. 
#You can use whitespace to organize your output so it’s easier for users to read


#To add a tab to your text, use the character combination \t:
print("\tPython")


#To add a newline in a string, use the character combination \n:
print("Languages:\nPython\nC\nJavaScript")

#You can also combine tabs and newlines in a single string. 
#The string "\n\t" tells Python to move to a new line, and start the next line with a tab.
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Python can look for extra whitespace on the right and left sides of a string. 

#To ensure that no whitespace exists at the right side of a string, use the rstrip() method:
favorite_langauge = 'python '
favorite_langauge.rstrip()

#Remove Prefix
#Enter the name of the variable followed by a dot, and then the method removeprefix().

nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')

#When you see a URL in an address bar and the https:// part isn’t shown, the browser is probably using a method like removeprefix() behind the scenes.








