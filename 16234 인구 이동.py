def makeGroup(N):
    group = []
    for i in range(N):
        temp = [num+i*N for num in range(N)]
        group.append(temp)
    return group

def uionAB(A,B):
    a = findRoot(A)
    b = findRoot(B)
    group[b] = a

def findRoot(node):
    if group[node] == node:
        return node
    group[node] = findRoot(group[node])
    return group[node]

N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
T = N*N
cnt = 0

dr,dc = (1,0),(0,1)

while True:
    flag = False
    n = 0
    group = [num for num in range(T)]
    for r in range(N):
        for c in range(N):
            for d in range(2):
                nr,nc = r+dr[d],c+dc[d]
                if nr<N and nc<N and L <= abs(arr[r][c]-arr[nr][nc]) <= R:
                    uionAB(n,nr*N+nc)
            n += 1
    check = {}
    for i in range(T):
        I = findRoot(i)
        check[I] = check.get(I,[]) + [(i//N,i%N)]

    for ls in check.values():
        if len(ls) == 1:
            continue
        temp = arr[ls[0][0]][ls[0][1]]
        for r,c in ls:
            if temp != arr[r][c]:
                break
        else:
            continue
        flag = True
        total = 0
        for r,c in ls:
            total += arr[r][c]
        total //= len(ls)
        for r,c in ls:
            arr[r][c] = total
    if flag:
        cnt += 1
    else:
        break
print(cnt)