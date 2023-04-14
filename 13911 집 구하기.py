import heapq,sys
input = sys.stdin.readline
def solution(start:int)->list[int]:
    shortcut = [maxValue]*(V+3)
    h = [(0,start)]
    while h:
        length,nowNode = heapq.heappop(h)
        if shortcut[nowNode] < length:
            continue
        for nextNode in road[nowNode]:
            nextLength = roadLength[nowNode][nextNode] + length
            if nextLength < shortcut[nextNode]:
                shortcut[nextNode] = nextLength
                heapq.heappush(h,(nextLength,nextNode))
    return shortcut

V,E = map(int,input().split())
road = [set() for _ in range(V+3)]
roadLength = [{} for _ in range(V+3)]
maxValue = 2000000001
for _ in range(E):
    u,v,w = map(int,input().split())
    road[u].add(v)
    road[v].add(u)
    length = min(roadLength[u].get(v,maxValue),w)
    roadLength[u][v] = length
    roadLength[v][u] = length

M,x = map(int,input().split())
mcdonalds = set(map(int,input().split()))
for mcdonald in mcdonalds:
    road[V+1].add(mcdonald)
    roadLength[V+1][mcdonald] = 0

S,y = map(int,input().split())
starbucks = set(map(int,input().split()))
for starbuck in starbucks:
    road[V+2].add(starbuck)
    roadLength[V+2][starbuck] = 0

mcdonaldsShortcut = solution(V+1)
starbucksShortcut = solution(V+2)

ans = maxValue
for node in range(1,V+1):
    if node in starbucks or node in mcdonalds:
        continue
    if mcdonaldsShortcut[node] <= x and starbucksShortcut[node] <= y:
        ans = min(ans,mcdonaldsShortcut[node] + starbucksShortcut[node])
if ans != maxValue:
    print(ans)
else:
    print(-1)