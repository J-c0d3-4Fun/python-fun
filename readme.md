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

Dictionaries
- A dictionary in Python is a collection of key-value pairs. 
- Each key is connected to a value, and you can use a key to access the value associated with that key. 
- A key’s value can be a number, a string, a list, or even another dictionary.
- In Python, a dictionary is wrapped in braces ({}) with a series of key-value pairs inside the braces
- A key-value pair is a set of values associated with each other. 
- When you provide a key, Python returns the value associated with that key. 
- Every key is connected to its value by a colon, and individual key-value pairs are separated
by commas. 
- You can store as many key-value pairs as you want in a dictionary.
- To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets

Nesting 
- Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called nesting. 
- You can nest dictionaries  inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary 

Input() Function
- The input() function pauses your program and waits for the user to enter some text. 
- Once Python receives the user’s input, it assigns that input to a variable to make it convenient for you to work with.

Int() Function
- converts the input string to a numerical value.
- When you use numerical input to do calculations and comparisons, be sure to convert the input value to a numerical representation first.

Modulo (%)
-  The modulo operator doesn’t tell you how many times one number fits into another
- It only tells you what the remainder is.

For Loops
- The for loop takes a collection of items and executes a block of code once for each item in the collection.
- A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the items in the list. 

While Loops
- The while loop runs as long as, or
while, a certain condition is true.
- You can use a while loop to count up through a series of numbers
- To modify a list as you work through it, use a while loop. Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.

Flag
- acts as a signal to the program.

Function
- are named blocks of code designed to do one specific job. 
- When you want to perform a particular task that you’ve
defined in a function, you call the function responsible
for it.

Arguments
- An argument is a piece of information that’s passed from a function call to a function.
- You can pass arguments to your functions
in a number of ways. 
        - You can use positional arguments, which need to be in
the same order the parameters were written;
                - You can get unexpected results if you mix up the order of the arguments in
                a function call when using positional arguments
        - keyword arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values.
                - a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion

Parameters
- parameter, a piece of information the function needs to do its job.


Slice Notation
- The slice notation [:] makes a copy of the list to send to the function.


Classes
- Object-oriented programming (OOP) is one of
the most effective approaches to writing
software. 
- In object-oriented programming,
you write classes that represent real-world things
and situations, and you create objects based on these
classes. 
- When you write a class, you define the general
behavior that a whole category of objects can have.
- Making an object from a class is called instantiation, and you work with
instances of a class.
- A function that’s part of a class is a method
- Variables that are accessible through instances are called attributes.
- The name super comes from a convention of calling the parent class a superclass and the child class a subclass.

The Python Standard Library
- The Python standard library is a set of modules included with every Python installation.


Exceptions
- special objects Python creates to manage errors that arise while a program is running.
- Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object.
- Exceptions are handled with try-except blocks
- A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised.

