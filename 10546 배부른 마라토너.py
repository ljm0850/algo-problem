import sys
input = sys.stdin.readline
N = int(input())
check = {}
for _ in range(N):
    name = input()
    check[name] = check.get(name,0) + 1
for _ in range(N-1):
    name = input()
    check[name] -= 1

for name,cnt in check.items():
    if cnt:
        print(name)
        break