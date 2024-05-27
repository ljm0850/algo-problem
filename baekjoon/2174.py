def solution()->str:
    cols,rows = map(int,input().split())
    N,M = map(int,input().split())
    arr = [[0]*(cols+1) for _ in range(rows+1)] # 현재 지도 상태
    robotPosition = [[] for _ in range(N+1)]    # idx 로봇의 좌표
    robotDirection = [0]*(N+1)                  # idx 로봇이 보고 있는 방향
    conversionDir = { 'N':0, 'E':1,'S':2,'W':3 }
    dr,dc = (1,0,-1,0),(0,1,0,-1)

    # 초기 위치 세팅
    for i in range(1,N+1):
        c,r,d = input().split()
        r,c = int(r),int(c)
        arr[r][c] = i
        robotPosition[i] = [r,c]
        robotDirection[i] = conversionDir[d]
    # 명령
    for i in range(M):
        robotId,cmd,cnt = input().split()
        robotId,cnt = int(robotId),int(cnt)
        if cmd == 'R':
            robotDirection[robotId] = (robotDirection[robotId] + (cnt%4)) % 4
        elif cmd == 'L':
            robotDirection[robotId] = (robotDirection[robotId] + 4 - (cnt%4)) % 4
        else:
            originR,originC = robotPosition[robotId]
            r,c = originR,originC
            d = robotDirection[robotId]
            for _ in range(cnt):
                nr,nc = r+dr[d],c+dc[d]
                if not (0<nr<=rows and 0<nc<=cols):
                    return f"Robot {robotId} crashes into the wall"
                if arr[nr][nc] != 0:
                    return f"Robot {robotId} crashes into robot {arr[nr][nc]}"
                r,c = nr,nc
            robotPosition[robotId][0] = r
            robotPosition[robotId][1] = c
            arr[originR][originC] = 0
            arr[r][c] = robotId
    return "OK"
ans = solution()
print(ans)