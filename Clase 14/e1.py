"""#Programación orientada a objetos (POO)
#mesero 1
name = 'Raul'
age = 20
uniform = 'red'
salary = 150 #esta forma de hacerlo es muy larga y no sirve, por lo tanto se hace una plantilla"""

#waiter
class Waiter:

    def __init__(self,name,age,weekend): #atributos de la clase, es la inicialización de un mesero
        self.name = name
        self.age = age
        self.gender ='male'
        self.work_on_weekends = weekend
        self.introduce()
        self.menu()
    

    def introduce(self):
        print(f'Hello, my name is {self.name}')

    def menu(self):
        print('The menu today is...')

    def work_on_weekend(self):
        if self.work_on_weekends:
            print(f'{self.name} works on weekends')
        else:
            print(f"{self.name} doesn't works on weekends")

waiter1 = Waiter('Raul',20,True)
waiter1.work_on_weekend()
#waiter2 = Waiter('Antonio',24,False)

