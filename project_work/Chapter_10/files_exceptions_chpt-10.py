# Read from a File 


# pi_digits.txt
3.1415926535
8979323846
2643383279

# file_reader.py

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)



# To work with the contents of a file, we need to tell Python the path to
# the file. A path is the exact location of a file or folder on a system. Python
# provides a module called pathlib that makes it easier to work with files and
# directories, no matter which operating system you or your program’s users
# are working with. A module that provides specific functionality like this is
# often called a library, hence the name pathlib.



# We start by importing the Path class from pathlib. There’s a lot you can
# do with a Path object that points to a file. For example, you can check that
# the file exists before working with it, read the file’s contents, or write new
# data to the file. Here, we build a Path object representing the file pi_digits.txt,
# which we assign to the variable path


# Since this file is saved in the same directory as the .py file we’re writing, the filename is all that Path needs to
# access the file.


# NOTE VS Code looks for files in the folder that was most recently opened. If you’re using VS
# Code, start by opening the folder where you’re storing this chapter’s programs. For
# example, if you’re saving your program files in a folder called chapter_10, press
# CTRL-O (⌘-O on macOS), and open that folder.

# Once we have a Path object representing pi_digits.txt, we use the read_text()
# method to read the entire contents of the file 2. The contents of the file are
# returned as a single string, which we assign to the variable contents. When we
# print the value of contents, we see the entire contents of the text file


# The only difference between this output and the original file is the
# extra blank line at the end of the output. The blank line appears because
# read_text() returns an empty string when it reaches the end of the file; this
# empty string shows up as a blank line.
# We can remove the extra blank line by using rstrip() on the contents
# string

from pathlib import Path
path = Path('pi_digits.txt')
contents = contents.rstrip()
print(contents)


# Recall from Chapter 2 that Python’s rstrip() method removes, or strips,
# any whitespace characters from the right side of a string.


# We can strip the trailing newline character when we read the contents
# of the file, by applying the rstrip() method immediately after calling
# read_text()

contents = path.read_text().rstrip()


# This line tells Python to call the read_text() method on the file we’re
# working with. Then it applies the rstrip() method to the string that read
# _text() returns. The cleaned-up string is then assigned to the variable
# contents. This approach is called method chaining, and you’ll see it used often
# in programming.

# Relative and Avsolute File Paths

# There are two main ways to specify paths in programming. 
# A relative file path tells Python to look for a given location relative to 
# the directory where the currently running program file is stored.

path = Path('text_files/filenamre.txt')

# You can also tell Python exactly where the file is on your computer, 
# regardless of where the program that’s being executed is stored.
# This is called an absolute file path.

# Absolute paths are usually longer than relative paths, 
# because they start at your system’s root folder

path = Path('home/eric/data_files/text_files/filename.txt')

# Using absolute paths, you can read files from any location on your system.


# NOTE Windows systems use a backslash (\) instead of a forward slash (/) when displaying file paths, 
# but you should use forward slashes in your code, even on Windows. 
# The pathlib library will automatically use the correct representation of 
# the path when it interacts with your system, or any user’s system.

# Accessing a File's Line
# You can use the splitlines() method to turn a long string into a set of
# lines, and then use a for loop to examine each line from a file, one at a time

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)


# We start out by reading the entire contents of the file, as we did earlier. 
# If you’re planning to work with the individual lines in a file, you
# don’t need to strip any whitespace when reading the file. The splitlines()
# method returns a list of all lines in the file, and we assign this list to the
# variable lines. We then loop over these lines and print each one


# Working with a File's Contents
# After you’ve read the contents of a file into memory, you can do whatever
# you want with that data

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))

# We start by reading the file and storing each line of digits in a list, just
# as we did in the previous example. We then create a variable, pi_string,
# We write a loop that adds each line of digits to
# pi_string 1. We print this string, and also show how long the string is



# The variable pi_string contains the whitespace that was on the left side of the digits in each line, 
# but we can get rid of that by using lstrip() on each line

