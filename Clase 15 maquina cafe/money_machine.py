class MoneyMachine:

    COIN_VALUES = {
                   'quarters':0.25,
                   'dime':0.10,
                   'nickles':0.05,
                   'pennies':0.01
    }

    SYMBOL = '$'

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f'Money {self.SYMBOL}{self.profit}')

    def process_coins(self):
        '''Return the total calculated from coins inserted'''
        print('Please insert coins')
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f'How many coins {coin}?'))*self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self,cost):
        '''Return True when payment is accepted, or False if insufficient'''
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost,2)
            print(f'Here is {self.SYMBOL} {change} in change')
            self.profit += cost
            self.money_received = 0
            return True

        else:
            print("Sorry, that's enough money. Money refunded.")
            self.money_received = 0
            return False
