Python Notes

Variable names can contain only:
- lettters
- numbers
- underscores
They can start with a letter or underscore, but not with a number.

Spaces are not allowed in variable names, but underscores can be used to separate words in variable names.

Avoid using Python keywords and function names as variable names.

Variable names should be short but descriptive.

Be careful when using the lowercase l and the uppercase letter O because they could be confused with the numbers 1 and 0.

Think of variables as labeles that you can assign to values.

Integers 
- You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.
- Python uses two multiplication symbols to represent exponents "**"
- Python supports the order of operations too, so you can use multiple operations in one expression. 
- You can also use parentheses to modify the order of operations so Python can evaluate your expression in the order you specify.


Floats 
- Python calls any number with a decimal point a float. 
- This term is used in most programming languages, and it refers to the fact that a decimal point can appear at any position in a number.
- When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float. 

(Python - defaults to a float in any operation that uses a float, even if the output is a whole number.)

Underscores in Numbers 
- When you print a number that was defined using underscores, Python prints only the digits 
- i.e. universe_age = 14_000_000_000

Mulltiple Assignemnet 
- You can assign values to more than one variable using just a single line ofcode. 
- This can help shorten your programs and make them easier to read; you’ll use this technique most often when initializing a set of numbers.
- i.e. x, y, z = 0, 0, 0
- You need to separate the variable names with commas, and do the same with the values, and Python will assign each value to its respective variable.
- As long as the number of values matches the number of variables, Python will match them up correctly.


Constant 
- A constant is a variable whose value stays the same throughout the life of a program
- Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed

(When you want to treat a variable as a constant in your code, write the name of the variable in all capital letters.)


List
- is a collection of itmes in a particular order
- it’s a good idea to make the name of your list plural, such as letters, digits, or names.
- In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.
- Python considers the first item in a list to be at position 0, not position 1.
        - Using this counting system, you can get any element you want from a list by subtracting one from its position in the list.
        - If you ask for the item at index -1, Python always returns the last item in the list

Loops
- When you want to do the same action with every item in a list, you
can use Python’s for loop
- When you’re using loops for the first time, keep in mind that the set of
steps is repeated once for each item in the list, no matter how many items
are in the list.
- when writing your own for loops that you can choose
any name you want for the temporary variable that will be associated with
each value in the list.
- Any lines of code after the for loop that are not indented are executed
once without repetition.
- Python uses indentation to determine how a line, or group of lines, is related to the rest of the program.
- Always indent the line after the for statement in a loop.
- The colon at the end of a for statement tells Python to interpret the next
line as the start of a loop


Style Guide
- When someone wants to make a change to the Python language, they write a Python Enhancement Proposal (PEP).
- One of the oldest PEPs is PEP 8, which instructs Python programmers on how to style their code.
- Python programmers will almost always encourage you to write code that’s easier to read.

Indentation
- PEP 8 recommends that you use four spaces per indentation level. 
- Using four spaces improves readability while leaving room for multiple levels of indentation on each line

Line length
- Many Python programmers recommend that each line should be less than 80 characters

Blank Lines
- To group parts of your program visually, use blank lines

