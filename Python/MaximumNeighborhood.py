t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(9)
    elif n == 3 or n == 4:
        print(4*n*n - n - 4)
    else:
        print(5*n*n - 5*n - 5)
