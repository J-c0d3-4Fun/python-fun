# TRY IT YOURSELF


# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() 
# that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    """describing a restaurant"""

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaraunt is {self.restaurant_name}")
        print(f"\n The type of food the restaurant serves is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business!")


business = Restaurant("Pappadeaux", "Louisiana")
business.describe_restaurant()
business.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

class Restaurant:
    """describing a restaurant"""

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaraunt is {self.restaurant_name}")
        print(f"\n The type of food the restaurant serves is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business!")

Restaurant_1 = Restaurant("Ruth Chris","Steak House")
Restaurant_1.describe_restaurant()

Restaurant_2 = Restaurant("The Varsity","American")
Restaurant_2.describe_restaurant()

Restaurant_3 = Restaurant("Taco Mac","American")
Restaurant_3.describe_restaurant()


# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class Users:
    """Describing a user using a profile"""

    def __init__(self,first_name,last_name,age,height,hair_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.hair_color = hair_color
        self.user = f"{self.first_name} {self.last_name}"

    def describe_user(self):
        print(f"This is the current profile for the user {self.first_name} {self.last_name}")
        print(f"{self.first_name}'s current age is {self.age} and their height is {self.height}")
        print(f"Lastly {self.first_name}'s hair color is {self.hair_color}")

    def greet_user(self):
        print(f"Hello {self.user} welcome to the team!")

user_1 = Users("John","Doe", 55, "5'9'", "black" )
user_1.describe_user()
user_1.greet_user()

user_2 = Users("Amy","Turner", 43, "5'4'", "red" )
user_2.describe_user()
user_2.greet_user()

user_3 = Users("Timmy", "Turner", 15, "5'6'","brown")
user_3.describe_user()
user_3.greet_user()

user_4 = Users("Jimmy", "Nuetron", 14, "5'6", "brown")
user_4.describe_user()
user_4.greet_user()


# Working with Classes and Instances


# The Car Class 

class Car:
    """A simple attempt to respresent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())


# In the Car class, we define the __init__() method with the self parameter
# first 1, just like we did with the Dog class. We also give it three other parameters:
# make, model, and year. The __init__() method takes in these parameters
# and assigns them to the attributes that will be associated with instances
# made from this class. When we make a new Car instance, we’ll need to specify
# a make, model, and year for our instance.
# We define a method called get_descriptive_name() 2 that puts a car’s
# year, make, and model into one string neatly describing the car. This will spare
# us from having to print each attribute’s value individually. To work with the
# attribute values in this method, we use self.make, self.model, and self.year.
# Outside of the class, we make an instance from the Car class and assign it to
# the variable my_new_car 3. Then we call get_descriptive_name() to show what
# kind of car we have


# Setting a Default Value for an Attribute
# When an instance is created, attributes can be defined without being
# passed in as parameters.

class Car:
    """A simple attempt to respresent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Printing a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# Modifying Attribute Values
# You can change an attribute’s value in three ways: you can change the value directly through an instance, 
# set the value through a method, 
# or increment the value (add a certain amount to it) through a method. 
# Let’s look at each of these approaches.

# Modifying an Attribute's Value Directly
# The simplest way to modify the value of an attribute is to access the attribute directly through an instance

class Car:
    """A simple attempt to respresent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Printing a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# We use dot notation to access the car’s odometer_reading attribute, and set its value directly. 
# This line tells Python to take the instance my_new_car, 
# find the attribute odometer_reading associated with it, and set the value of that attribute to 23.

# Modifying an Attribute's Value Through a Method
# It can be helpful to have methods that update certain attributes for you. 
# Instead of accessing the attribute directly, you pass 
# the new value to a method that handles the updating internally.




    def update_odometer(self, mileage):
        """Printing a statement showing the car's mileage"""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()


# The only modification to Car is the addition of update_odometer(). This
# method takes in a mileage value and assigns it to self.odometer_reading.
# Using the my_new_car instance, we call update_odometer() with 23 as an argument
# 1. This sets the odometer reading to 23, and read_odometer() prints
# the reading



# We can extend the method update_odometer() to do additional work every
# time the odometer reading is modified. Let’s add a little logic to make sure
# no one tries to roll back the odometer reading



    def update_odemeter(self, milage):
    """
    Set the odometer reading to the given value.
    Reject the change if it attempts to roll the odometer back.
    """

    if mileage >= self.odemeter_reading:
        self.odemeter_reading = mileage
    else:
        print ("You can't roll back an odemeter")

# Now update_odometer() checks that the new reading makes sense before
# modifying the attribute. If the value provided for mileage is greater than
# or equal to the existing mileage, self.odometer_reading, you can update
# the odometer reading to the new mileage 1. If the new mileage is less
# than the existing mileage, you’ll get a warning that you can’t roll back an
# odometer 2.

# Incrementing on Attribute's Value Through a Method
# Sometimes you’ll want to increment an attribute’s value by a certain amount,
# rather than set an entirely new value.

    def update_odemeter(self,mileage):
    
    def increment_odemeter(self, miles):
    """ Add the given amount to the odemeter reading."""
    self.odemeter_reading += miles

my_used_car = Car('subura', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odemeter(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()








