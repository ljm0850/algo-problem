import sys
input = sys.stdin.readline
def findPath(midArr:list[list[int]],graph,INF):
    record = [[[] for _ in range(n+1)] for __ in range(n+1)]

    for s in range(1,n+1):
        for e in range(1,n+1):
            if graph[s][e] == 0:
                continue
            record[s][e] = recur(midArr,s,e,record)
    return record

def recur(midArr,s,e,record):
    if record[s][e]:
        return record[s][e]
    if midArr[s][e] == 0:
        return list()
    m = midArr[s][e]
    record[s][e] = recur(midArr,s,m,record) + [m] + recur(midArr,m,e,record)
    return record[s][e]


n = int(input())
m = int(input())
INF = 100000 * n
graph = [[INF]*(n+1) for _ in range(n+1)]
midCheck = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)

for m in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if graph[s][e] > graph[s][m] + graph[m][e]:
                graph[s][e] = graph[s][m] + graph[m][e]
                midCheck[s][e] = m

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1,n+1):
    print(*graph[i][1:])

arr = findPath(midCheck,graph,INF)

for s in range(1,n+1):
    for e in range(1,n+1):
        if graph[s][e] == 0 or graph[s][e] == INF:
            print(0)
        else:
            value = [len(arr[s][e])+2]+[s]+arr[s][e]+[e]
            print(*value)
