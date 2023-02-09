from collections import deque
def solution(F:int,S:int,G:int,U:int,D:int)->int:
    if S == G:
        return 0
    que = deque([S])
    check = [False]*(F+1)
    check[S] = True
    dh = (U,-D)
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):
            h = que.popleft()
            for move in dh:
                nh = h + move
                if nh == G:
                    return cnt
                if 0<nh<=F and not check[nh]:
                    check[nh] = True
                    que.append(nh)
    return -1

F,S,G,U,D = map(int,input().split())
ans = solution(F,S,G,U,D)
if ans == -1:print("use the stairs")
else:print(ans)