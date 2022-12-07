from collections import deque
def solve(R:int,C:int)->int:
    value = 0
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 'L':
                value = max(value,find(r,c))
    return value
def find(r:int,c:int)->int:
    check = [[False] * C for _ in range(R)]
    check[r][c] = True
    que = deque()
    que.append((r,c))
    cnt = -1
    while que:
        cnt += 1
        for _ in range(len(que)):
            r,c = que.popleft()
            for way in range(4):
                nr,nc = r+dr[way],c+dc[way]
                if 0<=nr<R and 0<=nc<C and not check[nr][nc] and arr[nr][nc] == 'L':
                    check[nr][nc] = True
                    que.append((nr,nc))
    return cnt

dr,dc = (1,-1,0,0),(0,0,1,-1)
R,C = map(int,input().split())
arr = [input() for _ in range(R)]
ans = solve(R,C)
print(ans)