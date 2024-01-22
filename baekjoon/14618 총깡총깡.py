import sys
from heapq import heappush,heappop
input = sys.stdin.readline

def dijkstra(N:int,J:int,INF:int,graph:list[dict]):
    que = [(J,0)]    # (node,length)
    max_length = INF
    record = [max_length]*(N+1)
    while que:
        now_node,now_length = heappop(que)
        if record[now_node] < now_length:
            continue
        for next_node in graph[now_node]:
            add_length = graph[now_node][next_node]
            next_length = now_length + add_length
            if record[next_node] > next_length:
                heappush(que,(next_node,next_length))
                record[next_node] = next_length
    return record

N,M = map(int,input().split())
J = int(input())
K = int(input())
house_A = set(map(int,input().split()))
house_B = set(map(int,input().split()))
graph = [dict() for _ in range(N+1)]
for _ in range(M):
    X,Y,Z = map(int,input().split())
    graph[X][Y] = min(graph[X].get(Y,101),Z)
    graph[Y][X] = graph[X][Y]
INF = 100*(N+1)
short_cut = dijkstra(N,J,INF,graph)
ans_node,shorted_length = 0,INF
for node in range(1,N+1):
    if (not node in house_A) and (not node in house_B) or short_cut[node] == INF:
        continue
    if short_cut[node] < shorted_length:
        shorted_length = short_cut[node]
        ans_node = node
    elif short_cut[node] == shorted_length and node in house_A:
        ans_node = node
if K == 0:
    print(-1)
elif ans_node in house_A:
    print('A')
    print(shorted_length)
elif ans_node in house_B:
    print('B')
    print(shorted_length)
else:
    print(-1)