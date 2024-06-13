import sys
from collections import deque
input = sys.stdin.readline

def solution():
    C,R = map(int,input().split())
    N = int(input())
    arr = [[0]*C for _ in range(R)]
    que = deque()
    lamp = list()
    dr,dc = (1,-1,0,0),(0,0,1,-1)
    for _ in range(N):
        objectType,c,r = input().split()
        c,r = int(c),int(r)
        match objectType:
            case "redstone_block":
                arr[r][c] = 15
                que.append((r,c))
            case "redstone_dust":
                arr[r][c] = -1
            case "redstone_lamp":
                lamp.append((r,c))
                arr[r][c] = -2
    while que:
        r,c = que.popleft()
        nextPower = arr[r][c] -1
        if nextPower == -1:
            break
        for d in range(4):
            nr,nc = r+dr[d],c+dc[d]
            if not (0<=nr<R and 0<=nc<C):
                continue
            match arr[nr][nc]:
                case -1:
                    arr[nr][nc] = nextPower
                    que.append((nr,nc))
                case -2:
                    arr[nr][nc] = 0
    for r,c in lamp:
        if arr[r][c] != 0:
            return "failed"
    return "success"

ans = solution()        
print(ans)