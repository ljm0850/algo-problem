import sys
input = sys.stdin.readline
from collections import deque

def div_island(r:int,c:int,value:int)->deque:
    arr[r][c] = value
    total = deque()
    total.append((r,c))
    ls = [(r,c)]
    while ls:
        r,c = ls.pop()
        for d in range(4):
            nr,nc = r+dr[d],c+dc[d]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 1:
                arr[nr][nc] = value
                ls.append((nr,nc))
                total.append((nr,nc))
    return total

def check(que:deque[tuple[int,int]])->int:
    cnt = 0
    visit = [[False for _ in range(N)] for __ in range(N)]
    value = arr[que[0][0]][que[0][1]]

    while que:
        for _ in range(len(que)):
            r,c = que.popleft()
            for d in range(4):
                nr,nc = r+dr[d],c+dc[d]
                if 0<=nr<N and 0<=nc<N and not visit[nr][nc]:
                    if arr[nr][nc] == 0:
                        que.append((nr,nc))
                        visit[nr][nc] = True
                    elif arr[nr][nc] != value:
                        return cnt
        cnt += 1

def solution(N:int)->int:
    island_cnt = 2
    value = 2*N
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                ls = div_island(i, j, island_cnt)
                now_value = check(ls)
                value = min(value,now_value)
                island_cnt += 1
    return value

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dr,dc = (1,-1,0,0),(0,0,1,-1)
ans = solution(N)
print(ans)