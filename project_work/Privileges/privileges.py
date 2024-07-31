from user import Users

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