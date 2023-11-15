import sys
from collections import deque
input = sys.stdin.readline
def solution(R,C,sr,sc):
    global graph
    dr,dc = (1,-1,0,0),(0,0,1,-1)
    goal = {3,4,5}
    check = [[False]*C for _ in range(R)]
    check[sr][sc] = True
    que = deque()
    que.append((sr,sc))
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):
            r,c = que.popleft()
            for d in range(4):
                nr,nc = r + dr[d], c + dc[d]
                if 0<=nr<R and 0<=nc<C and not check[nr][nc] and graph[nr][nc] != 1:
                    check[nr][nc] = True
                    if graph[nr][nc] in goal:
                        return cnt
                    que.append((nr,nc))
    return 0

R,C = map(int,input().split())
graph = []
sr,sc = 0,0
for r in range(R):
    temp = list(map(int,input().rstrip()))
    for c in range(C):
        if temp[c] == 2:
            sr,sc = r,c
    graph.append(temp)
ans = solution(R,C,sr,sc)
if ans:
    print("TAK")
    print(ans)
else:
    print("NIE")