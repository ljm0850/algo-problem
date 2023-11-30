T = int(input())
 
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    cnt = 1
    way = 0
    di = [0,1,0,-1] #우하좌상
    dj = [1,0,-1,0]
    now = [0,0]
    while cnt <= N**2 :
 
        arr[now[0]][now[1]] = cnt
        now[0] += di[way]
        now[1] += dj[way]
        cnt += 1
 
        if 0>now[0] or now[0]>N-1 or 0>now[1] or now[1]>N-1 or arr[now[0]][now[1]] !=0:
            now[0] -= di[way]
            now[1] -= dj[way]
            if way == 3:
                way = 0
            else:
                way +=1
            now[0] += di[way]
            now[1] += dj[way]
    print(f'#{tc}')
    for sol in arr:
        print(*sol)