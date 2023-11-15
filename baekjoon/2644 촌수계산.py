from collections import deque
def check(t1,t2):
    visited = [0]*(n+1)
    visited[t1] = 1
    que = deque()
    que.append(t1)
    cnt = 0
    while que:
        cnt +=1
        for _ in range(len(que)):
            t = que.popleft()
            for nt in connect[t]:
                if nt == t2:
                    return cnt
                if not visited[nt]:
                    que.append(nt)
                    visited[nt] = 1
    return -1

n = int(input())                #사람의 수
t1,t2 = map(int,input().split())        # 계산해야할 인물번호
m = int(input())                #관계의 개수
connect = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    connect[x].append(y)
    connect[y].append(x)
print(check(t1,t2))