from collections import deque
import sys
input = sys.stdin.readline
def solution(l,sr,sc,gr,gc):
    dr, dc = (-2, -2, -1, -1, 1, 1, 2, 2), (1, -1, 2, -2, 2, -2, 1, -1)
    if sr == gr and sc == gc:
        return 0
    check = [[0]*l for _ in range(l)]
    check[sr][sc] = 1
    que = deque()
    que.append((sr,sc))
    while que:
        r,c = que.popleft()
        for d in range(8):
            nr,nc = r + dr[d], c + dc[d]
            if not (0<=nr<l and 0<=nc<l and check[nr][nc]==0):
                continue
            if nr == gr and nc == gc:
                return check[r][c]
            check[nr][nc] = check[r][c] + 1
            que.append((nr,nc))
    return -1

T = int(input())
for _ in range(T):
    l = int(input())
    sr,sc = map(int,input().split())
    gr,gc = map(int,input().split())
    ans = solution(l,sr,sc,gr,gc)
    print(ans)