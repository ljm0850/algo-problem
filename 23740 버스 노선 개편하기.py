import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
graph.sort()
S,E,C = graph[0]
ans = []
for s,e,c in graph:
    if s <= E:
        C = min(C,c)
        E = max(E,e)
    else:
        ans.append((S,E,C))
        S,E,C = s,e,c
if not ans or (ans[-1] != (S,E,C)):
    ans.append((S,E,C))
print(len(ans))
for value in ans:
    print(*value)