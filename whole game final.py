from __future__ import print_function
playerItems = []
enteredRooms = []
openedDoors = []
money = 0
times_entered_map = 0
def readMap(): #map of the world
    print("At the park there is a football field, a girl, a flower shop, a bench, and a playground")
    print("Navigate by saying where you want to go without using capital letters. Good luck!")
    center()
def center(): 
    global times_entered_map
    global playerItems
    global enteredRooms
    global openedDoors
    if times_entered_map == 0: #first time you enter gives instructions
        print("Welome to the park.You are at the map in the middle of the park.")
        print("You came to the park looking for money to pay for your date.")
        print("You also need a girlfriend to go on the date")
        print("All roads in the park lead through the map. You can see the places by saying 'read map'")
        print("Good luck")
        times_entered_map += 1
    while times_entered_map == 1: #every other time runs this based on what user says runs a dif function taking them to another room
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
        else:
            print("I don't understand that")
            user = raw_input("Try again: ")
        



def flowers():
    global playerItems
    global openedDoors
    global position
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
            center()
    elif userAction == 'buy flowers' and money < 30: #if money , 30, can't enter room and will kick out.
        print('Sorry, you do not have the proper funds! Go get more money!')
    else:
        userAction = raw_input('Not a valid action.  Try Again! ')




def playground():
    global position
    global playerItems
    global enteredRooms
    global openedDoors
    global money
    exitRoom = False
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
                exitRoom = True
        elif (userAction == 'return to map') or (userAction == 'go to map') or (userAction =='go back to map') or (userAction == 'walk to map'):#This section of code lets the user return to the map in the center of the park
            exitRoom = True
            center()
        else:
            userAction = raw_input('Not a valid action.  Try Again! ')




def restart(): #resets everything back to original 
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
            center()
        else:
            print("Fine. Game over")
        
        
   
def bench():
    global playerItems
    global enteredRooms
    global openedDoors
    if "bench" in enteredRooms: #can't enter twice
        print("You've already been here. Go back to map")
    else:
        enteredRooms.append("bench")        
        print("You have walked down towards the bench. ")
        print("You see a purse lying there unattended. ")
        print("You really need more money. What do you do?")
        print("Leave the purse alone? Or take the money you need")
        user = raw_input()
        if user == "leave the purse alone": #depending on what user says you either win the room or restart
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


