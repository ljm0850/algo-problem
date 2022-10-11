def dragon_curve(r:int,c:int,cnt:int,path:list)->None:
    global arr
    if cnt == -1:
        return

    for idx in range(len(path))[::-1]:
        next_d = (path[idx]+1)%4
        r,c = r+dr[next_d],c+dc[next_d]
        arr[r][c] = True
        path.append(next_d)
    dragon_curve(r,c,cnt-1,path)

def check(arr:list)->int:
    value = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
                value +=1
    return value

arr = [[False] * 101 for _ in range(101)]
dr,dc = (0,-1,0,1),(1,0,-1,0)
N = int(input())
for _ in range(N):
    # x는 column, y는 row
    x,y,d,g = map(int,input().split())
    # 0세대
    arr[y][x] = True
    r,c = y + dr[d], x + dc[d]
    arr[r][c] = True
    dragon_curve(r,c,g-1,[d])
ans=check(arr)
print(ans)