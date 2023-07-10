from collections import deque
import sys
input = sys.stdin.readline

def solution(K:int,C:int,R:int,arr:list[list[int]])->int:
    nomal_dr,nomal_dc = (1,0,0,-1),(0,1,-1,0)
    horse_dr,horse_dc = (2,2,1,1,-2,-2,-1,-1),(1,-1,2,-2,1,-1,2,-2)
    check = [[[False]*C for _ in range(R)] for __ in range(K+1)]
    check[0][0][0] = True
    W,H = C-1,R-1
    que = deque()
    que.append((0,0,0))
    cnt = 0
    while que:
        for _ in range(len(que)):
            r,c,k = que.popleft()
            if r == H and c == W:
                return cnt
            if k < K:
                nk = k +1
                for d in range(8):
                    nr,nc = r + horse_dr[d], c + horse_dc[d]
                    if inrange(R,C,nr,nc) and not check[nk][nr][nc] and arr[nr][nc] == 0:
                        check[nk][nr][nc] = True
                        que.append((nr,nc,nk))
            for d in range(4):
                nr,nc = r + nomal_dr[d], c + nomal_dc[d]
                if inrange(R,C,nr,nc) and not check[k][nr][nc] and arr[nr][nc] == 0:
                    check[k][nr][nc] = True
                    que.append((nr,nc,k))
        cnt += 1
    return -1

def inrange(R:int,C:int,r:int,c:int)->bool:
    if 0<=r<R and 0<=c<C:
        return True
    return False

K = int(input())
C,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
ans = solution(K,C,R,arr)
print(ans)