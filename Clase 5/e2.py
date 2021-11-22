#lanzar una moneda
import random

coin = ["head","tails"]
#print(random.choice(coin))
if random.choice(coin) == "head":
    print("head")
else:
    print("tails")
#se pueden usar ambas cosas