for line in lines:
    pi_string += line.lstrip()


print(pi_string)
print(len(pi_string))


# NOTE When Python reads from a text file, it interprets all text in the file as a string. 
# If you read in a number and want to work with that value in a numerical context, 
# you’ll have to convert it to an integer using the int() function or a float using the float() function.

# Large Files: One Million Digits

from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Python has no inherent limit to how much data you can work with; you
# can work with as much data as your system’s memory can handle.

# NOTE To run this program (and many of the examples that follow), you’ll need to download
# the resources available at https://ehmatthes.github.io/pcc_3e.


# Writing to a File 

# Writing a Single Line 

# Once you have a path defined, you can write to a file using the write_text() method.

from pathlib import Path

path = Path('programming')
path.write_text("I love programming.")

# The write_text() method takes a single argument: the string that you want to write to the file. This program has no terminal output, 
# but if you open the file programming.txt, you’ll see one line.

# NOTE Python can only write strings to a text file. If you want to store numerical data
# in a text file, you’ll have to convert the data to string format first using the str()
# function

# Writing Multiple Lines 

# The write_text() method does a few things behind the scenes. If the file that
# path points to doesn’t exist, it creates that file. Also, after writing the string
# to the file, it makes sure the file is closed properly. Files that aren’t closed
# properly can lead to missing or corrupted data.
# To write more than one line to a file, you need to build a string containing
# the entire contents of the file, and then call write_text() with that string.

from pathlib import Path

contents = "I love programming. \n"
contents += "I love creating new games. \n"
contents += "I also love working with data \n"

path = Path('programming.txt')
path.write_text(contents)

# We define a variable called contents that will hold the entire contents of
# the file. On the next line, we use the += operator to add to this string. You
# can do this as many times as you need, to build strings of any length. In this
# case we include newline characters at the end of each line, to make sure
# each statement appears on its own line.

# NOTE Be careful when calling write_text() on a path object. If the file already exists,
# write_text() will erase the current contents of the file and write new contents
# to the file. Later in this chapter, you’ll learn to check whether a file exists using
# pathlib.


# Exceptions

# Python uses special objects called exceptions to manage errors that arise during a program’s execution. 
# Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object. 
# If you write code that handles the exception, the program will continue running. If you don’t handle the exception, 
# the program will halt and show a traceback, which includes a report of the exception that was raised.
# Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it also tells 
# Python what to do if an exception is raised. When you use try-except blocks, your programs will continue running even if things start to go wrong. 
# Instead of tracebacks, which can be confusing for users to read, users will see friendly error messages that you’ve written.


# Handling the ZeroDivisionError Exception

# It’s impossible to divide a number by zero

print(5/0)

# Python can’t do this, so we get a traceback:

Traceback (most recent call last):
    File "division_calculator.py", line 1, in <module>
        print(5/0)
              ~^~
ZeroDivisionError: division by zero

# The error reported in the traceback, ZeroDivisionError, is an exception object 1. Python creates this kind of object in 
# response to a situation where it can’t do what we ask it to. When this happens, 
# Python stops the program and tells us the kind of exception that was raised. We can use this information to modify our program. 
# We’ll tell Python what to do when this kind of exception occurs; that way, if it happens again, we’ll be prepared.


# Using try-except Blocks

# When you think an error may occur, you can write a try-except block to
# handle the exception that might be raised. You tell Python to try running
# some code, and you tell it what to do if the code results in a particular kind
# of exception.
# Here’s what a try-except block for handling the ZeroDivisionError exception
# looks like:

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# We put print(5/0), the line that caused the error, inside a try block. If
# the code in a try block works, Python skips over the except block. If the code
# in the try block causes an error, Python looks for an except block whose
# error matches the one that was raised, and runs the code in that block.
# In this example, the code in the try block produces a ZeroDivisionError,
# so Python looks for an except block telling it how to respond. Python then
# runs the code in that block, and the user sees a friendly error message
# instead of a traceback.

