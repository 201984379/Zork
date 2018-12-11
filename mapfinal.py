from __future__ import print_function
import random
from myfootballField import footballField
times_entered_map = 0
enteredRooms = []
def readMap():
    print("At the park there is a football field, a girl who is wearing all purple, a flower shop, a bench, and a playground")
    print("Navigate by saying where you want to go without using capital letters. Good luck!")
def center():
    global times_entered_map
    global playerItems
    global enteredRooms
    global openedDoors
    if times_entered_map == 0:
        print("Welome to the park.You are at the map in the middle of the park.")
        print("You came to the park looking for money to pay for your date.")
        print("You also need a girlfriend to go on the date")
        print("All roads in the park lead through the map. You can see the places by saying 'read map'")
        print("Good luck")
        times_entered_map += 1
    while times_entered_map == 1:
        user = raw_input("Where would you like to go? ")
        if (user == "map") or (user == "go to map"):
            print("You are already at the map")
        elif user == "read map":
            readMap()
        elif (user == "football field") or (user == "go to football field"):
            footballField()
        elif (user == "playground") or (user == "go to playground"):
            playground()
        elif (user == "flower shop") or (user == "go to flower shop"):
            flowers()
        elif (user == "girl") or (user == "go to girl"):
            girl()
        elif (user == "bench") or (user == "go to bench") or (user == "go to the bench")
        else:
            print("I don't understand that")
            user = raw_input("Try again: ")
        
        
    