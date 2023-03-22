import sys,heapq
input = sys.stdin.readline
def solution(n:int,start:int,graph:list[list])->tuple:
    check = [False]*(n+1)
    cnt = 0
    value = 0
    h = [(0,start)]
    while h:
        time,nowNode = heapq.heappop(h)
        if check[nowNode]:
            continue
        check[nowNode] = True
        cnt += 1
        value = time
        for nextNode,addtime in graph[nowNode]:
            if not check[nextNode]:
                heapq.heappush(h,(time+addtime,nextNode))
    return (cnt,value)

T = int(input())
for tc in range(T):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))
    ans = solution(n,c,graph)
    print(*ans)