from collections import deque
N,K = map(int,input().split())
visted = [0]*200001

que = deque()
que.append(N)
visted[N] = 1
cnt = 0
while que:
    for _ in range(len(que)):
        t = que.popleft()
        if t == K:
            print(cnt)
            exit()

        for nt in (t+1,t-1,2*t):
            if 0<=nt<200000 and not visted[nt]:
                visted[nt] = 1
                que.append(nt)
    cnt += 1