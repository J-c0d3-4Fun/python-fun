#try it yourself

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

guest = ['lebron', 'kobe', 'michael']
message = "I'm inviting you to my dinner party"
print(f"Hello {guest[0].title()} {message}")
print(f"Hello {guest[1].title()} {message}")
print(f"Hello {guest[2].title()} {message}")


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in
# your list.

guest = ['lebron', 'kobe', 'michael']
print(f"I just heard that {guest[2].title()} can't make it! I'll have to invite someone else")
del guest[2]
guest.append('shaq')
print(f"Hello {guest[0].title()} {message}")
print(f"Hello {guest[1].title()} {message}")
print(f"Hello {guest[2].title()} {message}")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
#Print a new set of invitation messages, one for each person in your list.

guest = ['lebron', 'kobe', 'shaq']
print(f"Hey {guest[0].title()}, {guest[1].title()}, {guest[2].title()} I found a bigger table so I'm going to invite more people to our dinner part")
guest.insert(0,'hakeem')
guest.insert(2,'penny')
guest.append('steph')
message = "I'm inviting you to my dinner party"
print(f"Hello {guest[0].title()} {message}")
print(f"Hello {guest[1].title()} {message}")
print(f"Hello {guest[2].title()} {message}")
print(f"Hello {guest[3].title()} {message}")
print(f"Hello {guest[4].title()} {message}")
print(f"Hello {guest[5].title()} {message}")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you’re sorry you can’t invite them
# to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.

guest = ['lebron', 'kobe', 'shaq']
print(f"Hey {guest[0].title()}, {guest[1].title()}, {guest[2].title()} I found a bigger table so I'm going to invite more people to our dinner part")
guest.insert(0,'hakeem')
guest.insert(2,'penny')
guest.append('steph')
message = "I just found out the table won't make it in time and only have room for 2."
print(f"Hello {guest[0].title()}, {guest[1].title()}, {guest[2].title()}, {guest[3].title()}, {guest[4].title()}, and {guest[5].title()} {message}")
sorry = "sorry I can't invite you to my dinner party"
first_guest = guest.pop(4)
print(f"{first_guest.title()} {sorry}")
second_guest = guest.pop(2)
print(f"{second_guest.title()} {sorry}")
third_guest = guest.pop(3)
print(f"{third_guest.title()} {sorry}")
fourth_guest = guest.pop(0)
print(f"{fourth_guest.title()} {sorry}")
print(f"\nHey {guest[0].title()} & {guest[1].title()} you made the cut, welcome to the dinner party!")
del guest[0]
del guest[0]
print(guest)