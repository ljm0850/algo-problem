from collections import deque
import sys
input = sys.stdin.readline
dr,dc = (-1,-1,0,1,1,1,0,-1),(0,1,1,1,0,-1,-1,-1)
N,M,K = map(int,input().split())
fireBalls = deque()
for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    fireBalls.append((r-1,c-1,m,s,d))

arr = [[[] for _ in range(N)] for __ in range(N)]
for cnt in range(K):
    # 파이어볼 이동
    for i in range(len(fireBalls)):
        r,c,m,s,d = fireBalls.popleft()
        nr,nc = (r+s*dr[d])%N, (c+s*dc[d])%N
        arr[nr][nc].append((m,s,d))

    # 파이어볼 병합
    for r in range(N):
        for c in range(N):
            if len(arr[r][c]) > 1:
                mass,speed,direction = 0,0,0
                for m,s,d in arr[r][c]:
                    mass += m
                    speed += s
                    direction |= (d%2)+1
                mass //= 5
                speed //= len(arr[r][c])
                arr[r][c].clear()
                if mass != 0:
                    start = 1 if direction == 3 else 0
                    for d in range(start,8,2):
                        arr[r][c].append((mass,speed,d))
            for m,s,d in arr[r][c]:
                fireBalls.append((r,c,m,s,d))
            arr[r][c].clear()
ans = 0
for fireBall in fireBalls:
    mass = fireBall[2]
    ans += mass
print(ans)