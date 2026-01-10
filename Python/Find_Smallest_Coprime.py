import math

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))


    if 1 in arr:
        print(2)
        continue

    x = 2
    while True:
        ok = False
        for v in arr:
            if math.gcd(v, x) == 1:
                ok = True
                break
        if ok:
            print(x)
            break
        x += 1
