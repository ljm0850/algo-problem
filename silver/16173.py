def check():
    visited = [[0]*N for _ in range(N)]
    que = [(0,0)]
    while que:
        r,c = que.pop(0)
        for dr,dc in ((1,0),(0,1)):
            nr = r +dr*arr[r][c]
            nc = c +dc*arr[r][c]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                if arr[nr][nc] == -1:
                    print('HaruHaru')
                    return
                visited[nr][nc] = 1
                que.append((nr,nc))
    print('Hing')
    return

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
check()