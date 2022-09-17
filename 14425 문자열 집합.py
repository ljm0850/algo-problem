import sys
N,M = map(int,sys.stdin.readline().split())
docs = set()
ans = 0
for _ in range(N):
    docs.add(sys.stdin.readline())
for _ in range(M):
    target = sys.stdin.readline()
    if target in docs:
        ans += 1
print(ans)