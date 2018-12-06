money = 0

def flowers():
    global playerItems
    global openedDoors
    
    print('You have entered the flower shop')
    print('There are flowers of all different colors.')
    print('The shopowner asks if you would like to buy anything.')
    userAction = raw_input('What would you like to do? ')
    if userAction == 'buy flowers' and money >= 30: 
        print('Which color would you like?')
        if userAction != 'purple':
            print('store owner is infuriated you chose the wrong color' + 'restart')
        else:
            print('Alright! Here are your flowers!')
            print('You received purple flowers!') 
            playerItems += 'purpleflowers'    
    elif userAction == 'buy flowers' and money < 30:
        print('Sorry, you do not have the proper funds! Go get more money!')
    else:
        userAction = raw_input('Not a valid action.  Try Again! ')
   
   