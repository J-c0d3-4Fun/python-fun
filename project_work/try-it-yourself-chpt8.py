# TRY IT YOURSELF
# 8-1. Message: Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.

def display_message():
    """one simple sentence about chapter 8"""
    print("I am learning about functions in chapter 8.")

display_message()




# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(name):
    """Describes the users favorite book"""
    print(f"My favorite book is {name.title()}")

favorite_book('the personal mba')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
# Functions 137
def make_shirt(size, text):
    """describes the size and text that goes on the shirt"""
    print(f"I wear a size {size.upper()} ")
    print(f"My shirt will have the text: {text}")

make_shirt("xl","The most important time in your life is when you're born and when you find out why.")
make_shirt(size='l',text="The most important time in your life is when you're born and when you find out why.")

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size='l', text='I love Python'):
    """by default the shirt is large and has default text"""
    print(f"I wear a size {size.upper()} ")
    print(f"My shirt will have the text: {text}")

make_shirt()
make_shirt(size='m')
make_shirt(size='xl',text="The most important time in your life is when you're born and when you find out why.")
# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

def describe_city(city, country='united states'):
    """describes the users city and country"""
    print(f"{city.title()} is in {country.title()}")

describe_city(city='dhaka', country='bangladesh')
describe_city(city='salvador', country='brazil')
describe_city(city='rome', country='italy')


# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values
# that are returned.

def city_country(city, country):
    """Describes the city and country"""
    cityandcountry = f"{city}, {country}"
    return cityandcountry.title()

describe = city_country('dhaka', 'bangladesh')
print(describe)

describe = city_country('slavador', 'brazil')
print(describe)

describe = city_country('rome', 'italy')
print(describe)


# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
def make_album(artist, title, no_songs=None):
    """list artist, album and number of song son the album"""
    if no_songs:
        album = {'artist name': artist, 'album title': title, 'number of songs': no_songs}
    else:
        album = {'artist name': artist, 'album title': title}
    return album

first_album = make_album('tupac', 'all eyes on me')
print(first_album)

second_album = make_album('future', 'dirty sprite 2')
print(second_album)

third_album = make_album('prince', 'purple rain', 9)
print(third_album)
# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
def make_album(artist, title, no_songs=None):
    """list artist, album and number of song son the album"""
    if no_songs:
        album = {'artist name': artist, 'album title': title, 'number of songs': no_songs}
    else:
        album = {'artist name': artist, 'album title': title}
    return album

while True:
    artist = input('Who is your favorite artist?: ')
    if artist == 'q':
        break
    title = input("What is your favorite album by them?: ")
    if title == 'q':
        break
    no_songs = input("What is your favorite song from the album?: ")
    if no_songs == 'q':
        break

    fave_artist_album = make_album(artist, title, no_songs)
    print(fave_artist_album)






# 8-9. Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.


def show_messages(messages):
    """Prints the message from the list"""
    for message in messages:
        print(message)

unread_messages = ['Hey how are you?', 'My flight is at 6:30pm can you still pick me up?', 'will be at your house in 5 minutes']
show_messages(unread_messages)


# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.


# 8-11. Archived Messages: Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages