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