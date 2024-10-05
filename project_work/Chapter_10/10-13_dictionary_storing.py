from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    # contents = json.dumps(username)
    # path.write_text(contents)
    return username 

def get_location():
    """ask user where they live"""
    prompt = input("What city and state do you live in? ")
    # contents = json.dumps(prompt)
    # path.write_text(contents)
    return prompt

def get_age():
    """ask for age""" 
    prompt = input("How old are you? ")
    # contents = json.dumps(prompt)
    # path.write_text(contents)
    return prompt


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}! ")
    return username


def dictionary(path): 
    """putting info into a dictionary"""
    path = Path("dictionary.json")
    info = {}
    info['username'] = greet_user()
    info['city and state'] = get_location()
    info['age'] = get_age()
    contents = json.dumps(info) 
    path.write_text(contents)
    return_dictionary(path)
    

def return_dictionary(path):
    """returns the info in the dictionary"""
    contents = path.read_text()
    dictionary = json.loads(contents)
    print(f"This is what we currently have stored as your info: {dictionary}")
    return dictionary

dictionary('dictionary.json')