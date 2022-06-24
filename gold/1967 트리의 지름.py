# 나중에 알아 본 결과 한개의 점에서 가장 먼 점(p1), p1에서 가장 먼 점(p2)이 루트(p1-p2)가 된다..
# 밑 코드는 pypy에서만 통과

import sys
def solve(s):
    visited = [0]*(n+1)
    visited[s] = 1
    stack = [(s,0,0,[s])]
    while stack:
        now,length,way,path = stack.pop()
        for next in tree[now].keys():
            if not visited[next]:
                next_length = length + tree[now][next]
                visited[next] = 1
            else:
                continue

            if dp[now][next]:
                best = length + dp[now][next]
                path.append(next)
                for i in range(len(path) - 1):
                    dp[path[i]][path[i + 1]] = max(dp[path[i]][path[i + 1]], best)
                    best -= tree[path[i]][path[i + 1]]
                path.pop()
                continue

            if now == s:
                way = next
                best = 0
                for t in dp[way].items():
                    if t[0] != now and best < t[1]:
                        best = t[1]
                if best:
                    dp[s][way] = next_length + best
                    continue

            stack.append((next,next_length,way,path+[next]))

        for i in range(len(path)-1):
            dp[path[i]][path[i+1]] = max(dp[path[i]][path[i+1]], length)
            length -= tree[path[i]][path[i+1]]

n = int(input())
tree = [{} for _ in range(n+1)]
dp = [{} for _ in range(n+1)]
find_root = [0]*(n+1)
find_root[0] = 1
for _ in range(n-1):
    p,c,v = map(int,sys.stdin.readline().split())
    find_root[c] = 1
    tree[p][c] = v
    tree[c][p] = v
    dp[p][c] = 0
    dp[c][p] = 0
for i in range(1,n+1):
    if find_root[i] == 0:
        root = i
        break
solve(root)
ans = 0
for i in range(1,n+1):
    for j in dp[i].keys():
        if dp[i][j] == 0:
            temp = 0
            for k in dp[j].keys():
                if k != i:
                    temp = max(temp,dp[j][k])
            dp[i][j] = temp + tree[i][j]
    best1,best2 = 0,0
    for t in dp[i].values():
        if t >= best1:
            best2 = best1
            best1 = t
    ans = max(ans,best1+best2)
print(ans)