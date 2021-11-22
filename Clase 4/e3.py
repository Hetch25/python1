#Rollercoaster
height = int(input("Type your height in cm: "))

can_ride = False

if height >= 120:
    can_ride = True
#age < 12 --- $5
#age <= 18 --- $7
#age <= 45 ---$9
#free

if can_ride:
    age = int(input("How old are you?: "))
    ticket = 0
    if age < 12:
        ticket += 5
    elif age <= 18:
        ticket += 7
    elif age <= 45:
        ticket += 9

    photo = input("Do you want a photo?: (y/n)").lower()
    if photo == "y":
        ticket += 3  
    print(f"You have to pay {ticket} dollars")
elif not can_ride:
    print("You can't ride :(")
