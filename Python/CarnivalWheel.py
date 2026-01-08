t = int(input())

for _ in range(t):
    l, a, b = map(int, input().split())

    visited = set()
    cur = a
    ans = a

    while cur not in visited:
        visited.add(cur)
        ans = max(ans, cur)
        cur = (cur + b) % l

    print(ans)
