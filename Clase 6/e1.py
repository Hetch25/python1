#Búsqueda del tesoro
print("Welcome to the treasure island")
print("Your mission is to find the treasure")

if input("left o right?: ").lower() == "left":
    if input("swim or wait?: ").lower() == "wait":
        color = input("Which door?: ").lower()
        if color == "yellow":
            print("You win")
        elif color == "blue":
            print("eaten by beast")
        elif color == "red":
            print("burned by fire")
        else:
            print("Game Over")
    else:
        print("Attacked by trout")
else:
    print("Fall into a black hole")