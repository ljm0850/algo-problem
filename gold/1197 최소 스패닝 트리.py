import sys
def solve(arr:list)->int:
    total = 0
    for node in arr:
        if find_root(node[0]) != find_root(node[1]):
            union(node[0],node[1])
            total += node[2]
    return total

def union(a:int,b:int)->None:
    A = find_root(a)
    B = find_root(b)
    if depth[A] > depth[B]:
        group[B] = A
    elif depth[A] < depth[B]:
        group[A] = B
    else:
        group[A] = B
        depth[B] += 1

def find_root(n:int)->int:
    if group[n] == n:
        return n
    group[n] = find_root(group[n])
    return group[n]

V,E = map(int,sys.stdin.readline().split())
group = [num for num in range(V+1)]
depth = [1]*(V+1)
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(E)]
graph.sort(key=lambda x:x[2])
ans = solve(graph)
print(ans)