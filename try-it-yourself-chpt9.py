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