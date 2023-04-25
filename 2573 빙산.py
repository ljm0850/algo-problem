import sys
from collections import deque
input = sys.stdin.readline

def findIce(N:int,M:int)->deque[tuple[int,int]]:
    ls = deque()
    for r in range(N):
        for c in range(M):
            if arr[r][c]:
                ls.append((r,c))
    return ls

def melting(r:int,c:int)->int:
    cnt = 0
    for d in range(4):
        nr,nc = r+dr[d],c+dc[d]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0:
            cnt += 1
    return cnt

def checkIceberg(iceberg:deque[tuple[int,int]])->bool:
    if len(iceberg) == 0:
        return False
    check = set()
    ls = [iceberg[0]]
    while ls:
        r,c = ls.pop()
        for d in range(4):
            nr,nc = r+dr[d],c+dc[d]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] and not (nr,nc) in check:
                check.add((nr,nc))
                ls.append((nr,nc))

    for ice in iceberg:
        if not ice in check:
            return True
    return False

def solution(N:int,M:int)->int:
    iceberg = findIce(N,M)
    cnt = 0
    while iceberg:
        flag = False
        cnt += 1
        temp = []
        for _ in range(len(iceberg)):
            r,c = iceberg.popleft()
            sea = melting(r,c)
            temp.append((r,c,sea))

        for r,c,sea in temp:
            arr[r][c] -= sea
            if arr[r][c] <=0:
                arr[r][c] = 0
                flag = True
            else:
                iceberg.append((r,c))
        if flag:
            T = checkIceberg(iceberg)
            if T:
                return cnt
    return 0

N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr,dc = (1,-1,0,0),(0,0,1,-1)
ans = solution(N,M)
print(ans)