import sys
from collections import deque
input = sys.stdin.readline
def solve(s,e):
    global ans
    stack = deque()

    for i in range(1,N+1):
        if total[s][i] != -1:
            stack.append((i,total[s][i]))

    while stack:
        way,paid = stack.popleft()
        for j in range(1,N+1):
            temp = paid + total[way][j]
            if total[way][j] != -1:
                if total[s][j] == -1 or total[s][j] > temp:
                    total[s][j] = temp
                    stack.append((j,temp))
    return total[s][e]

N = int(input())
total = [[-1] * (N+1) for _ in range(N+1)]
M = int(input())
for _ in range(M):
    start,end,pay = map(int,input().split())
    if total[start][end] == -1:
        total[start][end] = pay
    else:
        total[start][end] = min(total[start][end],pay)

s,e = map(int,input().split())
ans = solve(s,e)
print(ans)