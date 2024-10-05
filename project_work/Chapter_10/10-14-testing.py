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

def check_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        prompt = input(f"Please confirm if this is the correct username?(y/n):{username} ")
        if prompt.lower() == 'n':
            get_new_username(path)
        
        return username
    
    

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        username = check_stored_username(path)
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}! ")
    return username


greet_user()








