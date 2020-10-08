a = int(input())
b = int(input())
c = int(input())
if a + b > c and b + c > a and a + c > b:
    print('Треугольник существует')
    if a == b or a == c:
        print('Треугольник равнобедренный')
    elif a == b and a == c and b == c:
        print('Треугольник равносторонний')
    else:
        print('Треугольник разносторонний')
else:
    print('None')
