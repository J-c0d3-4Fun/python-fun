from random import randint

class guess:
    """ guessing game"""
    def __init__(self,response):
        self.response = response

    def random_number(self):
        prompt = "Guess the number!"
        prompt += "(Enter 'quit' when you are finished.)"

        random = randint(1,100)
        active = True
        while active is True:
            guess_number = input(int(prompt))
            if random == guess_number:
                print(f"You guessed the number correctly it is {random}!")
                break
            elif random != guess_number:
                print("do you want to try again?")
                if guess_number == 'quit':
                    break


### currently a work in progress