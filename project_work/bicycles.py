bicycles = [ 'trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
# you can access any element in a list by telling Python the position, or index, of the item desired
# To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.
# i.e. print(bicycles[0])

bicycles = [ 'trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# You can also use the string methods on any element in this list.
bicycles = [ 'trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

#If you ask for the item at index -1, Python always returns the last item in the list
bicycles = [ 'trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1].title())

# This convention extends to other negative index values as well. 
# The index -2 returns the second item from the end of the list, the index -3 returns the third item from the end, and so forth.

#Using Individual Values from a List
#You can use f-strings to create a message based on a value from a list.
bicycles = [ 'trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)













