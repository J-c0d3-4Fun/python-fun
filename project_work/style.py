# TRY IT YOURSELF
# 4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/
# dev/peps/pep-0008. You won’t use much of it now, but it might be interesting
# to skim through it.




# 4-15. Code Review: Choose three of the programs you’ve written in this chapter
# and modify each one to comply with PEP 8.
# • Use four spaces for each indentation level. Set your text editor to insert four
# spaces every time you press the TAB key, if you haven’t already done so
# (see Appendix B for instructions on how to do this).
# • Use less than 80 characters on each line, and set your editor to show a
# vertical guideline at the 80th character position.
# • Don’t use blank lines excessively in your program files.

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