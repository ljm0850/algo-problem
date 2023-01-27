import sys
input = sys.stdin.readline
total = 0
woods = set()
value = {}
while True:
    target = input().rstrip()
    if not target:
        break
    total += 1
    if target in woods:
        value[target] += 1
    else:
        value[target] = 1
        woods.add(target)

temp = sorted(woods)
for wood in temp:
    print(f'{wood} {(value[wood]/total)*100:.4f}')