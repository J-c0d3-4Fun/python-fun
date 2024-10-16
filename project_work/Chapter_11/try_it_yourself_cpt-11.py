# TRY IT YOURSELF
# 11-1. City, Country: Write a function that accepts two parameters: a city name
# and a country name. The function should return a single string of the form
# City, Country, such as Santiago, Chile. Store the function in a module called
# city_functions.py, and save this file in a new folder so pytest won’t try to run the
# tests we’ve already written.
# Create a file called test_cities.py that tests the function you just wrote.
# Write a function called test_city_country() to verify that calling your function
# with values such as 'santiago' and 'chile' results in the correct string. Run the
# test, and make sure test_city_country() passes.


# city country program
def city_country(city,country):
    place = f"{city},{country}"

    return place.title()



# testing program

from city_function import city_country

def test_city_country():
    """Does it print out the correct output of city,country"""
    citytest = city_country("paris", "france")
    assert citytest == 'Paris,France'



========================= test session starts ==========================
platform darwin -- Python 3.11.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/jbrown/python-fun
collected 1 items                                                      

project_work/Chapter_11/pytest/test_city_function.py .           [ 100%]

========================== 1 passed in 0.01s ===========================

# 11-2. Population: Modify your function so it requires a third parameter, population.
# It should now return a single string of the form City, Country – population xxx,
# such as Santiago, Chile – population 5000000. Run the test again, and make sure
# test_city_country() fails this time.
# Modify the function so the population parameter is optional. Run the test,
# and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that verifies
# you can call your function with the values 'santiago', 'chile', and 'population
# =5000000'. Run the tests one more time, and make sure this new test passes.

def city_country(city,country,population):
    if population:
        place = f"{city},{country} -- population: {population}"
    else:
        place = f"{city},{country}"

    return place.title()

============================= test session starts ==============================
platform darwin -- Python 3.11.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/jbrown/python-fun
collected 1 items                                                              

project_work/Chapter_11/pytest/test_city_function.py F                   [ 100%]                  

=================================== FAILURES ===================================
______________________________ test_city_country _______________________________

    def test_city_country():
        """Does it print out the correct output of city,country"""
>       citytest = city_country("paris", "france")
E       TypeError: city_country() missing 1 required positional argument: 'population'

project_work/Chapter_11/pytest/test_city_function.py:5: TypeError
=========================== short test summary info ============================
FAILED project_work/Chapter_11/pytest/test_city_function.py::test_city_country - TypeError: city_country() missing 1 required positional argument: 'population'
========================= 1 failed 0.02s ==========================




def city_country(city,country,population=""):
    if population:
        place = f"{city},{country} -- population: {population}"
    else:
        place = f"{city},{country}"

    return place.title()

============================= test session starts ==============================
platform darwin -- Python 3.11.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/jbrown/python-fun
collected 1 items                                                              

project_work/Chapter_11/pytest/test_city_function.py .                   [ 100%]


============================== 1 passed in 0.01s ===============================


# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5,000 to the
# annual salary by default but also accepts a different raise amount.
# Write a test file for Employee with two test functions, test_give_default
# _raise() and test_give_custom_raise(). Write your tests once without using a
# fixture, and make sure they both pass. Then write a fixture so you don’t have to
# create a new employee instance in each test function. Run the tests again, and
# make sure both tests still pass

class Employee:

    def __init__(self,first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self):
        prompt = input("Do you want to give a custom raise? 'y' or 'n': ")
        if prompt == 'y':
            self.salary = int(input("enter raise here: ")) + self.salary
        else:
            self.salary = self.salary + 5000
        print(f"the employees salary is now ${self.salary}")








