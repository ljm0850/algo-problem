import sys
def bfs():
    global arr
    cnt = 0
    que = []
    for h in range(H):
        for c in range(N):
            for r in range(M):
                if arr[h][c][r] == 1:
                    que.append([h,c,r])
    temp = []
    if check(arr):
        return 0

    while que:
        h,c,r = que.pop()
        for way in range(6):
            nh = h + dh[way]
            nr = r + dr[way]
            nc = c + dc[way]
            if 0 <= nh < H and 0 <= nr < M and 0 <= nc < N and arr[nh][nc][nr] == 0:
                temp.append([nh, nc, nr])
                arr[nh][nc][nr] = 1
        if not que :
            if temp:
                cnt +=1
                for _ in temp:
                    que.append(_)
            temp.clear()
    if check(arr):
        return cnt
    return -1


def check(arr):
    for h in range(H):
        for c in range(N):
            for r in range(M):
                if arr[h][c][r] == 0:           # 덜 익은게 있다다
                   return 0
    return 1                                    # 완숙


dr=[1,-1,0,0,0,0]
dc=[0,0,1,-1,0,0]
dh=[0,0,0,0,1,-1]
M,N,H = map(int,sys.stdin.readline().split())        # 가로 세로 높이

arr = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for __ in range(H)]
print(bfs())