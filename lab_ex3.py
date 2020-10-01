a=int(input('Enter num: '))
if a % 4 == 0 and a % 400 != 0:
    print('високосный')
else:
    print('невисокосный')