import sys
def union(a:int,b:int)->list:
    A = find_root(a)
    B = find_root(b)
    if depth[A] > depth[B]:
        group[B] = A
    elif depth[A] < depth[B]:
        group[A] = B
    else:
        group[A] = B
        depth[B] += 1

def find_root(num:int)->int:
    if group[num] == num:
        return num
    group[num] = find_root(group[num])
    return group[num]

N,M = map(int,sys.stdin.readline().split())
group = [i for i in range(N+1)]
depth = [1]*(N+1)
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
graph.sort(key=lambda x:x[2])
answer = 0
max_cost = 0
for way in graph:
    a,b,c = way
    if find_root(a) != find_root(b):
        union(a,b)
        answer += c
        max_cost = max(max_cost,c)
print(answer-max_cost)