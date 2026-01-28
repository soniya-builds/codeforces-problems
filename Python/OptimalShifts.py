# OptimalShifts.py

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    # If already all ones
    if '0' not in s:
        print(0)
        continue

    # Make string circular by doubling
    s2 = s + s

    max_zeros = 0
    curr = 0

    for ch in s2:
        if ch == '0':
            curr += 1
            max_zeros = max(max_zeros, curr)
        else:
            curr = 0

    # Cannot exceed n (full circle)
    print(min(max_zeros, n))
