from birds.bird import Bird 
from birds.seabird  import Seabird
from birds.fowl import Fowl
 
my_bird = Bird("Owl", "Twit-Twoo!")

print(my_bird.get_description())

my_bird = Seabird("Gull", "Squaawwk!!", 2)

print(my_bird.get_description())

my_bird = Fowl("Chicken", "BockBock!", 'landfowl')

print(my_bird.get_description())


my_bird = Fowl("Duck", "Quaaakk!!", 'Waterfowl')

print(my_bird.get_description())


