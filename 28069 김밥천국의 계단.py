from collections import deque
def solution(N:int,K:int):
    que = deque()
    que.append(0)
    check = set()
    cnt = 0
    while que:
        if cnt == K:
            return False
        for _ in range(len(que)):
            step = que.popleft()
            for next_step in (step+1,step+step//2):
                if next_step <= N and not next_step in check:
                    if next_step == N:
                        return True
                    check.add(next_step)
                    que.append(next_step)
        cnt += 1

N,K = map(int,input().split())
ans = solution(N,K)
if ans:
    print('minigimbob')
else:
    print('water')