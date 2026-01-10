import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 0:
        print(0)
    else:
        print(min(2 * n - 1, math.ceil(k / n)))
