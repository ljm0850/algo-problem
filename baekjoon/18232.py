from collections import deque
import sys
input = sys.stdin.readline

def solution(N:int,S:int,E:int,graph:list[list[int]])->int:
    check = [False]*(N+2)
    check[0] = True
    check[N+1] = True
    que = deque([S])
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):
            point = que.popleft()
            for nextPoint in (point+1,point-1,*graph[point]):
                if nextPoint == E: return cnt
                if check[nextPoint]: continue
                check[nextPoint] = True
                que.append(nextPoint)
    return 0

N,M = map(int,input().split())
S,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
ans = solution(N,S,E,graph)
print(ans)