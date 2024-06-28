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









