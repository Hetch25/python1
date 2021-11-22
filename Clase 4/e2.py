#leap year
year = int(input("Type a year: "))

is_leap = False
"""#if year % 4 == 0:
#   if year % 100 == 0:
#       if year % 400 == 0:
#           is_leap = True
#   elif year % 100 != 0:
#       is_leap = True
# las compuertas lógicas sirven para ejecutar  el mismo ciclo de arriba con los condicionales anidados"""
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    is_leap = True
elif year % 4 == 0 and year % 100 != 0:
    is_leap = True

if is_leap:
    print(f"{year} is leap")
elif not is_leap:
    print(f"{year} is not leap")
