from collections import deque

def solve(N:int,S:int,D:int)->int:
    global police,move
    que = deque()
    que.append(S)
    ans = 0
    check = [False]*(N+1)
    while que:
        ans += 1
        for _ in range(len(que)):
            now = que.popleft()
            for moving in move:
                nextPosition = now + moving
                if nextPosition == D:
                    return ans
                elif 0 < nextPosition <= N and not check[nextPosition] and not nextPosition in police:
                    check[nextPosition] = True
                    que.append(nextPosition)
    return -1

N,S,D,F,B,K = map(int,input().split())
move = (F,-B)
if K:police = set(map(int,input().split()))
else: police = set()
ans = solve(N,S,D)
if ans == -1:
    print('BUG FOUND')
else:
    print(ans)