import sys

N,M = map(int,sys.stdin.readline().split())
nodes = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]

connect = [[] for _ in range(N+1)]
check = [0]*(N+1)
ans = 0
for node in nodes:
    connect[node[0]].append(node[1])
    connect[node[1]].append(node[0])

for i in range(1,N+1):
    if not check[i]:
        stack = [i]
        ans += 1
        while stack:
            t = stack.pop()
            check[t] = 1
            for j in connect[t]:
                if not check[j] and not j in stack:
                    stack.append(j)
print(ans)