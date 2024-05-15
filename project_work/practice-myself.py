# Favorite foods
responses = { }

active = True

while active: 
    # ask users name and which food they like
    firstName = input("What is your first name?")
    lastName = input("What is your last name?")
    name = f"{firstName.title()} {lastName.title()}"
    response = input("What is your favorite food?")

    # adds the name of the user and the response they provided as a key-value pair
    # name = key
    # response = value
    responses[name] = response

    # ask the user if they want to add more food
    repeat = input("Do you want to add another favorite food? (yes or no)")
    if repeat == 'yes':
        active = True
    else:
        active = False

print("Below are the results")
for name, response in responses.items():
    print(f"{name.title()} favorite food is {response}")
