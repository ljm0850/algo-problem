# 다익스트라 풀이
import heapq,sys
input = sys.stdin.readline
def dijkstra(node:int,N:int,end:int)->int:
    INF = 1000000001
    h = [(-INF,node)]
    ls = [0]*(N+1)
    ls[node] = INF
    while h:
        weight,now = heapq.heappop(h)
        weight = - weight
        if ls[now] and weight < ls[now]:
            continue
        for next_node,next_weight in graph[now]:
            new_weight = min(weight,next_weight)
            if ls[next_node] < new_weight:
                ls[next_node] = new_weight
                heapq.heappush(h,(-new_weight,next_node))
    return ls[end]

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))
start,end = map(int,input().split())
ans = dijkstra(start,N,end)
print(ans)

# union
import sys
input = sys.stdin.readline
def union_AB(a:int,b:int):
    A = find_root(a)
    B = find_root(b)
    if deepth[A] > deepth[B]:
        ls[B] = A
    elif deepth[A] < deepth[B]:
        ls[A] = B
    else:
        ls[B] = A
        deepth[A] += 1

def find_root(node:int)->int:
    if ls[node] == node:
        return node
    ls[node] = find_root(ls[node])
    return ls[node]

N,M = map(int,input().split())
graph = []
ls = [num for num in range(N+1)]
deepth = [0]*(N+1)
for _ in range(M):
    A,B,C = map(int,input().split())
    graph.append((C,A,B))
start,end = map(int,input().split())
graph.sort()
while graph:
    weight,a,b = graph.pop()
    union_AB(a,b)
    if find_root(start) == find_root(end):
        print(weight)
        break
