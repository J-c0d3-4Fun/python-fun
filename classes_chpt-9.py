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


























