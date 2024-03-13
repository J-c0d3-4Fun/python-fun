#Modifying, Adding, and Removing Elements
#The syntax for modifying an element is similar to the syntax for accessing an element in a list. 
#To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)


# Adding Elements to a List

#Append
#The simplest way to add a new element to a list is to append the item to the list. 
#When you append an item to a list, the new element is added to the end of the list.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# The append() method makes it easy to build lists dynamically.
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Insert
# You can add a new element at any position in your list by using the insert() method. 
# You do this by specifying the index of the new element and the value of the new item.

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removing an Item
#If you know the position of the item you want to remove from a list, you can use the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

#Remove an Item Using the pop() Method
#Sometimes you’ll want to use the value of an item after you remove it from a list.
#The pop() method removes the last item in a list, but it lets you work with that item after removing it. 
#The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. 
#In this analogy, the top of a stack corresponds to the end of a list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The first motorcycle I owned was a {last_owned.title()}.")

#Popping Items from any position in a list
#You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#Remember that each time you use pop(), the item you work with is no longer stored in the list.
#If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method


#Removing an item by Value
#If you only know the value of the item you want to remove, you can use the remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#You can also use the remove() method to work with a value that’s being removed from a list.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")


#Organizing list
#Sorting a List Permanently with the sort() Method
# sort() method makes it relatively easy to sort a list.

cars = ['bmw', 'audi', 'toyoyta', 'subaru']
cars.sort()
print(cars)

#The sort() method changes the order of the list permanently. The cars are now in alphabetical order, and we can never revert to the original order

#You can also sort this list in reverse-alphabetical order by passing the argument reverse=True to the sort() method.
cars = ['bmw', 'audi', 'toyoyta', 'subaru']
cars.sort(reverse=True)
print(cars)

#Again, the order of the list is permanently changed


#Sorting a ListTemporarilywith the sorted() Function
#To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. 
#The sorted() function lets you display your list in a particular order, but doesn’t affect the actual order of the list.
cars = ['bmw', 'audi', 'toyoyta', 'subaru']
print('Here is the original list:')
print(cars)

print("\nHereis the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#The sorted() function can also accept a reverse=True argument if you want to display a list in reverse-alphabetical order

#Printing a List in Reverse Order 
#To reverse the original order of a list, you can use the reverse() method
cars = ['bmw', 'audi', 'toyoyta', 'subaru']
print(cars)

cars.reverse()
print(cars)

#Finding the Length of a list
cars = ['bmw', 'audi', 'toyoyta', 'subaru']
len(cars)

#You’ll find len() useful when you need to identify the number of aliens that still need to be shot down in a game, determine the amount of data you have to manage in a visualization, or figure out the number of registered users on a website, among other tasks.
