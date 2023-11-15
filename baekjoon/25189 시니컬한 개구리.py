from collections import deque
import sys
input = sys.stdin.readline
def isHome(rh:int,ch:int,r:int,c:int)->bool:
    if r == rh and c == ch:
        return True
    return False
def solution(rf:int,cf:int,rh:int,ch:int,R:int,C:int)->int:
    if isHome(rh,ch,rf,cf):
        return 0
    dr,dc = (1,-1,0,0),(0,0,1,-1)
    check = [[[False]*M for _ in range(N)] for __ in range(2)]
    rowCheck = [False]*(R)
    colCheck = [False]*(C)
    check[0][rf][cf] = True
    que = deque()
    que.append((rf,cf,0))
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):
            r,c,ignore = que.popleft()
            v = arr[r][c]
            for d in range(4):
                nr,nc = r + v * dr[d], c + v * dc[d]
                if 0<=nr<R and 0<=nc<C and not check[ignore][nr][nc]:
                    if isHome(rh,ch,nr,nc):
                        return cnt
                    check[ignore][nr][nc] = True
                    check[1][nr][nc] = True
                    que.append((nr,nc,ignore))
            if ignore == 0:
                if not rowCheck[r]:
                    rowCheck[r] = True
                    nr = r
                    for d in range(2,4):
                        v = 1
                        while True:
                            nc = c + v * dc[d]
                            if 0<=nc<C:
                                if not check[1][nr][nc]:
                                    if isHome(rh,ch,nr,nc):
                                        return cnt
                                    check[1][nr][nc] = True
                                    que.append((nr,nc,1))
                                v += 1
                            else:
                                break
                if not colCheck[c]:
                    colCheck[c] = True
                    nc = c
                    for d in range(2):
                        v = 1
                        while True:
                            nr = r + v * dr[d]
                            if 0<=nr<R:
                                if not check[1][nr][nc]:
                                    if isHome(rh,ch,nr,nc):
                                        return cnt
                                    check[1][nr][nc] = True
                                    que.append((nr,nc,1))
                                v += 1
                            else:
                                break
    return -1

N,M = map(int,input().split())
rf,cf,rh,ch = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = solution(rf-1,cf-1,rh-1,ch-1,N,M)
print(ans)