t = int(input())
LIMIT = 10**18

for _ in range(t):
    n = int(input())
    colors = list(map(int, input().split()))

    distinct = set(colors)
    k = len(distinct)

    if k in distinct:
        print(k)
    else:
        print(k + (LIMIT - n))
