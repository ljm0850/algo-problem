from collections import deque

def inrange(R,C,r,c)->bool:
    if 0<=c<C and 0<=r<R:
        return True
    return False

def solution(R:int,C:int,arr:list[str],coins:deque)->int:
    dr,dc = (1,-1,0,0),(0,0,1,-1)
    value = 0
    check = set()

    while coins:
        value += 1
        for _ in range(len(coins)//2):
            r1,c1 = coins.popleft()
            r2,c2 = coins.popleft()
            for d in range(4):
                cnt = 0
                nr1,nc1 = r1 + dr[d], c1 + dc[d]
                nr2,nc2 = r2 + dr[d], c2 + dc[d]
                if inrange(R,C,nr1,nc1):
                    if arr[nr1][nc1] == '#':
                        nr1,nc1 = r1,c1
                else:
                    cnt += 1
                if inrange(R,C,nr2,nc2):
                    if arr[nr2][nc2] == '#':
                        nr2,nc2 = r2,c2
                else:
                    cnt += 1
                if cnt == 1:
                    return value
                elif cnt == 0:
                    if (nr1,nc1,nr2,nc2) in check:
                        continue
                    check.add((nr1,nc1,nr2,nc2))
                    coins.append((nr1,nc1))
                    coins.append((nr2,nc2))

    return -1

R,C = map(int,input().split())
arr = []
coins = deque()
for r in range(R):
    temp = input()
    for c in range(C):
        if temp[c] == 'o':
            coins.append((r,c))
    arr.append(temp)

ans = solution(R,C,arr,coins)
print(ans)