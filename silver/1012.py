import sys

di=[1,-1,0,0]
dj=[0,0,1,-1]

def spread(i,j):
    global arr
    que = [[i,j]]
    while que:
        c,r = que.pop()
        arr[c][r] = 0
        for way in range(4):
            nc = c+di[way]
            nr = r+dj[way]
            if 0<=nc<N and 0<=nr<M and arr[nc][nr] and not [nc,nr] in que:
                que.append([nc,nr])

T = int(input())

for tc in range(1,T+1):
    M,N,K = map(int,input().split())            # M = 가로 N = 세로 50이하 //K = 배추 수 2500이하
    arr = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        r,c = map(int,sys.stdin.readline().split())
        arr[c][r] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt +=1
                spread(i,j)
    print(cnt)