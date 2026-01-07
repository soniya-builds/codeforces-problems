g, c, l = map(int, input().split())

scores = sorted([g, c, l])

if scores[2] - scores[0] >= 10:
    print("check again")
else:
    print(f"final {scores[1]}")
g, c, l = map(int, input().split())

scores = sorted([g, c, l])

if scores[2] - scores[0] >= 10:
    print("check again")
else:
    print(f"final {scores[1]}")