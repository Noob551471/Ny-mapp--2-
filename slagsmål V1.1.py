import random
from time import sleep
from os import system




Player1_name = input("Choose your name\n")
Player1_hp = 100
Player1_crit_chance = float(0.1)



class player_stats():
    def __init__(self, name, hp, crit_chance):
        
        self.name = name
        self.hp = hp
        self.crit_chance = crit_chance

Player1 = player_stats(Player1_name, Player1_hp, Player1_crit_chance)













