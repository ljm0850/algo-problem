import sys
input = sys.stdin.readline

def union(a:int,b:int)->None:
    global dangerous_city
    A = find_root(a)
    B = find_root(b)
    if A == B:
        return
    if depth[A] > depth[B]:
        group[B] = A
        main,sub = A,B
    elif depth[A] < depth[B]:
        group[A] = B
        main,sub = B,A
    else:
        group[B] = A
        depth[A] += 1
        main,sub = A,B
    total_gap = gap[main] + gap[sub]
    if total_gap >= 0:
        if gap[main] < 0:
            dangerous_city -= group_size[main]
        elif gap[sub] < 0 :
            dangerous_city -= group_size[sub]
    else:
        if gap[main] >= 0:
            dangerous_city += group_size[main]
        elif gap[sub] >= 0:
            dangerous_city += group_size[sub]
    group_size[main] += group_size[sub]
    gap[main] = total_gap

def find_root(num:int)->int:
    if group[num] == num:
        return group[num]
    group[num] = find_root(group[num])
    return group[num]

N,M = map(int,input().split())
capacity = [0] + list(map(int,input().split()))
data = [0] + list(map(int,input().split()))
gap = [0]*(N+1)
dangerous_city = 0
for i in range(1,N+1):
    gap[i] = capacity[i] - data[i]
    if gap[i] < 0:
        dangerous_city += 1

group = [i for i in range(N+1)]
group_size = [1]*(N+1)
depth = [0]*(N+1)
for _ in range(M):
    query,*city = map(int,input().split())
    if query == 1:
        union(city[0],city[1])
    else:
        print(dangerous_city)