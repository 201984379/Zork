from __future__ import print_function
import random

playerItems = []
enteredRooms = []
openedDoors = []
money = 0
def center():
    print('you return to the map') #Remove this on compilation
def playground():
    global position
    global playerItems
    global enteredRooms
    global openedDoors
    global money
    exitRoom = False
    position = 3
    chestItems = ['shovel']
    print('You have entered the playground, and are standing at the playground bench!')
    print('There are many things to do on the playgorund!  There is a ladder to a slide, a sandbox, a swingset, and a toy chest!')
    userAction = raw_input('Have fun on the playground! ')
    while exitRoom == False:
        if (userAction == 'go to swingset') or (userAction =='walk to swingset') or (userAction == 'run to swingset') or (userAction == 'go to the swingset') or (userAction == 'walk to the swingset'):#This section of code lets the user head to the swingset
            print('You see that all of the swings are occupied. You walk back to the playground bench. ')
        elif (userAction == 'go to slide') or (userAction == 'walk to slide') or (userAction == 'run to slide'):#This section of code lets the  user head to the slide and go down it
            slideAction = raw_input('You are at the bottom of the ladder. ')
            if (slideAction == 'climb ladder') or (slideAction == 'go up ladder'):
                print('You climbed the ladder and went down the slide! Congratulations! You walk back to the playground bench. ')
            elif (slideAction == 'return to bench') or (slideAction == 'go to bench') or (slideAction == 'walk to bench'):
                print('You are standing at the bench. ')
            userAction = raw_input('What would you like to do now? ')
        elif (userAction == 'go to toy chest') or (userAction == 'walk to toy chest') or (userAction == 'go to toychest'):#This section of code lets the user go to  the toy chest where they can find a shovel
            print('There is a shovel in the toy chest.')
            userAction = raw_input('What would you like to do now? ')
            if (userAction == 'pick up shovel') or (userAction == 'grab shovel') or (userAction == 'take shovel'):
                playerItems += chestItems
                print('You have picked up the shovel. You walk back to the playground bench.')
            elif (userAction == 'return to bench') or (userAction == 'walk to bench') or (userAction == 'go to bench'):
                print('You are standing at the bench. ')
        elif (userAction == 'go to sandbox') or (userAction == 'walk to sandbox') or (userAction == 'walk to the sandbox') or (userAction == 'go to the sanbox'):#This section of code lets the user head to the sandbox where $10 is buried
            print('You are standing in the sandbox, there are no kids around.')
            userAction = raw_input('What would you like to do now? ')
            if (userAction == 'dig') or (userAction == 'dig in sandbox') or (userAction == 'pick up sand') or (userAction == 'play in sand') or (userAction == 'play in sandbox') and 'shovel' not in playerItems:
                print('You do not have anything to dig with. You walk back to the playground bench.')
            if (userAction == 'dig') or (userAction == 'dig in sandbox') or (userAction == 'pick up sand') or (userAction == 'play in sand') or (userAction == 'play in sandbox') and 'shovel' in playerItems:
                print('You have dug up 10 dollars using the shovel! You return to the park bench with your prize!')
                money += 10
                exitRoom == True
        elif (userAction == 'return to map') or (userAction == 'go to map') or (userAction =='go back to map') or (userAction == 'walk to map'):#This section of code lets the user return to the map in the center of the park
            position = 4
        else:
            userAction = raw_input('Not a valid action.  Try Again! ')