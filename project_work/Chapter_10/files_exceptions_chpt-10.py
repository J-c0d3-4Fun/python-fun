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

















