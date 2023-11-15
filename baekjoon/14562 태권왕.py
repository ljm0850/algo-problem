from collections import deque
def solution(S:int,T:int)->int:
    que = deque()
    que.append((S,T))
    visit = set()
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):
            value,end = que.popleft()
            v1,v2 = value+1,2*value
            if v1 == end or v2 == end+3:
                return cnt
            if v1 < end and not (v1,end) in visit:
                visit.add((v1,end))
                que.append((v1,end))
            if v2 < end+3 and not (v2,end+3) in visit:
                visit.add((v2,end+3))
                que.append((v2,end+3))
    return 0
C = int(input())
for tc in range(C):
    S,T = map(int,input().split())
    ans = solution(S,T)
    print(ans)