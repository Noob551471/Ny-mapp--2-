import time 
import random





#Player hud
Player_amount = ""
Player_amount_decider = ["0", "1", "2"]


Player1 = "" 
Player2 = "" 
Player1HP = int(100)
Player2HP = int(100)

#player damages

damage1 = "" #player 1 damage
damage2 = "" #player 2 damage

#crit chances

Player1_crit = float(0.1) #base possibility for player1 to land a crit
Player2_crit = float(0.1) #base possibility for player2 to land a crit
Strong_steve = float(0.3) #base possibility for strong steve to land a crit


#bot names

names1 = ["geff", "Steve", "carl", "alex"] 
names2 = ["Ash", "mike", "blank", "boss", "Strong Steve", "Mike Thyson", "Loran"] 
#Strong steve boss- never misses and higher base chance for crits
#Mike Thyson boss- Ur just dead unless u get lucky

#how many players




#Player wins
Player1_wins = int(0)
Player2_wins = int(0)

retry = ""



Player_amount = input ("how many players? choose 0-2 \n")


while Player_amount not in Player_amount_decider:
    print ("please choose 0-2 players")
    Player_amount = input ("how many players? choose 0-2 \n")


#0 players




if Player_amount == "0":
    Player1 = random.choice(names1)
    Player2 = random.choice(names2)
    print ("Bot vs Bot selected")
    
    time.sleep (2)
    
    
        
    
    while Player1HP  > 0 and Player2HP > 0:
        
    
        #damage amount of player 1 and 2 every round
    
        damage1 = random.randint(0, 20)

        damage2 = random.randint(0, 20)
    
    
            #round counter
    
    
            #player 1 round
        if damage1 == 0:
            print (f"{Player1} misses")
    
            time.sleep(1)   
            
        else:
                
            if random.random() < Player1_crit:
                damage1 *=3 #triple the damage
                print (Player1,"lands a crit!")
                print (f"{Player1} attacks {Player2} for {damage1} damage!")
                Player2HP -= damage1
                time.sleep(1)
            else:
                print (f"{Player1} attacks {Player2} for {damage1} damage!")
                Player2HP -=damage1
        
            time.sleep(1)
    
                #player 2 round
        if damage2 == 0:
                print (f"{Player2} misses")
                time.sleep(1)
        else:
            if random.random() < Player2_crit:
                damage2 *=3 #triple the damage
                print (Player2,"lands a crit!")
                print (f"{Player2} attacks {Player1} for {damage2} damage!")  
                Player1HP -= damage2
                time.sleep(1)
        
            else:
                print (f"{Player2} attacks {Player1} for {damage2} damage!") 
                Player1HP -=damage2
                time.sleep(1)

        

    
        if Player1HP < 0:
            print (f"{Player1} had {Player1HP} and {Player2} had {Player2HP}")
            print (Player2, "wins")
            Player2_wins += 1
            print (f"{Player1} {Player1_wins} - {Player2} {Player2_wins}")
        
            retry = input ("Play again? Yes or No\n" ).lower()
        
            while retry not in ["yes", "no", "y", "n"]:
                print ("Please anser it Yes or no?")
                retry = input ("Play again? Yes or No\n").lower()
        
            else:
                Player1HP = 100
                Player2HP = 100
            
    
        elif Player2HP < 0:
            print (f"{Player1} had {Player1HP} and {Player2} had {Player2HP}")
            print (Player1, "wins")
            Player1_wins += 1
            print (f"{Player1} {Player1_wins} - {Player2} {Player2_wins}")
        
            retry = input ("Play again? Yes or No\n" ).lower()
    
            while retry not in ["yes", "no", "y", "n"]:
                print ("Please answer it Yes or no?")
                retry = input ("Play again? Yes or No\n").lower()
        
            else:
                Player1HP = 100
                Player2HP = 100
    
        elif Player2HP and Player1HP <0:
            print ("tie")
            print (f"{Player1} {Player1_wins} - {Player2} {Player2_wins}")
        
        
        
            retry = input ("Play again? Yes or No\n" ).lower()
    
            while retry not in ["yes", "no", "y", "n"]:
                print ("Please answer it Yes or no?")
                retry = input ("Play again? Yes or No\n").lower()
        
            else:
                if retry == "yes":
                    Player1HP = int(100)
                    Player2HP = int(100)
                elif retry == "y":
                    Player1HP = int(100)
                    Player2HP = int(100)
                else:
                    Player_amount = ""
                    Player1HP = int(100)
                    Player2HP = int(100)
                    Player1_wins = int(0)
                    Player2_wins = int(0)
                    Player_amount = input ("how many players? choose 0-2 \n")



