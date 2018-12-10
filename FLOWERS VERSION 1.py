money = 0

def flowers():
    global playerItems
    global openedDoors
    
    print('You have entered the flower shop')
    print('There are flowers of all different colors.')
    print('The shopowner asks if you would like to buy anything.')    
    userAction = raw_input('What would you like to do? ') #print statements don't actually do anything, just informing the players
    if userAction == 'buy flowers' and money >= 30: #if statement for success, if this is fulfilled and the correct color is chosen, player gains item required to advance
        print('Which color would you like?')
        if userAction != 'purple': #if the answer is anything other than purple, you lose the game. Don't mess up...
            print('store owner is infuriated you chose the wrong color' + ' you lose')
        else:
            print('Alright! Here are your flowers!') #Within an elif statement, this 'else' is for if userInput is 'purple'.
            print('You received purple flowers!') 
            playerItems += 'purpleflowers'    #adding purpleflowers to items, this will be needed for another room
    elif userAction == 'buy flowers' and money < 30: #if money , 30, can't enter room and will kick out.
        print('Sorry, you do not have the proper funds! Go get more money!')
    else:
        userAction = raw_input('Not a valid action.  Try Again! ')
   
   