import sys
input = sys.stdin.readline
def kruskal_ls(well_cost:list[int],graph:list[list[int]])->list[tuple[int]]:
    ls = list()
    for i in range(N):
        for j in range(i + 1, N):
            ls.append((graph[i][j], i, j))
        ls.append((well_cost[i], i, N))
    ls.sort()
    return ls
def union(a:int,b:int)->None:
    A = find_root(a)
    B = find_root(b)
    group[A] = B

def find_root(num:int)->int:
    if group[num] == num:
        return num
    group[num] = find_root(group[num])
    return group[num]

maxValue = 100001
N = int(input())
well_cost = [int(input()) for _ in range(N)]
graph = [tuple(map(int,input().split())) for _ in range(N)]
group = [i for i in range(N+1)]
ls = kruskal_ls(well_cost,graph)
ans = 0
for cost,a,b in ls:
    if find_root(a) != find_root(b):
        union(a,b)
        ans += cost
print(ans)
