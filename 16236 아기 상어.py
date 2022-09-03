# 먹을 수 있는 가장 가까운 물고기찾아 감
# 거리가 같다면 가장 위에 있는 물고기, 그중에서도 제일 왼쪽을 먼저 타겟
# 크기와 같은 수의 물고기를 먹을 떄 마다 크기가 1 증가
# 크기가 같은 물고기는 먹을순 없지만 지나갈 수는 있다
# 크기가 큰 물고기는 못지나감
# 시작 크기는 2

from collections import deque
def search(si,sj):
    global size,eat,time
    que = deque()
    que.append((si,sj))
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    cnt = 0
    while que:
        cnt += 1
        solve = []
        for _ in range(len(que)):       # 같은 거리 단위로 반복문이 돌게
            r, c = que.popleft()
            for way in range(4):
                nr, nc = r + dr[way], c + dc[way]  # 다음 이동 좌표
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] <= size:  # 범위안, 사이즈보다 작거나 같으면 지나감
                    visited[nr][nc] = 1
                    que.append((nr,nc))
                    if 0<arr[nr][nc]<size :  # 잡아 먹을 수 있다면
                        solve.append((nr,nc))
        if solve:
            time += cnt
            eat += 1
            if eat == size:
                size +=1
                eat = 0
            solve.sort(key=lambda x:(x[0],x[1]))
            nr,nc=solve[0][0],solve[0][1]
            arr[nr][nc] = 0
            search(nr,nc)


dr = [-1,0,0,1]
dc = [0,-1,1,0]
N = int(input())            #2이상 20이하
arr = []
for _ in range(N):
    temp = list(map(int,input().split()))
    for s in range(N):
        if temp[s] == 9:
            si = _
            sj = s
    arr.append(temp)
arr[si][sj] = 0
time = 0
size = 2
eat = 0
search(si,sj)
print(time)