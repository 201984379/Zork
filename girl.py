playerItems = []
def girl():
    print("You walk up to the girl and start talking to her")
    if "purple flowers" not in playerItems:
        print("You attempt to flirt with her, but she is angry that you didn't bring her a gift and sends you away")
        center()
    else:
        print("You attempt to flirt with her, but it is obvious she wants a gift")
        userAction = raw_input("What do you do")
        if (userAction == 'give her flowers') or (userAction == 'give her the flowers'):
            print("She loves the flowers and agrees to go on a date with you")
            print("Congratulations you have won the game")
        
        