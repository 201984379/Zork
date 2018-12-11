from __future__ import print_function
import random



def restart():
    user = ""
    playerItems = []
    enteredRooms = []
    openedDoors = []
    money = 0
    
    
    user = raw_input("Would you like to restart the game? ")
    if user == "yes":
        map()
    else:
        print("You should really type yes")
        prompt = raw_input("type yes ")
        if prompt == "yes":
            map()
        else:
            print("Fine. Game over")
        
        
   
def benches():
    global playerItems
    global enteredRooms
    global openedDoors
    if "bench" in enteredRooms:
        print("You've already been here. Go back to map")
    else:
        enteredRooms.append("bench")        
        print("You have walked down towards the bench. ")
        print("You see a purse lying there unattended. ")
        print("You really need more money. What do you do?")
        print("Leave the purse alone? Or take the money you need")
        user = raw_input()
        if user == "leave the purse alone":
            print("Nice job! You made the right decision.")
            print(" A cop just passed by and waved at you.")
            print("Although you don't have the money, you have the knowledge you did the right thing")
        if user!= "leave the purse alone":
            if user != "take the money" or "take the money you need":
                print("I don't understand what you said")    
            else:
                print("You have been caught stealing by a cop. ")
                print("He puts you in handcuffs and takes you to jail.")
                restart()
           
            
        
    
    
     