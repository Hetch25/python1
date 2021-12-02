#recursión de una función
"""def factorial_(n): #no contiene recursión
    factorial = 1
    while n >= 1:
        factorial = factorial * n
        n-= 1
    return factorial"""

"""print(factorial_(6))"""
n = int(input("Type a number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial(n-1)
    
print(factorial(n))