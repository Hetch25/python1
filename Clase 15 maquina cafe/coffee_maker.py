class CoffeeMaker:
    '''Models the machine that makes coffee'''
    def __init__(self):
        self.resources = {'water':400,'milk':400,'coffee':400}

    def report(self):
        '''Prints a report of all sources'''
        print(f'Water: {self.resources["water"]} ml')
        print(f'Milk: {self.resources["milk"]} ml')
        print(f'Coffee: {self.resources["coffee"]} gr')

    def is_resources_sufficient(self,drink):
        '''Returns True when order can be made, False if ingredients are indufficient'''
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                can_make = False
        return can_make

    def make_coffee(self,order):
        ''''''
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f'Here is your {order.name}. Enjoy it')
