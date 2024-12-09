import pygame
pygame.init

from time import sleep




#documentation about what veriables used

user =""  #the persons name
answer1 = "" #about joke question
answer_gender = "" #what gender are you

#family members
family_options = ""
family_yes = "yes"
mom = ""
dad = ""
sister = ""
brother = ""
geff = ""

#information about you

user= input ("Tell me your name \n ")
print ("Hello " +user)
sleep (1)
print ("Welcome to my game")
sleep (1)
answer1= input ("Before we start i want to know a little about you. Do you like blood? \n answer with yes or no \n").lower()

while answer1 not in ["yes", "no", "n", "y"]:
    print("please answer it \n yes or no")
    answer1= input ("Before we start i want to know a little about you. Do you like blood? \n answer with yes or no ").lower()

 
if answer1 == "yes" :
    print ("Well there wont be any😀")
elif answer1 == "y" :
    print ("Well there wont be any😀")

else:
    print ("Thats good to know. Dont worry there wont be any")

sleep (1)

answer_gender = input ("what gender are you? \n male or female\n").lower()
while answer_gender not in ["male", "m", "female", "f"]:
    print("please answer it with male or female")
    answer_gender = input ("what gender are you? \n male or female\n").lower()

if answer_gender == "m":
    print ("so you are male")
elif answer_gender == "male":
    print ("so you are male")


else:
    print ("so you are female")



sleep (1)

print ("Anyways back to the game information")

sleep (1)

#small game information
print ("This game will include the following things= \n \n multiple choices that will affect the ending (yes first question aswell) \n \n weird random questions about u that wont do anything about the game so dont worry \n \n ur private information(no not really) \n \n and at last you and me (the game)")


sleep(4)

#game start

print ("Here we go")

sleep (1)

#a little story

print ("you are in the car with your family")

sleep (1)

print ("First choice who do u want in ur family?")

sleep(1)

#choose family members

family_options = ["yes", "no"]

answer_mom = input ("do you want mom? \n yes or no \n").lower()

#decides if its allowed or not

while answer_mom not in family_options: 
    print("please answer it with yes or no")
    answer_mom = input ("do you want mom? \n yes or no \n").lower()
    

if answer_mom == "yes":
    mom = ["mom"]

else: 
    mom = ["no"]

answer_dad = input ("do you want dad? \n yes or no \n").lower()

#decides if its allowed or not

while answer_dad not in family_options: 
    print("please answer it with yes or no")
    answer_dad = input ("do you want dad? \n yes or no \n").lower()

if answer_dad == "yes":
    dad = ["dad"]
else: 
    dad = ["no"]
    

#brother
answer_brother = input ("do you want brother? \n yes or no \n").lower()
#decides if its allowed or not

while answer_brother not in family_options: 
    print("please answer it with yes or no")
    answer_brother = input ("do you want dad? \n yes or no \n").lower()

if answer_brother == "yes":
    brother = ["dad"]
else: 
    brother = ["no"]

#sister
answer_sister = input ("do you want sister? \n yes or no \n").lower()

#decides if its allowed or not

while answer_sister not in family_options: 
    print("please answer it with yes or no")
    answer_sister = input ("do you want dad? \n yes or no \n").lower()

if answer_sister == "yes":
    sister = ["dad"]
else: 
    sister = ["no"]

#geff
answer_geff= input ("do you want geff? \n yes or no \n").lower()

#decides if its allowed or not


while answer_geff not in family_options: 
    print("please answer it with yes or no")
    answer_geff = input ("do you want dad? \n yes or no \n").lower()

if answer_geff == "yes":
    geff = ["dad"]
else: 
    geff = ["no"]

#show 

