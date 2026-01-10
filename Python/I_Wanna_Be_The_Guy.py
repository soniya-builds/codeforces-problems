n = int(input())

x_data = list(map(int, input().split()))
y_data = list(map(int, input().split()))

levels = set()


for lvl in x_data[1:]:
    levels.add(lvl)

for lvl in y_data[1:]:
    levels.add(lvl)

if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
