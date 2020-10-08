a = int(input())
b = int(input())
c = int(input())
D = (b ** 2) - (4 * a * c)
if D > 0:
    x1 = ((-1 * b) + (D ** 1 / 2)) / (2 * a)
    x2 = ((-1 * b) - (D ** 1 / 2)) / (2 * a)
if D == 0:
    x = (-1 * b) / (2 * a)
if D < 0:
    print('Нет корней')
