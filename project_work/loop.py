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






