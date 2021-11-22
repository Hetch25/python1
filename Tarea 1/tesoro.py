print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
direction = input("Choose a direction (left/right): ").lower()
level2 = False
if direction == "left":
    level2 = True 
    print("You pass to level 2")
    wtdo = input("What do you want to do?: (swim or wait) ").lower()
    level3 =False
    if wtdo == "wait":
        level3 = True
        print("You pass to level 3")
        wdoor = input("Choose a color to pass the dimensional portal: ").lower()
        win = False
        if wdoor == "yellow":
            win = True
            print("You are rich now, you have the secret treasure. CONGRATULATION MATE")
            if wdoor == "red":
                print("You are burning in lava. GAME OVER hahaha")
                if wdoor == "blue":
                    print("You died eaten by a large beast. GAME OVER hahaha") 
        elif not win:
                print("You are travelling to the centre of a massive star. GAME OVER hahaha")
    elif not level3:
        print("You were attacked by a water monster. GAME OVER hahaha")
elif not level2:
    print("You have fallen into a dark hole. GAME OVER hahaha")