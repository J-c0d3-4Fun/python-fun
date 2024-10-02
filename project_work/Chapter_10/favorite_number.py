from pathlib import Path
import json

def favorite_number(path):
    """Asking for the favorite number"""
    prompt = input("What is your favorite number?")
    path = Path("numbers.json")
    contents = json.dumps(prompt)
    path.write_text(contents)
    return prompt

def read_number():
    """Reading numbers from a file"""
    path = Path("numbers.json")
    if path.exists():
        contents = path.read_text() 
        reading = json.loads(contents)
        print(f"I know your favorite number! It's {reading}")
    else:
        number = favorite_number(path)
        print(f"We now have stored your favorite number, {number}")

read_number()