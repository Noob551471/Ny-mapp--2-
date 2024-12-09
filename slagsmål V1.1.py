import random
from time import sleep
from os import system


Player_amount =input("select 0-2 players")

allowed_amount= ["0", "1", "2"]

while Player_amount not in allowed_amount:
    Player_amount =input("select 0-2 players")

#Player stats
while Player_amount == "1":
    Player1_name = input("Choose your name\n")

while Player_amount == "2":
        Player1_name = input("Choose your name Player1\n")
        Player2_name = input("Choose your name Player2\n")

hp = 100
crit_chance = float(0.1)

#naming bots



names1 = ["geff", "Steve", "carl", "alex"] 
names2 = ["Ash", "mike", "blank", "boss", "Strong Steve", "Mike Thyson", "Loran"] 

Player2_name = random.choice (names2)

class player_stats():
    def __init__(self, name, hp, crit_chance):
        
        self.name = name
        self.hp = hp
        self.crit_chance = crit_chance

Player1 = player_stats(Player1_name, hp, crit_chance)
Player2 = player_stats(Player2_name, hp, crit_chance)


if names2 == ("Mike thyson"):
    names2 == player_stats("Mike thyson", 200, 0.4)
    print("Warning \n you are going to fight Mike Thyson u are gonna die")
    sleep(4)

else:
    player_stats(names2, 100, 0.1)





#How much damage

damage1=random.randint(0,10)
damage2=random.randint(0,10)
Mikedamage=random.randint(0.30)


#class about who damage who

def hitPlayer(crit, hitter, victim, damage, crit_chance):
    if random.random(crit_chance) < crit:
        damage *=3 #triple the damage
        print (hitter,"lands a crit!")
        print (f"{hitter} attacks {victim} for {damage} damage!")
    

    else:
        print (f"{hitter} attacks {victim} for {damage} damage!") 

        sleep(1)
        return damage



def missplayer(hitter, victim,):
    print (hitter,"Misses", victim)



