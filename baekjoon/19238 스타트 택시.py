# N*N 배열
# M명의 손님
from collections import deque
import sys
input = sys.stdin.readline

def solution(N:int,M:int,oil:int,now_position:tuple[int],arr:list[list[int]],target:list[list[int]])->int:
    custom_check = [0]*(M)
    now_r,now_c = now_position
    for _ in range(M):
        # 현재 위치에서 손님까지의 거리 탐색
        length_arr = bfs(N,now_r,now_c,arr)
        short_length,short_idx = 400,-1
        for idx in range(M):
            if custom_check[idx]:
                continue
            nr,nc,gr,gc = target[idx]
            length = length_arr[nr][nc]
            if length == -1:
                return -1
            if length < short_length:
                short_length = length
                short_idx = idx
        custom_check[short_idx] = 1
        oil -= short_length
        # 손님 목적지로 이동
        r,c,gr,gc = target[short_idx]
        length_arr = bfs(N,r,c,arr)
        length = length_arr[gr][gc]
        if length == -1:
            return -1
        oil -= length
        if oil <0:
            return -1
        oil += 2*length
        now_r,now_c = gr,gc

    return oil


def bfs(N:int,r:int,c:int,arr:list[list[int]]):
    dr,dc = (1,-1,0,0),(0,0,1,-1)
    visit = [[-1]*N for _ in range(N)]
    visit[r][c] = 0
    que = deque()
    que.append((r,c))
    while que:
        r,c = que.popleft()
        cnt = visit[r][c]
        for d in range(4):
            nr,nc = r+dr[d], c+dc[d]
            if not (0<=nr<N and 0<=nc<N) or arr[nr][nc] == 1 or visit[nr][nc] != -1:
                continue
            visit[nr][nc] = cnt + 1
            que.append((nr,nc))
    return visit

N,M,oil = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
sr,sc = map(lambda x:x-1,map(int,input().split()))
target = [tuple(map(lambda x: x-1,map(int,input().split()))) for _ in range(M)]
target.sort(key=lambda x:(x[0],x[1]))
ans = solution(N,M,oil,(sr,sc),arr,target)
print(ans)