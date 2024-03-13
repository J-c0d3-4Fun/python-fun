#Try it yourself
# 3-8. Seeing the World: Think of at least five places in the world you’d like
# to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly;
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing
# the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

location = ['mexico','africa','germany','paris','brazil']
print(location)
print(sorted(location))
print(location)
sorted(location,reverse=True)
print(location)
print(location)
location.reverse()
print(location)
location.reverse()
print(location)
location.sort()
print(location)
location.sort(reverse=True)
print(location)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (pages 41–42), use len() to print a message indicating the number
# of people you’re inviting to dinner.

guest = ['lebron', 'kobe', 'shaq']
print(f"I'm inviting {len(guest)} to the dinner party")




# 3-10. Every Function: Think of things you could store in a list. For example, you
# could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items and
# then uses each function introduced in this chapter at least once.

languages = ['french', 'spanish', 'english', 'polish']
print(f"I'm learning {languages[0].title} as my secondary langaunge")
print(f"I'm learning {languages[1].title} as my secondary langaunge")
print(f"I'm learning {languages[2].title} as my secondary langaunge")
print(sorted(languages))
print(languages)
sorted(languages, reverse=True)
print(languages)
print(f'this list contains {len(languages)} languanges')
languages.reverse()
print(languages)
languages.sort(reverse=True)
print(languages)
languages.sort()
print(languages)
del languages[-1]
languages.append('mandarin')
print(f"I've learned a new language called {languages[1]}")
languages.pop(0)
print(languages)
languages.insert(0, 'chinese')
print(languages)
languages.remove('chinese')
print(languages)
