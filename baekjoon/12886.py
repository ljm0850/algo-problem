from collections import deque

def solution(A:int,B:int,C:int)->int:
    if A == B == C:
        return 1
    if (A+B+C)%3:
        return 0
    check = set()
    que = deque([tuple(sorted((A,B,C)))])
    while que:
        x,y,z = que.popleft()
        if x == y == z:
            return 1
        
        total = [
            (x+x,y-x,z),
            (x+x,y,z-x),
            (x,y+y,z-y)
        ]
        for value in total:
            if value[1]>0 and value[2]>0:
                sortedValue = tuple(sorted(value))
                if not sortedValue in check:
                    check.add(sortedValue)
                    que.append(sortedValue)
    return 0

A,B,C = map(int,input().split())
ans = solution(A,B,C)
print(ans)