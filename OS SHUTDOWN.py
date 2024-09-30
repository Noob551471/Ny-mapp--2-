import os
import time

passwerd = "comp"
user = "yunus"

username = input("user: ")
password = input("password: ")


if username.lower () != user or password != passwerd:
    
    print ("try again")
    print ("wrong password or username")
    
    time.sleep(1)
    
    print ("shutting down...")  
    
    time.sleep(1)
    
    os.system('shutdown /s /t 1')


else:
    print ("hello friend :)")

