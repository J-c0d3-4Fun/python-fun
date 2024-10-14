# While Python includes a lot of functionality in the standard library, Python
# developers also depend heavily on third-party packages. A third-party package
# is a library that’s developed outside the core Python language. Some popular
# third-party libraries are eventually adopted into the standard library,
# and end up being included in most Python installations from that point
# forward. This happens most often with libraries that are unlikely to change
# much once they’ve had their initial bugs worked out. These kinds of libraries
# can evolve at the same pace as the overall language.


# Unit Tests
#There is a wide variety of approaches to testing software. One of the simplest kinds of test is a unit test. 
# A unit test verifies that one specific aspect of a function’s behavior is correct. 


# Test Cases
# A test case is a collection of unit tests that together prove that a function behaves as 
# it’s supposed to, within the full range of situations you expect it to handle. 
# A good test case considers all the possible kinds of input a function could receive 
# and includes tests to represent each of these situations. 
# A test case with full coverage includes a full range of unit tests 
# covering all the possible ways you can use a function.


# A Passing Test
# With pytest, writing your first unit test is pretty straightforward. 
# We’ll write a single test function. The test function will call the function 
# we’re testing, and we’ll make an assertion about the value that’s returned. 
# If our assertion is correct, the test will pass; if the assertion is incorrect, the test
# will fail.

# name_function.py

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

# names.py
from name_function import get_formatted_name
   
    print("Enter 'q' at any time to quit.")
    while True:
        first = input("\nPlease give me a first name: ")
        if first == 'q':
            break
        last = input("Please give me a last name: ")
        if last == 'q':
            break

        formatted_name = get_formatted_name(first, last)
        print(f"\tNeatly formatted name: {formatted_name}.")


test_name_function.py

from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis','joplin')
    assert formatted_name == 'Janis Joplin'


# The name of a test file is important; it must start with test_. When we ask pytest
# to run the tests we’ve written, it will look for any file that begins with test_,
# and run all of the tests it finds in that file.

# In the test file, we first import the function that we want to test: get
# _formatted_name(). Then we define a test function: in this case, test_first
# _last_name().


# test functions need to start with the word test,
# followed by an underscore. Any function that starts with test_ will be
# discovered by pytest, and will be run as part of the testing process.


# Also, test names should be longer and more descriptive than a typical
# function name. You’ll never call the function yourself; pytest will find the
# function and run it for you.

# Next, we call the function we’re testing. Here we call get_formatted
# _name() with the arguments 'janis' and 'joplin', just like we used when we
# ran names.py. We assign the return value of this function to formatted_name.

# Finally, we make an assertion 3. An assertion is a claim about a condition.
# Here we’re claiming that the value of formatted_name should be 'Janis
# Joplin'.


# Running a Test

# If you run the file test_name_function.py directly, you won’t get any output
# because we never called the test function. Instead, we’ll have pytest run the
# test file for us.


# To do this, open a terminal window and navigate to the folder that contains
# the test file. If you’re using VS Code, you can open the folder containing
# the test file and use the terminal that’s embedded in the editor window. In the
# terminal window, enter the command pytest.


============================================================ test session starts ============================================================
platform darwin -- Python 3.11.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/jbrown/python-fun
collected 1 item                                                                                                                            

project_work/Chapter_11/test_name_function.py .                                                                                       [100%]

============================================================= 1 passed in 0.01s =============================================================
jbrown@Jabaris-MacBook-Pro python-fun % 


# First of all, we see some information about the system the test is running on <--- Platform
# Next, we see the directory where the test is being run from
# We can see that pytest found one test to run and we can see the test file that’s being run


# A Failing Test

from name_function2 import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis','joplin')
    assert formatted_name == 'Janis Joplin'


================================================================= FAILURES ==================================================================
___________________________________________________________ test_first_last_name ____________________________________________________________

    def test_first_last_name():
        """Do names like 'Janis Joplin' work?"""
>       formatted_name = get_formatted_name('janis','joplin')
E       TypeError: get_formatted_name() missing 1 required positional argument: 'last'

project_work/Chapter_11/test_name_function copy.py:5: TypeError
========================================================== short test summary info ==========================================================
FAILED project_work/Chapter_11/test_name_function copy.py::test_first_last_name - TypeError: get_formatted_name() missing 1 required positional argument: 'last'
======================================================== 1 failed, 1 passed in 0.02s ========================================================


# The first item of note in the output is a single F , which tells us that one test failed.
# We then see a section that focuses on FAILURES, because failed tests are usually the most important thing to
# focus on in a test run. Next, we see that test_first_last_name() was the test
# function that failed. An angle bracket indicates the line of code that
# caused the test to fail. The E on the next line shows the actual error that
# caused the failure: a TypeError due to a missing required positional argument,
# last. The


# Responding to a Failed Test


# changing the function to work
def get_formatted_name(first,last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()



============================================================ test session starts ============================================================
platform darwin -- Python 3.11.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/jbrown/python-fun
collected 2 items                                                                                                                           

project_work/Chapter_11/test_name_function copy.py .                                                                                  [ 50%]
project_work/Chapter_11/test_name_function.py .                                                                                       [100%]

============================================================= 2 passed in 0.01s =============================================================


# Adding New Tests 

def test_first_last_name():
    """Do names like 'Wolfgang Amadeus Mozart' work? """
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'



============================================================ test session starts ============================================================
platform darwin -- Python 3.11.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/jbrown/python-fun
collected 2 items                                                                                                                           

project_work/Chapter_11/test_name_function copy.py .                                                                                  [ 50%]
project_work/Chapter_11/test_name_function.py .                                                                                       [100%]

============================================================= 2 passed in 0.01s =============================================================


# To test the function, we call get_formatted_name() with a first, last, and middle name, 
# and then we make an assertion that the returned full name matches 
# the full name (first, middle, and last) that we expect.

# The two dots indicate that two tests passed, which is also clear from
# the last line of output.



















