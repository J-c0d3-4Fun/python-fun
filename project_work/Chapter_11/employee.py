class Employee:

    def __init__(self,first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self):
        name = f"{self.first_name} {self.last_name}"
        prompt = input(f"Do you want to give a {name} custom raise? 'y' or 'n': ")
        if prompt == 'y':
            self.salary = int(input("enter raise here: ")) + self.salary
        else:
            self.salary = self.salary + 5000
        print(f"{name} salary is now ${self.salary}")

