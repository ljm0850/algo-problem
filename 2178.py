def bfs(si,sj):
    global maze
    global maze_mirror
    maze[si][sj] = 0
    maze_mirror[si][sj] = 1
    que = [[si,sj]]
    while que:
        i,j = que.pop(0)
        if i == N and j == M:
            return maze_mirror[i][j]

        for way in range(4):
            ni = i+di[way]
            nj = j+dj[way]
            if 0<=ni<=N and 0<=nj<=M and maze[ni][nj] :
                que.append([ni,nj])
                maze[ni][nj] = 0
                maze_mirror[ni][nj] = maze_mirror[i][j] +1

N,M = map(int,input().split())          # N,M = 도착지점
maze = [[0]*(M+1)]
maze_mirror = [[0]*(M+1) for _ in range(N+1)]
for _ in range(N):
    maze.append([0]+list(map(int,input())))
di=[1,-1,0,0]
dj=[0,0,1,-1]
print(bfs(1,1))