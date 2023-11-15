import sys
def union(a,b):
    A = find_root(a)
    B = find_root(b)
    if depth[A] > depth[B]:
        group[B] = A
    elif depth[A] < depth[B]:
        group[A] = B
    else:
        group[A] = B
        depth[B] += 1

def find_root(n):
    if group[n] == n:
        return n
    group[n] = find_root(group[n])
    return group[n]


n,m = map(int,sys.stdin.readline().split())
group = [num for num in range(n+1)]
depth = [1]*(n+1)
for _ in range(m):
    F,a,b = map(int,sys.stdin.readline().split())
    if F == 0:
        union(a,b)
    else:
        if find_root(a) == find_root(b):
            print("YES")
        else:
            print("NO")