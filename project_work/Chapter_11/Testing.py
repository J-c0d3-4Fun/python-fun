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


#Testing a Class

# A Variety of Assertions

Assertion                                   Claim
assert a == b                   Assert that two values are equal.
assert a != b                   Assert that two values are not equal.
assert a                        Assert that a evaluates to True.
assert not a                    Assert that a evaluates to False.
assert element in list          Assert that an element is in a list.
assert element not in list      Assert that an element is not in a list.



# A Class to Test  

class AnonymousSurvey:
    """Collect anonymous ansers toa survey question."""

    def __init__(self, question):
        """store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")



# This class starts with a survey question that you provide 
# and includes an empty list to store responses. 
# The class has methods to print the survey question, 
# add a new response to the response list, 
# and print all the responses stored in the list.




class AnonymousSurvey:
    """Collect anonymous ansers toa survey question."""

    def __init__(self, question):
        """store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

# This program defines a question ("What language did you first learn to
# speak?") and creates an AnonymousSurvey object with that question. The program
# calls show_question() to display the question and then prompts for responses.
# Each response is stored as it is received. When all responses have been entered
# (the user inputs q to quit), show_results() prints the survey result




from survey import AnonymousSurvey

# Define a question, and make a survey 

question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question 

language_survey.show_question()
print("Enter 'q' at any time to quit. \n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)


# Show the survey results.

print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()

# Testing the AnonymousSurvey Class 

from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

# We start by importing the class we want to test, AnonymousSurvey. The first test function will verify 
# that when we store a response to the survey question, 
# the response will end up in the survey’s list of responses. A good descriptive name for this 
# function is test_store_single_response(). If this test fails, we’ll know from the function 
# name in the test summary that there was a problem storing a single response to the survey.
# To test the behavior of a class, we need to make an instance of the class. 
# We create an instance called language_survey with the question
# "What language did you first learn to speak?" We store a single response, English, using the store_response() method. 
# Then we verify that the response was stored correctly by asserting 
# that English is in the list language_survey.responses.
# By default, running the command pytest with no arguments will run all the tests that pytest discovers 
# in the current directory. To focus on the tests in one file, pass the name of the test file you want to run


================================================================= test session starts ==================================================================
platform darwin -- Python 3.11.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/jbrown/python-fun
collected 1 item                                                                                                                                       

project_work/Chapter_11/test_survey.py .                                                                                                         [100%]

================================================================== 1 passed in 0.00s ===================================================================

# Let’s verify that three responses can be stored correctly. 
# To do this, we add another method to TestAnonymousSurvey

def test_store_three_response():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    assert response in language_survey.responses

# We call the new function test_store_three_responses(). We create a survey
# object just like we did in test_store_single_response(). We define a list
# containing three different responses, and then we call store_response()
# for each of these responses. Once the responses have been stored, we
# write another loop and assert that each response is now in language_survey.responses.
# When we run the test file again, both tests (for a single response and
# for three responses) pass


================================================================== 1 passed in 0.00s ===================================================================
jbrown@Jabaris-MacBook-Pro python-fun % pytest project_work/Chapter_11/test_survey.py
================================================================= test session starts ==================================================================
platform darwin -- Python 3.11.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/jbrown/python-fun
collected 2 items                                                                                                                                      

project_work/Chapter_11/test_survey.py ..                                                                                                        [100%]

================================================================== 2 passed in 0.01s ===================================================================



# Using Fixtures



# In test_survey.py, we created a new instance of AnonymousSurvey in each test
# function. This is fine in the short example we’re working with, but in a realworld
# project with tens or hundreds of tests, this would be problematic.
# In testing, a fixture helps set up a test environment. Often, this means
# creating a resource that’s used by more than one test. 


# We create a fixture in
# pytest by writing a function with the decorator @pytest.fixture. A decorator is
# a directive placed just before a function definition; Python applies this directive
# to the function before it runs, to alter how the function code behaves.



@pytest.fixture
def langauge_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    langauge_survey = AnonymousSurvey(question)
    return langauge_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_response(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses




# We need to import pytest now, because we’re using a decorator that’s defined in pytest. 
# We apply the @pytest.fixture decorator 1 to the new function language_survey() 2. 
# This function builds an AnonymousSurvey object and returns the new survey.
# Notice that the definitions of both test functions have changed 3 5; each 
# test function now has a parameter called language_survey. When
# a parameter in a test function matches the name of a function with the
# @pytest.fixture decorator, the fixture will be run automatically and
# the return value will be passed to the test function. In this example, 
# the function language_survey() supplies both test_store_single_response() and 
# test_store_three_responses() with a language_survey instance.
# There’s no new code in either of the test functions, but notice that two lines 
# have been removed from each function 4 6: the line tthe line that defined a question and the 
# line that created an AnonymousSurvey object





# When you want to write a fixture, write a function that generates the resource 
# that’s used by multiple test functions. Add the @pytest.fixture
# decorator to the new function, and add the name of this function as a
# parameter for each test function that uses this resource. Your tests will be
# shorter and easier to write and maintain from that point forward.