# import sys
# input = sys.stdin.readline
#
# N,T = map(int,input().split())
# city = [[] for _ in range(N)]
# specialCity = [0]*(N)
# for idx in range(N):
#     s,x,y = map(int,input().split())
#     city[idx] = (x,y)
#     specialCity[idx] = s
#
# impossble = 10000
# graph = [[impossble]*(N) for _ in range(N)]
# for idx in range(N):
#     graph[idx][idx] = 0
#
# for s in range(N):
#     r1,c1 = city[s]
#     for e in range(s+1,N):
#         r2,c2 = city[e]
#         length = abs(r1-r2) + abs(c1-c2)
#         if specialCity[s] and specialCity[e]:
#             length = min(T,length)
#         graph[s][e] = length
#         graph[e][s] = length
#
# for m in range(N):
#     for s in range(N):
#         for e in range(N):
#             if graph[s][e] > graph[s][m] + graph[m][e]:
#                 graph[s][e] = graph[s][m] + graph[m][e]
#
# M = int(input())
# for _ in range(M):
#     a,b = map(int,input().split())
#     print(graph[a-1][b-1])
import sys
input = sys.stdin.readline
def length(c1:tuple,c2:tuple)->int:
    return abs(c1[0] - c2[0]) + abs(c1[1]-c2[1])

N,T = map(int,input().split())
city = []
specialCity = set()
for idx in range(N):
    s,x,y = map(int,input().split())
    city.append((x,y))
    if s:
        specialCity.add(idx)
INF = 10000

graph = [[INF]*(N) for _ in range(N)]
for idx in range(N):
    graph[idx][idx] = 0
for s in range(N):
    for e in range(s+1,N):
        l = length(city[s],city[e])
        graph[s][e] = l
        graph[e][s] = l

short_cut = [0]*(N)
for c in range(N):
    if c in specialCity:
        continue
    minValue = 10000
    for node in specialCity:
        minValue = min(minValue,graph[c][node])
    short_cut[c] = minValue

for s in range(N):
    for e in range(s+1,N):
        graph[s][e] = min(graph[s][e],short_cut[s]+short_cut[e]+T)
        graph[e][s] = graph[s][e]

M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    print(graph[a-1][b-1])