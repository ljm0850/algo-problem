from collections import deque
import sys
N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]       # N 100이하
ch = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] :
            ch[i].append(j)

for i in range(N):
    stack = deque()
    for ii in ch[i]:
        stack.append(ii)
    while stack:
        t = stack.pop()
        for j in ch[t]:
            if not j in ch[i] and not j in stack :
                stack.append(j)
                ch[i].append(j)
solve = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j in ch[i]:
            solve[i].append(1)
        else:
            solve[i].append(0)

for sol in solve:
    print(*sol)