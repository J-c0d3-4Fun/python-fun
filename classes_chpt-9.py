# Creating and Using a Class
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a commad."""
        print(f"{self.name} rolled over!")



# By convention, capitalized names refer to classes
# in Python. There are no parentheses in the class definition because we’re
# creating this class from scratch. We then write a docstring describing what
# this class does.

# The __init__() Method
# The __init__() method 2 is a special method
# that Python runs automatically whenever we create a new instance based
# on the Dog class. This method has two leading underscores and two trailing
# underscores, a convention that helps prevent Python’s default method
# names from conflicting with your method names. Make sure to use two
# underscores on each side of __init__(). If you use just one on each side, the
# method won’t be called automatically when you use your class, which can
# result in errors that are difficult to identify.

# The self parameter is required in the method definition, and
# it must come first, before the other parameters. It must be included in
# the definition because when Python calls this method later (to create an
# instance of Dog), the method call will automatically pass the self argument.
# Every method call associated with an instance automatically passes self,
# which is a reference to the instance itself; it gives the individual instance
# access to the attributes and methods in the class. When we make an
# instance of Dog, Python will call the __init__() method from the Dog class.
# We’ll pass Dog() a name and an age as arguments; self is passed automatically,
# so we don’t need to pass it. Whenever we want to make an instance
# from the Dog class, we’ll provide values for only the last two parameters, name
# and age.

# The two variables defined in the body of the __init__() method each
# have the prefix self 3. Any variable prefixed with self is available to every
# method in the class, and we’ll also be able to access these variables through
# any instance created from the class. The line self.name = name takes the
# value associated with the parameter name and assigns it to the variable name,
# which is then attached to the instance being created. The same process
# happens with self.age = age. Variables that are accessible through instances
# like this are called attributes.

# The Dog class has two other methods defined: sit() and roll_over() 4.
# Because these methods don’t need additional information to run, we just
# define them to have one parameter, self. The instances we create later
# will have access to these methods. In other words, they’ll be able to sit and
# roll over. For now, sit() and roll_over() don’t do much. They simply print
# a message saying the dog is sitting or rolling over.


# Making an Instance from a Class 

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# The Dog class we’re using here is the one we just wrote in the previous example. Here, we tell Python to create a dog whose name is 'Willie' and whose age is 6 1. 
# When Python reads this line, it calls the __init__() method in Dog with the arguments 'Willie' and 6. 
# The __init__() method creates an instance representing this particular dog and sets the name and age attributes using the values we provided. 
# Python then returns an instance representing this dog. We assign that instance to the variable my_dog. The naming convention is helpful here;
#  we can usually assume that a capitalized name like Dog refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.


# Accessing Attributes

# To access the attributes of an instance, you use dot notation. We access the value of my_dog’s attribute name 2 by writing

my_dog.name


# Dot notation is used often in Python. 
# This syntax demonstrates how Python finds an attribute’s value. 
# Here, Python looks at the instance my_dog and then finds the attribute name associated with my_dog. 
# This is the same attribute referred to as self.name in the class Dog. 
# We use the same approach to work with the attribute age 3.
 

# Calling a Method
# After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.
#  Let’s make our dog sit and roll over

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

# To call a method, give the name of the instance (in this case, my_dog)
# and the method you want to call, separated by a dot. When Python reads
# my_dog.sit(), it looks for the method sit() in the class Dog and runs that
# code. Python interprets the line my_dog.roll_over() in the same way.

# Creating Multiple Instances
# You can create as many instances from a class as you need.

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Youe dog is {your_dog.age} years old.")
your_dog.sit()


# Even if we used the same name and age for the second dog, Python
# would still create a separate instance from the Dog class. You can make
# as many instances from one class as you need, as long as you give each
# instance a unique variable name or it occupies a unique spot in a list or
# dictionary.

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

# The new method increment_odometer() takes in a number of miles, and adds this value to self.odometer_reading. First, we create a used car, my_used_car 1.
# We set its odometer to 23,500 by calling update_odometer() and passing it 23_500 2. Finally, we call increment_odometer() and pass it 100 to add the
# 100 miles that we drove between buying the car and registering it


# NOTE You can use methods like this to control how users of your program update values such as an odometer reading, 
# but anyone with access to the program can set the odometer reading to any value by accessing the attribute directly. 
# Effective security takes extreme attention to detail in addition to basic checks like those shown here

# The __init__() Method for a Child Class
# When you’re writing a new class based on an existing class, you’ll often
# want to call the __init__() method from the parent class. This will initialize
# any attributes that were defined in the parent __init__() method and make
# them available in the child class.

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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

# We start with Car 1. When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.
# We then define the child class, ElectricCar 2.
# The name of the parent class must be included in parentheses in the definition of a child class. 
# The __init__() method takes in the information required to make a Car instance 3.
# The super() function 4 is a special function that allows you to call a method from the parent class. 
# This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method.
# We make an instance of the ElectricCar class and assign it to my_leaf 5. This line calls the __init__() method defined in ElectricCar, 
# which in turn tells Python to call the __init__() method defined in the parent class Car.

# Defining Attributes and Methods for the Child Class 
# Once you have a child class that inherits from a parent class, you can add
# any new attributes and methods necessary to differentiate the child class
# from the parent class.

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


# We add a new attribute self.battery_size and set its initial value to
# 40 1. This attribute will be associated with all instances created from the
# ElectricCar class but won’t be associated with any instances of Car. We also
# add a method called describe_battery() that prints information about the
# battery 2. When we call this method, we get a description that is clearly
# specific to an electric car


# Overriding Methods from Parent Class
# You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class. 
# To do this, you define a method in the child class with the same name as the method you want to override in the parent class. 
# Python will disregard the parent class method and only pay attention to the method you define in the child class.
# Say the class Car had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle, so you might want to override this method. 
# Here’s one way to do that:
class ElectricCar(Car):

def fill_gas_tank(self):
    """Electric cars don't have gas tanks!"""
    print("This car doesn't have a gas tank!")

# Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method 
# fill_gas_tank() in Car and run this code instead. When you use inheritance, 
# you can make your child classes retain what you need and override anything you don’t need from the parent class.


# Instaces as Attributes
# When modeling something from the real world in code, you may find that you’re adding more and more detail to a class. 
# You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy. 
# In these situations, you might recognize that part of one class can be written as a separate class. 
# You can break your large class into smaller classes that work together; this approach is called composition.
# For example, if we continue adding detail to the ElectricCar class, we might notice that
# we’re adding many attributes and methods specific to the car’s battery. 
# When we see this happening, we can stop and move those attributes and methods to a separate class called Battery. 
# Then we can use a Battery instance as an attribute in the ElectricCar class:

class Car:
--snip--
    
class Battery:
    """A simple attempt to model a battery for can electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}--kWh battery.")

class ElectricCar(Car):
    """Represnt aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', '2024')
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

# We define a new class called Battery that doesn’t inherit from any other
# class. The __init__() method 1 has one parameter, battery_size, in addition
# to self. This is an optional parameter that sets the battery’s size to 40 if no
# value is provided. The method describe_battery() has been moved to this
# class as well 2.
# In the ElectricCar class, we now add an attribute called self.battery 3.
# This line tells Python to create a new instance of Battery (with a default size
# of 40, because we’re not specifying a value) and assign that instance to the
# attribute self.battery. This will happen every time the __init__() method
# is called; any ElectricCar instance will now have a Battery instance created
# automatically.
# We create an electric car and assign it to the variable my_leaf. When
# we want to describe the battery, we need to work through the car’s battery
# attribute



# Importing Classes
# this is the car.py module

1 """A class that can be used to represent a car."""
class Car:
    """A simple attempt to represent a car."""
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
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

# We include a module-level docstring that briefly describes the contents of this module 1. 
# You should write a docstring for each module you create.


from car import Car

my_new_car = Car('audi','a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# The import statement 1 tells Python to open the car module and import
# the class Car. Now we can use the Car class as if it were defined in this file.


# Storing Multiple Classes in a Module
# You can store as many classes as you need in a single module, although
# each class in a module should be related somehow.
# this is the car.py module


"""A set of classes used to represent gas and electric cars."""
class Car:
    --snip--

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

# Now we can make a new file called my_electric_car.py, 
# import the ElectricCar class, and make an electric car:

from car import ElectricCar

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()


# Importing Multiple Classes from a Module




















