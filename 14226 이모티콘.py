from collections import deque
def solution(N:int)->int:
    que = deque()
    que.append((1,0,0))
    M = 2001
    check = [[False]*(M) for _ in range(M)]
    while que:
        length,clipboard,cnt = que.popleft()
        if length == N:
            return cnt
        if check[length][clipboard]:
            continue
        check[length][clipboard] = True
        ncnt = cnt + 1
        que.append((length,length,ncnt))
        if clipboard and length+clipboard < M:
            que.append((length+clipboard,clipboard,ncnt))
        if length > 1:
            que.append((length-1,clipboard,ncnt))

S = int(input())
ans = solution(S)
print(ans)