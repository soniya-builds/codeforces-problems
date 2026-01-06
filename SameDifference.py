t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    last_char = s[-1]
    operations = 0

    for ch in s:
        if ch != last_char:
            operations += 1

    print(operations)
