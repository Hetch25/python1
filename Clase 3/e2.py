#leap year
year = int(input("Type a year: "))

is_leap = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
    elif year % 100 != 0:
        is_leap = True

if is_leap:
    print(f"{year} is leap")
elif is_leap == False:
    print(f"{year} is not leap")
