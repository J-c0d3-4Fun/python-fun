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


# # 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a day of
# business.
class Restaurant:
    """describing a restaurant"""

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaraunt is {self.restaurant_name}")
        print(f"\n The type of food the restaurant serves is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business!")
    
    def restaurant(self):
        print(f"The number of customers the restaurant {self.number_served} ")

    def set_number_served(self,number):
        self.number_served = number
    
    def increment_number_served(self,customers):
        self.number_served += customers


business = Restaurant("Pappadeaux", "Louisiana")
business.describe_restaurant()
business.open_restaurant()
business.restaurant()
business.set_number_served(3)
business.increment_number_served(20000)
business.restaurant()
business.increment_number_served(1300)
business.restaurant()


# 9-5. Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class Users:
    """Describing a user using a profile"""

    def __init__(self,first_name,last_name,age,height,hair_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.hair_color = hair_color
        self.user = f"{self.first_name} {self.last_name}"
        self.login_attempts = 0

    def describe_user(self):
        print(f"This is the current profile for the user {self.first_name} {self.last_name}")
        print(f"{self.first_name}'s current age is {self.age} and their height is {self.height}")
        print(f"Lastly {self.first_name}'s hair color is {self.hair_color}")

    def greet_user(self):
        print(f"Hello {self.user} welcome to the team!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"You've attempted {self.login_attempts} number of logins")

    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = Users("John","Doe", 55, "5'9'", "black" )
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()















# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.


class Restaurant:
    """describing a restaurant"""

    def __init__(self,restaurant_name, cuisine_type, flavors):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors

    def describe_restaurant(self):
        print(f"The name of the restaraunt is {self.restaurant_name}")
        print(f"\n The type of food the restaurant serves is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business!")


class IceCreamStand(Restaurant):
    """Initializes attributes from the parent class restaraunt. 
    Then allows you to choose your favorite Ice Cream flavor.
    """

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type, flavors)
        self.flavors = flavors

    def favorite(self):
        """describes the Ice cream flavor"""
        print("My favorite flavor of ice cream is:")
        for flavor in self.flavors:
            print(f"{flavor}")

icecream = IceCreamStand("ice day breeze", "cream", ["vanilla", "chocolate", "strawberry"])
icecream.favorite()




# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
# strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

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

class Admin(Users):

    def __init__(self, first_name, last_name, age, height, hair_color):
        super().__init__(first_name, last_name, age, height, hair_color)
        self.privileges = ["can add post", "can delete post"]

    def show_privileges(self):
        print(f"The admin {self.user} current privileges are listed below")
        for rights in self.privileges:
            print(f"- {rights}")

user_1 = Admin("John","Doe", 55, "5'9'", "black")
user_1.show_privileges()



# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.


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

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post"] 

    def show_privileges(self):
            print(f"The admin's current privileges are listed below")
            for rights in self.privileges :
                print(f"- {rights}")

class Admin(Users):

    def __init__(self, first_name, last_name, age, height, hair_color):
        super().__init__(first_name, last_name, age, height, hair_color)
        self.privileges = Privileges()


administrator = Admin("John","Doe", 55, "5'9'", "black")
administrator.describe_user()
administrator.privileges.show_privileges()




# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 65 if it isn’t already. Make
# an electric car with a default battery size, call get_range() once, and then
# call get_range() a second time after upgrading the battery. You should see an
# increase in the car’s range.


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
        """Set the odometer reading to the given value."""
    
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

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
    
    def upgrade_battery(self):
        """Upgrades the battery"""
        if self.battery_size != 65:
            self.battery_size = 65
 

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, battery_size):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024, battery_size=40)
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()


# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
# Make a separate file that imports Restaurant. Make a Restaurant instance,
# and call one of Restaurant’s methods to show that the import statement is working
# properly.

# Solution found in project work named Restaurant

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store
# the classes User, Privileges, and Admin in one module. Create a separate file,
# make an Admin instance, and call show_privileges() to show that everything is
# working correctly.

# Solution found in project work named Admin

# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.

# Solution found in project work named Privileges



# 9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. 
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import randint

class Die:
    """ a 6 sided die"""
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        roll = randint(1, self.sides)
        print(roll)

rolling = Die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()

rolling = Die(sides=10)
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()

rolling = Die(sides=20)
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()
rolling.roll_die()


# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
# Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.


from random import choice

lottery = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E']
fc = choice(lottery)
sc = choice(lottery)
tc = choice(lottery)
foc = choice(lottery)

message = print(f"Any ticket that matches these 4 numbers and letters win a prize! 
                \n:{fc}{sc}{tc}{foc}")

# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
# Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. 
# Print a message reporting how many times the loop had to run to give you a winning ticket.
from random import choice

lottery = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E']
fc = choice(lottery)
sc = choice(lottery)
tc = choice(lottery)
foc = choice(lottery)

winning_ticket = f"{fc}{sc}{tc}{foc}"

my_ticket = "A15D"

count = 0

while winning_ticket != my_ticket:
    print(count)
    count += 1
    fc = choice(lottery)
    sc = choice(lottery)
    tc = choice(lottery)
    foc = choice(lottery)
    winning_ticket = f"{fc}{sc}{tc}{foc}"

        
    
        


# 9-16. Python Module of the Week: One excellent resource for exploring the Python standard library is a site called Python Module of the Week. 
# Go to https://pymotw.com and look at the table of contents. 
# Find a module that looks interesting to you and read about it, perhaps starting with the random module
























