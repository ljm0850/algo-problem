import sys
sys.stdin = open('input.txt')
def check(i,j):
    global tree
    di=[0,1,0,-1]
    dj=[1,0,-1,0]
    for way in range(4):
        temp_i = i+di[way]
        temp_j = j+dj[way]
        if (0<=temp_i<N) and (0<=temp_j<N):
            if arr[i][j] +1 == arr[temp_i][temp_j]:
                tree[i][j].append((temp_i,temp_j))

# N*N 형태의 방
T = int(input())

for tc in range(1,T+1):
    N = int(input())          #1000 이하
    arr = [list(map(int,input().split())) for _ in range(N)]
    tree = [[[] for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            check(i,j)
    max_cnt = 0
    sol_num = N**2
    for i in range(N):
        for j in range(N):
            cnt = 0
            que=[[i,j]]
            while que:
                temp = que.pop(0)
                ii,jj = temp[0],temp[1]
                cnt += 1
                if tree[ii][jj]:
                    for s in tree[ii][jj]:
                        que.append([s[0],s[1]])
                
            if max_cnt < cnt:
                max_cnt = cnt
                sol_num = arr[i][j]
            elif max_cnt == cnt:
                if sol_num > arr[i][j]:
                    sol_num = arr[i][j]
    print(f'#{tc} {sol_num} {max_cnt}')