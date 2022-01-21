ye = int(input())

if ((ye % 4 == 0) and (ye % 100 != 0)) or (ye % 400 == 0):
    print(1)
else:
    print(0)
