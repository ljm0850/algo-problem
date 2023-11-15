import sys
input = sys.stdin.readline
def make_graph(n,k):
    graph = [[] for _ in range(n+1)]
    check = [0]*(n+1)
    for _ in range(k):
        X,Y = map(int,input().split())
        graph[X].append(Y)
        check[Y] += 1
    return graph,check

def find_start(check,n):
    starts = []
    for i in range(1,n+1):
        if not check[i]:
            starts.append(i)
    return starts

def solve(starts,check):
    dp = [0] * (N + 1)
    stack = []
    for start in starts:
        dp[start] = building_time[start]
        stack.append((start,building_time[start]))

    while stack:
        now,now_time = stack.pop()
        nexts = graph[now]
        for next in nexts:
            check[next] -= 1
            dp[next] = max(dp[next],dp[now]+building_time[next])
            if check[next] == 0:
                stack.append((next,dp[now]+building_time[next]))
    return dp

T = int(input())
for tc in range(T):
    N,K = map(int,input().split())
    building_time = [0]+list(map(int,input().split()))
    graph,check = make_graph(N,K)
    W = int(input())
    starts = find_start(check,N)
    ans=solve(starts,check)
    print(ans[W])