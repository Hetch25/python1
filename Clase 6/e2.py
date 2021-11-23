#juego de piedra, papel o tijera
"""list1 = [1,3,4,5]
list1.insert(1,2)
print(list1)"""

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list1 =[rock,paper,scissors]

choice = int(input("Make a choice 0-rock, 1-paper, 2-scissors: "))
computer = random.randint(0,len(list1)-1)

if choice == 0 and computer == 2:
    print("You win")
elif computer == 0 and choice ==2:
    print("You lose")
elif computer > choice:
    print("You lose")
elif choice == computer:
    print("It's a tie")
elif choice > computer:
    print("You win")

print("User")
print(list1[choice])
print("Computer")
print(list1[computer])