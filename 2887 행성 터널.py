import sys
input = sys.stdin.readline

def union(a:int,b:int)->None:
    A = find_root(a)
    B = find_root(b)

    if depth[A] > depth[B]:
        group[B] = A
    elif depth[A] < depth[B]:
        group[A] = B
    else:
        group[B] = A
        depth[A] += 1

def find_root(n:int)->int:
    T = group[n]
    if T == n:
        return n
    group[n] = find_root(T)
    return group[n]

def find_min_length(ls:list[int,int,int])->int:
    a,b,c = ls[0][0],ls[1][0],ls[2][0]
    if a <= b and a <= c:
        return 0
    elif b <= a and b <= c:
        return 1
    else:
        return 2

def gap_ls(ls:list[int])->list[int]:
    ls.sort()
    l = len(ls)
    value = []
    for i in range(l-1):
        value.append((ls[i+1][0] - ls[i][0],ls[i+1][1],ls[i][1]))
    value.sort()
    return value

def solution(N:int,x_point:list[int],y_point:list[int],z_point:list[int])->int:
    if N == 1:
        return 0
    n = N - 1
    value = 0
    x_gap = gap_ls(x_point)
    y_gap = gap_ls(y_point)
    z_gap = gap_ls(z_point)

    xyz = [x_gap,y_gap,z_gap]
    index = [0,0,0]
    ls = [xyz[i][0] for i in range(3)]

    while True:
        T = find_min_length(ls)
        union(ls[T][1],ls[T][2])
        value += ls[T][0]

        for i in range(3):
            while True:
                a,b = xyz[i][index[i]][1],xyz[i][index[i]][2]
                if find_root(a) == find_root(b):
                    index[i] += 1
                    if index[i] == n:
                        return value
                else:
                    break
            ls[i] = xyz[i][index[i]]

N = int(input())
x_point,y_point,z_point = list(),list(),list()
for i in range(N):
    x,y,z = map(int,input().split())
    x_point.append((x,i))
    y_point.append((y,i))
    z_point.append((z,i))
group = [num for num in range(N)]
depth = [0]*(N)
ans = solution(N,x_point,y_point,z_point)
print(ans)