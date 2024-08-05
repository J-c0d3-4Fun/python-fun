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

# Accessing a File's Line



