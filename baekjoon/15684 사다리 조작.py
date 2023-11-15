import sys
input = sys.stdin.readline
def solution(cnt:int,h:int,s:int)->None:
    global ans
    if cnt >= ans:
        return
    if check():
        ans = min(ans,cnt)
        return
    if cnt == 3:
        return
    for r in range(h,H):
        if r == h:
            c = s
        else:
            c = 1
        while c < N-1:
            if arr[r][c] == 0 and arr[r][c+1] == 0:
                arr[r][c],arr[r][c+1] = 1,-1
                solution(cnt+1,r,c+2)
                arr[r][c],arr[r][c+1] = 0,0
                c += 1
            elif arr[r][c+1] == 0:
                c += 1
            else:
                c += 2

def check()->bool:
    for i in range(1,N):
        c = i
        for r in range(H):
            c += arr[r][c]
        if c != i:
            return False
    return True

N,M,H = map(int,input().split())
N += 1
arr = [[0]*(N) for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a-1][b] = 1
    arr[a-1][b+1] = -1
ans = 4
solution(0,0,1)
if ans != 4:
    print(ans)
else:
    print(-1)