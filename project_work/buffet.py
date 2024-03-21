# TRY IT YOURSELF
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

food = ('baked chicken', 'pizza', 'meatloaf', 'steak', 'baked potato')
for buffet in food:
    print(buffet)

food = ('baked chicken', 'pizza', 'meatloaf', 'steak', 'baked potato')
food[0] = 'banana'
print(food)

food = ('baked chicken', 'pizza', 'meatloaf', 'steak', 'baked potato')
print("Original Menu:")
for buffet in food:
    print(buffet)

food = ('chicken parm', 'pizza', 'meatloaf', 'steak', 'corn')
print("\nModified Menu:")
for buffet in food:
    print(buffet.title())