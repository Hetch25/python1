#Se creará un diccionario
"""dictionary = {}

dictionary['superman'] = 'He is very strong'
dictionary['flash'] = "He's the fastest man over the world"
dictionary.pop("superman")"""

dictionary = {'superman':{'power1':"He's very strong",'power2':"He can fly"},'flash':"He's the fastest man over the world",
'green lantern':"He's the chosen one"}

for key in dictionary:
    print(key)
    print(dictionary[key])