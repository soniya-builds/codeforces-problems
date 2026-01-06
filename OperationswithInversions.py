t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    max_so_far = arr[0]
    operations = 0

    for i in range(1, n):
        if arr[i] < max_so_far:
            operations += 1
        else:
            max_so_far = arr[i]

    print(operations)
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    max_so_far = arr[0]
    operations = 0

    for i in range(1, n):
        if arr[i] < max_so_far:
            operations += 1
        else:
            max_so_far = arr[i]

    print(operations)
