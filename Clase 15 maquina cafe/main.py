from coffee_maker import CoffeeMaker
from menu import *
from money_machine import MoneyMachine
import os


"""Let's create all the objects we'll use"""
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? {options}')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        money_machine.report()
        coffe_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resources_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)

    os.system('clear')



