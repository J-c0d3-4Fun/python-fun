def fav_number(integer, response):
    """Allows the user to guess my favorite number"""
    active = True
    while active is True:
        if integer == 23:
            print(f"You guessed my favorite number! which is {integer}")
            break
        else:
            response = input("You're close! do you want to go again? (yes / no)")
            if response == 'yes':
                integer = int(input("Please guess again: "))
            else:
                active = False

print("Welcome to my guessing game!")
integer = int(input("What is my favorite number?"))
number = integer
response = integer
fav_number(integer, response)
