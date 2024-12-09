#labyrin
from time import sleep
import random

chance_happening = (0.9)

#will run first
print ("Hello dear traveler. Welcome to the task place. Which maze would u wanna enter? Be ware they are all built different each time and it will be dangerous so choose wisely")

sleep (3)


Maze_selector = input ("\n 1.The dungeon (not done) \n 2. The dragons lair (not done yet)\n")

#whats going to happen in the beginning

def before_entrance(name):
    print (f"you have chosen{name}") 
    sleep (2)
    if random.random() < chance_happening:
        print (f"While you were traveling to {name} you encounter The Shopkeeper")
        sleep (4)
        print ("Hello dear traveler. I'm the shopkeeper. I will be in there while you are looking around. Since u met me before i will give u one of the following items.")
        sleep (5)
        free_item = input ("1.")
    else:
        print(f"You have arrived to {name}")

before_entrance(Maze_selector)


def entrance():
    print (f"you are in the entrance of {Maze_selector}")