from collections import deque
import sys
input = sys.stdin.readline
def isRange(r,c,n):
    if 0<=r<n and 0<=c<n:
        return True
    return False

def solution(n,m,arr):
    if (arr[0][0] == 1) or (arr[n-1][n-1] == 1):
        return -1
    if n == 1:
        if arr[0][0] == 1:return -1
        else:return 0

    dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
    m2 = 2*m
    check = [[[-1] * m2 for _ in range(n)] for __ in range(n)]
    check[0][0][0] = 0
    que = deque()
    que.append((0, 0, 0))

    while que:
        r, c, cnt = que.popleft()
        turn = cnt % m2
        nturn = (turn + 1) % m2
        isAm = turn < m
        ncnt = cnt + 1
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not isRange(nr, nc, n):  # 범위 밖
                continue
            if check[nr][nc][nturn] != -1:
                continue
            if arr[nr][nc] == 1:
                if isAm: continue
                while arr[nr][nc] == 1:
                    nr, nc = nr + dr[d], nc + dc[d]
                    if not isRange(nr, nc, n):
                        nr = -1
                        break
                if nr == -1 or check[nr][nc][nturn] != -1: continue
            if nr == n-1 and nc == n-1:
                return ncnt
            check[nr][nc][nturn] = ncnt
            que.append((nr, nc, ncnt))
    return -1


n,m = map(int,input().split())
m2 = 2*m
arr = [list(map(int,input().split())) for _ in range(n)]
ans = solution(n,m,arr)
if ans == -1:
    print(ans)
else:
    day = ans//m2 + 1
    isAm = ans%m2 < m
    if isAm:
        print(day,'sun')
    else:
        print(day,'moon')