playerItems = ["purple flowers"]
def girl():
    stop = False
    print("You walk up to the girl and start talking to her")
    if "purple flowers" not in playerItems: #if you don't have flowers you can't interact with the girl
        print("You attempt to flirt with her, but she is angry that you didn't bring her a gift and sends you away")
        center() #sends you back to center
    else:
        print("You attempt to flirt with her, but it is obvious she wants a gift")
        userAction = raw_input("What do you do? ") #user chooses what to do
        while(stop == False):
            if (userAction == 'give her flowers') or (userAction == 'give her the flowers'): #if they say those lines they win the game else 
                print("She loves the flowers and agrees to go on a date with you")
                print("Congratulations you have won the game")
                stop = True
        
            else: 
                userAction = raw_input("I don't understand, maybe give her the flowers? ")
        