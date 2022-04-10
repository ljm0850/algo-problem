# 현재 좌표에서 4칸내로 이동할수 있는 모든 곳의 합 구해야 할듯
# 결국 pypy 제출
import sys
def search(use):
    global ans
    for r,c in use:
        for way in range(4):
            nr,nc = r+dr[way],c+dc[way]
            if 0<=nr<N and 0<=nc<M and not check[nr][nc] and not (nr,nc) in use :
                if len(use) == 3:
                    temp = 0
                    for sr, sc in use:
                        temp += arr[sr][sc]
                    temp += arr[nr][nc]
                    if temp > ans:
                        ans = temp
                    continue
                search(use+[(nr,nc)])

dr = [1,0,-1,0]
dc = [0,1,0,-1]

N,M = map(int,input().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = 0
check = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        check[i][j] = 1
        search([(i,j)])
print(ans)

# ------------------------------------------------------------------
# import sys
# def bfs(r,c,total,visited):
#     global ans
#     total += arr[r][c]
#     if len(visited) == 4:
#         if ans < total:
#             ans = total
#         return
#     for way in range(4):
#         nr,nc = r+dr[way],c+dc[way]
#         if 0<=nr<N and 0<=nc<M and not check[nr][nc] and (nr,nc) not in visited:
#             bfs(nr,nc,total,visited+[(nr,nc)])
#
# def t_spin(r,c):
#     global ans
#     if c+2<M:
#         temp = 0
#         for i in range(3):
#             temp += arr[r][c+i]
#         if 0<=r-1:
#             temp += arr[r-1][c+1]
#             if ans < temp:
#                 ans = temp
#             temp -= arr[r-1][c+1]
#         if r+1<N:
#             temp += arr[r+1][c+1]
#             if ans < temp:
#                 ans = temp
#     if r+2<N:
#         temp = 0
#         for i in range(3):
#             temp += arr[r+i][c]
#         if 0<=c-1:
#             temp += arr[r+1][c-1]
#             if ans < temp:
#                 ans = temp
#             temp -= arr[r+1][c-1]
#         if c+1<M:
#             temp += arr[r+1][c+1]
#             if ans < temp:
#                 ans = temp
#
#
# dr = [1,0,-1,0]
# dc = [0,1,0,-1]
# N,M = map(int,input().split())
# arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# ans = 0
# check = [[0]*M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         check[i][j] = 1
#         bfs(i,j,0,[(i,j)])
#         t_spin(i,j)
# print(ans)