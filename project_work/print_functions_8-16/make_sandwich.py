import create_sandwiches

create_sandwiches.sandwiches("turkey", 'american cheese', "tomato", "lettuce")


from create_sandwiches import sandwiches

sandwiches("beef", "chicken", "swiss", "onions")

from create_sandwiches import sandwiches as sn

sn("swiss cheese", "gouda", "pepper jack", "tomato")


import create_sandwiches as cs

cs.sandwiches("goat cheese", "lamb", "lettuce", "tomato", "onion")



from create_sandwiches import *

create_sandwiches.sandwiches("meetballs", "marinara", "mozzarella")