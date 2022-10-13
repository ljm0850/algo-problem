import sys
input = sys.stdin.readline

def solve(graph:list)->int:
    friend = set()
    first_friend = graph[1]
    for s in first_friend:
        friend.add(s)
    while first_friend:
        now = first_friend.pop()
        for next in graph[now]:
            if not next in friend and next != 1:
                friend.add(next)
    return len(friend)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = solve(graph)
print(ans)