class MenuItem:
    '''Models each menu item'''
    def __init__(self,name,water,milk,coffee,cost):
        self.name = name
        self.cost = cost
        self.ingredients = {'water':water,
                            'milk':milk,
                            'coffee':coffee}

        """self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost
"""

class Menu:
    '''Models the menu with drinks'''
    def __init__(self):
        self.menu = [MenuItem(name='latte',water=70,milk=150,coffee=24,cost=2.5),
                     MenuItem(name='espresso', water=10,milk=0,coffee=18,cost=1.5),
                     MenuItem(name='cappuccino',water='80',milk=50,coffee=24,cost=3)]

    def get_items(self):
        '''Returns all the names of the available menu item'''
        options = ''
        for item in self.menu:
            options = options + f'{item.name}/'
        return options
    def find_drink(self,order_name):
        '''Searches the menu for a particular drink. Returns that item if exist
            otherwise returns none'''
        for item in self.menu:
            if item.name == order_name.lower():
                return item
        print('Sorry, that item is not available')