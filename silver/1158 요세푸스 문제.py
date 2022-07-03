from collections import deque
N,K = map(int,input().split())
total = deque([str(i) for i in range(1,N+1)])
ans = deque()

while total:
    total.rotate(-K+1)
    ans.append(total.popleft())
print('<',end='')
for i in range(N):
    print(ans.popleft(),end='')
    if ans:
        print(',',end=' ')
print('>')