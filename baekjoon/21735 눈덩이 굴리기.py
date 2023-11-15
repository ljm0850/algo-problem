from collections import deque

def solve(N:int,time:int,snow:list[int])->int:
    que = deque()
    que.append((1,0,1))
    check = [0]*(N+1)
    while que:
        size,nowPosition,nowTime = que.popleft()
        if nowTime > time:
            break
        for step in range(1,3):
            nextPosition = nowPosition + step
            if step == 2:
                size //= 2
            if nextPosition <= N:
                nextSize = size + snow[nextPosition]
                if nextSize > check[nextPosition]:
                    check[nextPosition] = nextSize
                    que.append((nextSize,nextPosition,nowTime+1))
    return max(check)

N,M = map(int,input().split())
snow = [0]+list(map(int,input().split()))
ans = solve(N,M,snow)
print(ans)
