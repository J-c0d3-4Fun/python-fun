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

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username 

def get_location(path):
    """ask user where they live"""
    prompt = input("What city and state do you live in? ")
    contents = json.dumps(prompt)
    path.write_text(contents)
    return prompt

def get_age(path):
    """ask for age""" 
    prompt = input("How old are you? ")
    contents = json.dumps(prompt)
    path.write_text(contents)
    return prompt


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    info = {}
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}! ")
    
    """putting info into a dictionary"""
    info['username'] = username
    info['city and state'] = get_location(path)
    info['age'] = get_age(path)
    print(f"{info}")
    
greet_user()