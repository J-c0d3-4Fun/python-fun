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












