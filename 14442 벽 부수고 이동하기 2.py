from collections import deque
import sys
input = sys.stdin.readline
def solution(R:int,C:int,K:int,arr:list[list[int]])->int:
    if R == 1 and C == 1:
        return 1

    Tr,Tc = R-1,C-1
    que = deque()
    que.append((0,0,0))
    check = [[[0]*C for _ in range(R)] for __ in range(K+1)]
    check[0][0][0] = 1
    dr,dc = (1,0,0,-1),(0,1,-1,0)
    while que:
        r,c,k = que.popleft()
        value = check[k][r][c]
        nvalue,nk = value + 1, k + 1
        for d in range(4):
            nr,nc = r+dr[d],c+dc[d]
            if not (0<=nr<R and 0<=nc<C):
                continue
            if arr[nr][nc] == 1:
                if nk <= K and not check[nk][nr][nc]:
                    if nr == Tr and nc == Tc:
                        return nvalue
                    check[nk][nr][nc] = nvalue
                    que.append((nr,nc,nk))
            else:
                if not check[k][nr][nc]:
                    if nr == Tr and nc == Tc:
                        return nvalue
                    check[k][nr][nc] = nvalue
                    que.append((nr,nc,k))
    return -1

R,C,K = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(R)]
ans = solution(R,C,K,arr)
print(ans)