def footballField(): 
    exitRoom = False
    defense = False
    global enteredRooms
    while exitRoom == False:
        print('You arrived at the football field')
        #This next code is what calls for user input on whether or not they want to play the game
        userAction = raw_input('A child walks up to you and challenges you to a football game. If you win you get $10. Do you accept his challenge?')
        #if they say yes then it asks them if they want to run or pass the football
        if userAction == 'yes' or userAction ==  'Yes':
            print ('The game has begun')
            userAction = raw_input ('Choose what play you want to execute, pass or run?')
            #If they say pass it runs a pass scenerio
            if userAction == 'pass' or userAction == 'Pass':
                print ('You chose a pass play.')
                print ('You are the Quarterback.')
                print ('You hike the football and drop back to pass')
                userAction = raw_input('You have 3 recievers, a, b,and c. All of them are covered by a defender. Choose which reciever to throw it to.')
                if userAction == 'a'or userAction == 'A':
                    userAction = raw_input('They are running a vertical route. Would you like to throw a bullet or a bomb?')
                    if userAction == 'bullet' or userAction ==  'Throw a bullet' or userAction == 'throw a bullet':
                        print ('Moron. What a horrible decision. You severly underthrew the reciever and your pass was intercepted!')
                        print ('Now the other team has the chance to win')
                      #if they throw a pick it set the variable defense to true
                        defense = True
                    if userAction == 'bomb' or userAction == 'Throw a bomb' or userAction == 'throw a bomb':
                        print ('Good choice. The reciever catches the ball for a touchdown. You won the game! You get $10!')
                        #if they score then it gets them out of the loop so that they can go to other rooms. 
                        exitRoom = True
                if userAction == 'b' or userAction == 'B':
                    '''All if statements that are dependent upon the user input. There are many decisions to be made, each of which can lead to success or failure.
                    The initial decision is always less significant than the follow up question.''' 
                    userAction = raw_input('They are running a slant route. Would you like to throw a bullet or a bomb?')
                    if userAction == 'bullet' or userAction =='Throw a bullet' or userAction =='throw a bullet': #Different options to communicate the same idea
                        print ('Smart decision.')
                        print ('The reciever caught the pass, but was tackled for a small gain.')
                        userAction = raw_input('You now have to run another play, pass or run?')
                        if userAction == 'pass' or userAction == 'Pass': #The user can capitalize or not, it doesnt matter
                            print ('You chose pass play. You hike the football and drop back to pass.')
                            print ('The defense decided to blitz and they are bringing pressure.')
                            userAction = raw_input('Are you going to tuck and run, or launch it deep.')
                            if userAction == 'tuck and run' or userAction == 'Tuck and run':
                                print ('You decided to tuck and run.')
                                print ('You get past the first defender but fast approaching another.')
                                userAction = raw_input('How do you want to get around him: juke right or juke left')
                                if userAction == 'juke right' or userAction == 'Juke right':
                                    print ('You try to juke right but the defender read you mind and tackles you.')
                                    print ('Your clumsy self fumbled the football and now the other team has a chance to score.')
                                    defense = True #This calls 'defense'. There's no good option, either left or right leads to calling defense
                                if userAction == 'juke left' or userAction =='Juke left': #user input for trying to avoid defense
                                    print ('You broke their ankles and break free into the secondary.')
                                    print ('A smaller child runs towards you to tackle you.')
                                    userAction = raw_input('How do you want to get past them, stiff arm or truck them.')
                                    if userAction == 'stiff arm' or userAction =='Stiff arm':
                                        #still trying to get past the defender.
                                        print ('You try to stiff arm them but they are small enough to duck it and wrap around your ankles.')
                                        print ('You are humilated that you were tackled by a 3 year old.')
                                        print ('Everyone is laughing at you what do you do, go back to the playground, or fight the children.')
                                        if userAction == 'go back to the playground' or userAction == 'Go back to the playground':
                                            #At this point they aren't going to win this one so I had a bit of fun with it.
                                            print ('You are a pathetic loser. Restart the game')
                                            restart()
                                        if userAction == 'fight the children' or userAction == 'Fight the children': #At this point they aren't going to win this one so I had a bit of fun with it.
                                            print ('You find the leader of the children and slam him on the ground.')
                                            print ('The other children try to pull you off but are too weak')
                                            print ('As you are on top of the kid the cops see you and arrest you.')
                                            print ('I do not think you are going to win the girl with that attitude.')
                                            restart()
                                    if userAction == 'truck them' or userAction =='Truck them': #win the game by choosing truck them and you exit room
                                        print ('You truck the weakling and celebrate your way into the endzone')
                                        print ('You score and win the game. You got your $10')
                                        exitRoom = True
                            if userAction == 'launch it deep' or userAction =='Launch it deep': #you choose the wrong thing and go back to defense
                                print ('You close you eyes and throw a prayer towards the endzone.')
                                print ('Your prayers were not answered however as your pass was intercepted. Good job Mark Sanchez.')
                                defense = True
                        if userAction == 'run' or userAction =='Run': #if you run the ball you fumble and decide whether to play defense or you die
                            print('You chose to peform a run play.')
                            print('You try to hand the ball off to your running back but he drops the football.')
                            userAction = raw_input('Do you dive on the ball or let the defense take it?')
                            if userAction == 'dive on the ball' or userAction =='Dive on the ball':
                                print('You dive on the ball but all the dhildren fall on top of you and crush you.')
                                print ('You died.')
                                restart()
                            if userAction == 'let the defense take it' or userAction =='Let the defense take it':
                                print('What a weakling. You watch the other team take the football.')
                                defense = True
                    if userAction == 'bomb'  or userAction =='Bomb' or userAction =='Throw a bomb' or userAction =='throw a bomb': #choose wrong option so you play defense
                        print ('Well that was stupid. Your overthrew the reciever by a mile and the pass was intercepted. It is like watching the Packers out here.')
                        defense = True
                if userAction == 'c' or userAction =='C': #what happens if they choose the other reciever
                    userAction = raw_input('They are running a screen route. Would you like to bulled or a bomb?')
                    if userAction == 'bullet' or   userAction == 'throw a bullet' or userAction =='Bullet' or userAction =='Throw a bullet': #choose the type of pass
                        print('You try to throw a bullet pass but you throw a backwards pass that the reciever drops')
                        print('Instead of picking up the football you watch helplessly as your reciever throws a hissy fit and the other team picks up the football and scores.')
                        print('You are such a failure!')
                        restart()
                    if userAction == 'bomb' or userAction =='Bomb' or userAction =='Throw a bomb' or userAction =='throw a bomb':
                        print('No one but you knows why you decide to throw a bomb on a screen pass, but I guess you do.')
                        print('Then again why anyone would be pathetic enough to throw a screen pass is beyond me.')
                        print('Lucky for you the reciever makes a remarkable catch, but only gets a couple yards.')
                        userAction = raw_input('Time for another play. What type of play do you want to do, pass or run? ')
                        if userAction == 'pass' or userAction =='Pass': #second play
                            print('As the star quarterback you hike the ball and drop back to pass')
                            userAction = raw_input('Your best reciever is running free deep do you want to launch it to him, yes or no? ')
                            if userAction == 'yes' or userAction =='Yes': 
                                print('Dang. Unlucky for you the safety read your mind and shaded over at the last second and picked you off.')
                                print('Sucks to suck my dude.')
                                defense = True
                            if userAction == 'no' or userAction =='No': 
                                print ('Good call. The safety began shifting that way leaving your running back wide open.')
                                userAction = raw_input('What do you do, throw a bullet, throw a bomb, or wait for something else? ')
                                if userAction == 'throw a bullet' or userAction =='bullet' or userAction =='Throw a bullet' or userAction =='Bullet': #3rd play
                                    print('Your running back tries to come back for the ball but it is batted down by the corner back. Incomplete.')
                                    print('This is 3rd down. It is time for greatness.')
                                    userAction = raw_input('You decide your fate, pass or run? ')
                                    if userAction == 'pass'  or userAction =='Pass': 
                                        print('You have a new found faith in your throwing ability.')
                                        print('You hike the football and drop back to pass.')
                                        print ('All your reciever are running verticals. It is miracle time.')
                                        userAction = raw_input('Do you, let it fly or throw back corner? ')
                                        if userAction == 'let it fly' or userAction =='Let if fly':
                                            print('Sadly your dumb choice gave the ball to the other team via interception. GARBAGE!!!')
                                            defense = True
                                        if userAction == 'throw back corner' or userAction =='Throw back corner':
                                            print ('Good call. Your reciver made a dart to the back corner and makes a tremendous catch.')
                                            print ('Congrats on beating the 5 year olds. You got $10.')
                                            exitRoom = True
                                       
                                    if userAction =='run' or userAction =='Run': #if they run
                                        print ('Lame only weaklings try to run the football.')
                                        print ('The defense looks like they are blitzing.')
                                        userAction = raw_input('Would you like to audible, yes or no? ')#what should they do
                                        if userAction == 'yes' or userAction =='Yes':
                                            print ('You audibled to a pass play.')
                                            userAction = raw_input('All your recievers run deep. Do you throw a bomb or finesse it? ')
                                            if userAction == 'throw a bomb' or userAction =='bomb' or userAction == 'Throw a bomb' or userAction =='Bomb':
                                                print ('Congrats you are the worst quarterback in the world. Interception for you.')
                                                defense = True
                                            if userAction == 'finesse it' or userAction =='Finesse it':
                                                print ('PERFECT PASS INTO THE ENDZONE! TOUCHDOWN! YOU WIN! You recieve $10 dollars for your efforts')
                                                exitRoom = True
                                              
                                        if userAction == 'no' or userAction =='No':
                                            print('Moron. You are sacked and lose and fumble. They pick up the ball and take into the endzone. You lose!')
                                            restart()
                                        
                                          
                                if userAction == 'throw a bomb' or userAction =='Throw a bomb':                       #you win             
                                    print('Good call. The running back snags the football and streaks into the endzone. TOUCHDOWN!!! You win $10')
                                    exitRoom = True
                                if userAction == 'wait for something else' or userAction =='Wait for something else':
                                    print('That was stupid. You just watch a dub go by.')
                                    print('Instead you get sacked and fumble the football. Good job idiot.')
                                    defense = True
                               
                        if userAction == 'run' or userAction =='Run': #you win
                            print('You hand the ball off to the running back and watch in awe as he carries your team.')
                            print ('He breaks 7 tackles on his way to the endzone winning the game for your team.')
                            print('Congrats on winning $10 by doing nothing.')
                            exitRoom = True
                        
                              
            if userAction == 'run' or userAction =='Run': #you die
                print('You wanted to win but your team was conspiring against you and intentionally gives the ball to the other team.')
                print('You watch helplessly as the other team showboats their way into the endzone for a touchdown.')
                print('What a loser. Next time try not to be pathetic.')
                print('Now you gotta start all over again.')
                restart()
            if defense ==True: #code for whenever the girl 
                print('You must now defend the best offense to ever exist.')
                userAction = raw_input('Do you want to play conservative defense, aggressive defense, or give up? ')
                if userAction == 'conservative defense' or userAction =='Conservative' or userAction =='Conservative defense' or userAction =='conservative':
                    print('The running back for the other team destroys your entire defense and scores a touchdown on 3 plays. Should have been more aggressive. ')
                    restart()
                if userAction == 'aggressive defense' or userAction == 'aggressive' or userAction =='Aggressive defense' or userAction =='Aggressive':
                    print ('The quarterback fakes a hand off and then burns you for a 68 yard touchdown. Should have been more conservative. ')
                    restart()
                if userAction == 'give up' or userAction == 'Give up':
                    print ('That is no way to win a girl. Only those who deserve the victory get the girl.')
                    restart()
        if userAction == 'no' or userAction =='No': # you lose
            print ('You must say yes to win the girl. Try again. ')
            restart()
    if exitRoom == True:
        center()        
    if 'footballField' in enteredRooms: #can't play the game twice
        print('You have already played the game. Everyone hates you and you can not play again. You have been banished back to the park.')
    if 'footballField' not in enteredRooms: #adds it so you can't play again
        enteredRooms += ['footballField']