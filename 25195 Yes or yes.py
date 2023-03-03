import sys
input = sys.stdin.readline
def solution(graph:list[list[int]],fanclub:set[int])->str:
    if 1 in fanclub:
        return 'Yes'

    ls = [1]
    while ls:
        now = ls.pop()
        if graph[now]:
            for nextPoint in graph[now]:
                if not nextPoint in fanclub:
                    ls.append(nextPoint)
        else:
            return 'yes'
    return 'Yes'

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
S = int(input())
fanclub = set(map(int,input().split()))
ans = solution(graph,fanclub)
print(ans)