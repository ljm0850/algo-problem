def find_root(node:int)->int:
    if group[node] == node:
        return node
    group[node] = find_root(group[node])
    return group[node]

def unionA_B(A:int,B:int)->None:
    a = find_root(A)
    b = find_root(B)
    if a == b:
        return
    if depth[a] > depth[b]:
        group[b] = a
    elif depth[a] < depth[b]:
        group[a] = b
    else:
        group[b] = a
        depth[a] += 1

def check(arr:list[int])->bool:
    v = find_root(arr[0])
    for i in arr:
        if v != find_root(i):
            return False
    return True

N = int(input())
M = int(input())
group = [num for num in range(N+1)]
depth = [0]*(N+1)
for i in range(1,N+1):
    value = list(map(int,input().split()))
    for j in range(i,N):
        if value[j]:
            unionA_B(i,j+1)
total = list(map(int,input().split()))
ans = check(total)
if ans:
    print('YES')
else:
    print('NO')