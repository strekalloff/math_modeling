b1 = int(input())
q = int(input())
n_max = int(input())

for n in range(1, n_max+1):
    print(b1 * q ** (n - 1))
