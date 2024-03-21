#Looping allows you to take the same action, or set of actions, with every item in a list


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#It might help to read this code as “For every magician in the list of magicians, print the magician’s name.”

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

#Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Because we have indented both calls to print(), each line will be executed once for every magician in the list. 
#The newline ("\n") in the second print() call inserts a blank line after each pass through the loop.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")



#Looping with Numbers
#Using the range() function

for value in range(1, 5):
    print(value)

# In this example, range() prints only the numbers 1 through 4. This is
# another result of the off-by-one behavior you’ll see often in programming
# languages. The range() function causes Python to start counting at the first
# value you give it, and it stops when it reaches the second value you provide.
# Because it stops at that second value, the output never contains the end
# value, which would have been 5 in this case


# You can also pass range() only one argument, and it will start the
# sequence of numbers at 0. For example, range(6) would return the numbers
# from 0 through 5.

#Using range() to make a list of numbers
#to make a list of numbers, you can convert the results of range() directly into a list using the list() function. When you wrap list() around a call to the range() function, the output will be a list of numbers.

numbers = list(range(1, 6))
print(numbers)

#We can also use the range() function to tell Python to skip numbers in a given range. 
#If you pass a third argument to range(), Python uses that value as a step size when generating numbers.

even_numbers = list(range(2, 11, 2))
print(even_numbers)

#In this example, the range() function starts with the value 2 and then adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end value, 11,

#consider how you might make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10). In Python, two asterisks (**) represent exponents

squares = [ ]
for value in range (1,11 ):
    square = value ** 2
    squares.append(square)

print(squares)

#To write this code more concisely, omit the temporary variable square and append each new value directly to the list

squares = [ ]
for value in range(1, 11):
    squares.append(value**2)

print(squares)

#A few Python functions are helpful when working with lists of numbers. 
#For example, you can easily find the minimum, maximum, and sum of a list of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

#A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
squares = [value**2 for value in range(1, 11)]
print(squares)

#slicing a list
#a specific group of items in a list, called a slice in Python.
#To make a slice, you specify the index of the first and last elements you want to work with. As with the range() function, Python stops one item before the second index you specify.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

#If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

# A similar syntax works if you want a slice that includes the end of a list.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

# Note - You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.

#looping through a slice
#You can use a slice in a for loop if you want to loop through a subset of the elements in a list.

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())

#copying a list
# To copy a list, you can make a slice that includes the entire original list
# by omitting the first index and the second index ([:]). This tells Python to
# make a slice that starts at the first item and ends with the last item, producing
# a copy of the entire list.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#tuples
#Python refers to values that cannot change as immutable, and an immutable list is called a tuple
# A tuple looks just like a list, except you use parentheses instead of square brackets. 
# Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Note - Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma:
my_t = (3,)

#looping through all values in a tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#Writing over a tuple
#Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#When compared with lists, tuples are simple data structures. Use them when you want to store a set of values that should not be changed throughout the life of a program.


