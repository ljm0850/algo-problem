import sys
input = sys.stdin.readline
N = int(input())
tips = [0]+[int(input()) for _ in range(N)]
tips.sort()
ans = 0

for i in range(N):
    value = tips[N-i] - i
    if value > 0:
        ans += value
    else:
        break
print(ans)