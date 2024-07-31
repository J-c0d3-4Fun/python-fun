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