# Using Exceptions to Prevent Crashes

# Handling errors correctly is especially important when the program has
# more work to do after the error occurs. This happens often in programs
# that prompt users for input. If the program responds to invalid input appropriately,
# it can prompt for more valid input instead of crashing.
# Let’s create a simple calculator that does only division

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)




# This program prompts the user to input a first_number 1 and, if the user does not enter q to quit, a second_number 
# We then divide these two numbers to get an answer  
# This program does nothing to handle errors, so asking it to divide by zero causes it to crash



# The else Block 

--snip--

while True:
    --snip--
    if the second number == 'q':
        break
    try:
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# We ask Python to try to complete the division operation in a try block , which includes only the code that might cause an error. 
# Any code that depends on the try block succeeding is added to the else block. In this case, if the division operation is 
# successful, we use the else block to print the result.
# The except block tells Python how to respond when a ZeroDivisionError arises. If the try block doesn’t succeed because of a division-by-zero error
# we print a friendly message telling the user how to avoid this kind of error.
# The program continues to run, and the user never sees a traceback



# The only code that should go in a try block is code that might cause an
# exception to be raised. Sometimes you’ll have additional code that should
# run only if the try block was successful; this code goes in the else block.
# The except block tells Python what to do in case a certain exception arises
# when it tries to run the code in the try block.




# Handling the FileNotFoundError Exception 

# One common issue when working with files is handling missing files. The
# file you’re looking for might be in a different location, the filename might
# be misspelled, or the file might not exist at all. You can handle all of these
# situations with a try-except block.

from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8')

# Note that we’re using read_text() in a slightly different way here than
# what you saw earlier. The encoding argument is needed when your system’s
# default encoding doesn’t match the encoding of the file that’s being read.
# This is most likely to happen when reading from a file that wasn’t created
# on your system.



# Python can’t read from a missing file, so it raises an exception
Traceback (most recent call last):
    File "alice.py", line 4, in <module>
        contents = path.read_text(encoding='utf-8')
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/.../pathlib.py", line 1056, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/.../pathlib.py", line 1042, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'



# This is a longer traceback than the ones we’ve seen previously, so let’s look at how you can make sense of more complex tracebacks. 
# It’s often best to start at the very end of the traceback. On the last line, we can see that a FileNotFoundError exception was raised 3. 
# This is important because it tells us what kind of exception to use in the except block that we’ll write.
# Looking back near the beginning of the traceback 1, we can see that the error occurred at line 4 in the file alice.py. 
# The next line shows the line of code that caused the error 2. The rest of the traceback shows some code from the libraries that are 
# involved in opening and reading from files. You don’t usually need to read through or understand all of these lines in a traceback.
# To handle the error that’s being raised, the try block will begin with the line that was identified as problematic in the traceback. 
# In our example, this is the line that contains read_text()


from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist")

# In this example, the code in the try block produces a FileNotFoundError, so we write an except block that matches that error 1. 
# Python then runs the code in that block when the file can’t be found, and the result is a friendly error message instead of a traceback

# Analyzing Text

# You can analyze text files containing entire books. Many classic works of literature are available as simple text files because they are in the public domain.

# Let’s pull in the text of Alice in Wonderland and try to count the number
# of words in the text. To do this, we’ll use the string method split(), which
# by default splits a string wherever it finds any whitespace

from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# I moved the file alice.txt to the correct directory, so the try block will
# work this time. We take the string contents, which now contains the entire
# text of Alice in Wonderland as one long string, and use split() to produce a
# list of all the words in the book 1. Using len() on this list 2 gives us a good
# approximation of the number of words in the original text. Lastly, we print
# a statement that reports how many words were found in the file. This code
# is placed in the else block because it only works if the code in the try block
# was executed successfully.


# Working with Multiple Files 

# Let’s add more books to analyze, but before we do, let’s move the bulk of
# this program to a function called count_words(). This will make it easier to
# run the analysis for multiple books

from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')


















