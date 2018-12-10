from ethicaldecisionfinished_ import restart
enteredRooms = []
def footballField():
    exitRoom = False
    defense = False
    global enteredRooms
    while exitRoom == False:
        print('You arrived at the football field')
        userAction = raw_input('A child walks up to you and challenges you to a football game. If you win you get $10. Do you accept his challenge?')
        if userAction == 'yes' or userAction ==  'Yes':
            print ('The game has begun')
            userAction = raw_input ('Choose what play you want to execute, pass or run?')
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
                        defense = True
                    if userAction == 'bomb' or userAction == 'Throw a bomb' or userAction == 'throw a bomb':
                        print ('Good choice. The reciever catches the ball for a touchdown. You won the game!')
                if userAction == 'b' or userAction == 'B':
                    userAction = raw_input('They are running a slant route. Would you like to throw a bullet or a bomb?')
                    if userAction == 'bullet' or userAction =='Throw a bullet' or userAction =='throw a bullet':
                        print ('Smart decision.')
                        print ('The reciever caught the pass, but was tackled for a small gain.')
                        userAction = raw_input('You now have to run another play, pass or run?')
                        if userAction == 'pass' or userAction == 'Pass':
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
                                    defense = True
                                if userAction == 'juke left' or userAction =='Juke left':
                                    print ('You broke their ankles and break free into the secondary.')
                                    print ('A smaller child runs towards you to tackle you.')
                                    userAction = raw_input('How do you want to get past them, stiff arm or truck them.')
                                    if userAction == 'stiff arm' or userAction =='Stiff arm':
                                        print ('You try to stiff arm them but they are small enough to duck it and wrap around your ankles.')
                                        print ('You are humilated that you were tackled by a 3 year old.')
                                        print ('Everyone is laughing at you what do you do, go back to the playground, or fight the children.')
                                        if userAction == 'go back to the playground' or userAction == 'Go back to the playground':
                                            print ('You are a pathetic loser. Restart the game')
                                            restart()
                                        if userAction == 'fight the children' or userAction == 'Fight the children':
                                            print ('You find the leader of the children and slam him on the ground.')
                                            print ('The other children try to pull you off but are too weak')
                                            print ('As you are on top of the kid the cops see you and arrest you.')
                                            print ('I do not think you are going to win the girl with that attitude.')
                                            restart()
                                    if userAction == 'truck them' or userAction =='Truck them':
                                        print ('You truck the weakling and celebrate your way into the endzone')
                                        print ('You score and win the game. You got your $10')
                            if userAction == 'launch it deep' or userAction =='Launch it deep':
                                print ('You close you eyes and throw a prayer towards the endzone.')
                                print ('Your prayers were not answered however as your pass was intercepted. Good job Mark Sanchez.')
                                defense = True
                        if userAction == 'run' or userAction =='Run':
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
                    if userAction == 'bomb'  or userAction =='Bomb' or userAction =='Throw a bomb' or userAction =='throw a bomb':
                        print ('Well that was stupid. Your overthrew the reciever by a mile and the pass was intercepted. It is like watching the Packers out here.')
                        defense = True
                if userAction == 'c' or userAction =='C':
                    userAction = raw_input('They are running a screen route. Would you like to bulled or a bomb?')
                    if userAction == 'bullet' or   userAction == 'throw a bullet' or userAction =='Bullet' or userAction =='Throw a bullet':
                        print('You try to throw a bullet pass but you throw a backwards pass that the reciever drops')
                        print('Instead of picking up the football you watch helplessly as your reciever throws a hissy fit and the other team picks up the football and scores.')
                        print('You are such a failure!')
                        restart()
                    if userAction == 'bomb' or userAction =='Bomb' or userAction =='Throw a bomb' or userAction =='throw a bomb':
                        print('No one but you knows why you decide to throw a bomb on a screen pass, but I guess you do.')
                        print('Then again why anyone would be pathetic enough to throw a screen pass is beyond me.')
                        print('Lucky for you the reciever makes a remarkable catch, but only gets a couple yards.')
                        userAction = raw_input('Time for another play. What type of play do you want to do, pass or run? ')
                        if userAction == 'pass' or userAction =='Pass':
                            print('As the star quarterback you hike the ball and drop back to pass')
                            userAction = raw_input('Your best reciever is running free deep do you want to launch it to him, yes or no? ')
                            if userAction == 'yes' or userAction =='Yes':
                                print('Dang. Unlucky for you the safety read your mind and shaded over at the last second and picked you off.')
                                print('Sucks to suck my dude.')
                                defense = True
                            if userAction == 'no' or userAction =='No':
                                print ('Good call. The safety began shifting that way leaving your running back wide open.')
                                userAction = raw_input('What do you do, throw a bullet, throw a bomb, or wait for something else? ')
                                if userAction == 'throw a bullet' or userAction =='bullet' or userAction =='Throw a bullet' or userAction =='Bullet':
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
                                        if userAction == 'throw back corner' or userAction =='Throw back corner:
                                            print ('Good call. Your reciver made a dart to the back corner and makes a tremendous catch.')
                                            print ('Congrats on beating the 5 year olds. You got $10.')
                                       
                                    if userAction =='run' or userAction =='Run':
                                        print ('Lame only weaklings try to run the football.')
                                        print ('The defense looks like they are blitzing.')
                                        userAction = raw_input('Would you like to audible, yes or no? ')
                                        if userAction == 'yes' or userAction =='Yes':
                                            print ('You audibled to a pass play.')
                                            userAction = raw_input('All your recievers run deep. Do you throw a bomb or finesse it? ')
                                            if userAction == 'throw a bomb' or userAction =='bomb' or userAction == 'Throw a bomb' or userAction =='Bomb':
                                                print ('Congrats you are the worst quarterback in the world. Interception for you.')
                                                defense = True
                                            if userAction == 'finesse it' or userAction =='Finesse it':
                                                print ('PERFECT PASS INTO THE ENDZONE! TOUCHDOWN! YOU WIN! You recieve $10 dollars for your efforts')
                                              
                                        if userAction == 'no' or userAction =='No':
                                            print('Moron. You are sacked and lose and fumble. They pick up the ball and take into the endzone. You lose!')
                                            restart()
                                        
                                          
                                if userAction == 'throw a bomb' or userAction =='Throw a bomb':                                    
                                    print('Good call. The running back snags the football and streaks into the endzone. TOUCHDOWN!!! You win $10')
                                if userAction == 'wait for something else' or userAction =='Wait for something else':
                                    print('That was stupid. You just watch a dub go by.')
                                    print('Instead you get sacked and fumble the football. Good job idiot.')
                                    defense = True
                               
                        if userAction == 'run' or userAction =='Run':
                            print('You hand the ball off to the running back and watch in awe as he carries your team.')
                            print ('He breaks 7 tackles on his way to the endzone winning the game for your team.')
                            print('Congrats on winning $10 by doing nothing.')
                        
                              
            if userAction == 'run' or userAction =='Run':
                print('You wanted to win but your team was conspiring against you and intentionally gives the ball to the other team.')
                print('You watch helplessly as the other team showboats their way into the endzone for a touchdown.')
                print('What a loser. Next time try not to be pathetic.')
                print('Now you gotta start all over again.')
                restart()
            if defense == userAction ==True:
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
        if userAction == 'no' or userAction =='No':
            print ('You must say yes to win the girl. Try again. ')
            restart()
if 'footballField' in enteredRooms:
    print('You have already played the game. Everyone hates you and you can not play again. You have been banished back to the park.')
if 'footballField' not in enteredRooms:
    enteredRooms += ['footballField']
    

