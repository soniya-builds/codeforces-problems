t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0] * 26
    ans = []

    for needed in a:
        for c in range(26):
            if freq[c] == needed:
                ans.append(chr(ord('a') + c))
                freq[c] += 1
                break

    print("".join(ans))
