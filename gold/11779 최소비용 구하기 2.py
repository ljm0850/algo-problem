import heapq,sys
input = sys.stdin.readline
def djikstra(start:int,end:int)->list((int,list())):
    maximum = 100000*1000
    short_cut = [(maximum,[start]) for _ in range(n+1)]
    short_cut[start] = (0,[])
    h = [(start,0,[start])]
    while h:
        now,pay,path = heapq.heappop(h)
        if short_cut[now][0] < pay:
            continue
        for next,paid in bus[now]:
            next_pay = paid + pay
            if short_cut[next][0] > next_pay:
                h.append((next,next_pay,path+[next]))
                short_cut[next] = (next_pay,path+[next])
    return short_cut[end]

n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수
bus = [[] for _ in range(n+1)]
for _ in range(m):
    A,B,pay = map(int,input().split())
    bus[A].append((B,pay))
start,end = map(int,input().split())
ans = djikstra(start,end)

print(ans[0])
print(len(ans[1]))
print(*ans[1])