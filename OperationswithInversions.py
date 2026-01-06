t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    kept = []
    for x in a:
        if not kept or x >= kept[-1]:
            kept.append(x)

    print(n - len(kept))
