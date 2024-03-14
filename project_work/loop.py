#Looping allows you to take the same action, or set of actions, with every item in a list


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#It might help to read this code as “For every magician in the list of magicians, print the magician’s name.”

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

#Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Because we have indented both calls to print(), each line will be executed once for every magician in the list. 
#The newline ("\n") in the second print() call inserts a blank line after each pass through the loop.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
























