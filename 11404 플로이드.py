import sys
from collections import deque
def check(s):
    que = deque()
    for i in range(n):
        if bus[s][i]:
            que.append((i,bus[s][i]))

    while que:
        now,toll = que.popleft()
        for next in range(n):
            if next == s:
                continue
            if bus[now][next] and (not bus[s][next] or toll + bus[now][next] < bus[s][next]):
                bus[s][next] = toll + bus[now][next]
                que.append((next,toll + bus[now][next]))


n = int(input())        # 도시의 수
m = int(input())        # 버스의 개수
bus = [[0]*(n) for _ in range(n)]
for _ in range(m):
    a,b,pay = map(int,sys.stdin.readline().split())
    if not bus[a-1][b-1]:
        bus[a-1][b-1] = pay
    else:
        bus[a-1][b-1] = min(bus[a-1][b-1],pay)
for start in range(n):
    check(start)

for ans in bus:
    print(*ans)