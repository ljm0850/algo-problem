from collections import deque
def check():
    global ans
    for i in range(h):
        for j in range(w):
            if arr[i][j] :
                arr[i][j] = 0
                ans +=1
                que = deque()
                que.append((i,j))
                while que:
                    r,c = que.popleft()
                    for way in ((1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                        nr,nc = r+way[0],c+way[1]
                        if 0<=nr<h and 0<=nc<w and arr[nr][nc]:
                            que.append((nr,nc))
                            arr[nr][nc] = 0
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int,input().split())) for __ in range(h)]
    ans = 0
    check()
    print(ans)