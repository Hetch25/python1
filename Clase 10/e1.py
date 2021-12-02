#Funciones
"""def sum(x,y):
    return x + y
print(sum(x = 2,y = 3))
print(sum(-2,10)) #Ambas formas se utilizan, pero es mejor sin definir x,y de nuevo dentro de sum"""

def max(a,b):
    return a > b
    """if a>b:
        return True
    else:
        return False"""

x = int(input("Type a number: "))
y = int(input("Type another number: "))
if max(x,y):
    print("First number is bigger than second")
else:
    print("Second number is bigger than first")