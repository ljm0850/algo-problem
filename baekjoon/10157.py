C,R = map(int,input().split())      #공연장의 격자 크기 5이상 1000이하
K =int(input())                     #대기번호

arr = [[0]*C for _ in range(R)]
way = 0                             #방향
dx=[0,1,0,-1]                       #상우하좌
dy=[1,0,-1,0]
y=0
x=0                                 #현위치 y,x
cnt = 1
while cnt <=K:
    if K > C*R:
        break

    if arr[y][x] == 0:
        arr[y][x] = cnt
        y += dy[way]
        x += dx[way]
    cnt += 1

    if y<0 or x<0 or x>C-1 or y > R-1 or arr[y][x] != 0:
        y -= dy[way]
        x -= dx[way]
        if way == 3:
            way = 0
        else:
            way +=1
        y += dy[way]
        x += dx[way]
if K > C*R:
    print(0)
else:
    print(x-dx[way]+1,y-dy[way]+1)