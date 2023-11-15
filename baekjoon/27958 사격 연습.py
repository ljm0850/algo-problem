import copy
def solution(K:int,bullets:list[int])->None:
    ls = []
    for bullet in bullets:
        ls.append((bullet,0))
    recur(K,0,0)

def recur(K:int,idx:int,point:int)->None:
    global ans
    ans = max(ans,point)
    if K == idx:
        return
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                p,ls = shot(r,c,idx)
                if p:
                    bf,obf = arr[r][c],origin[r][c]
                    arr[r][c],origin[r][c] = 0,0
                    for nr,nc in ls:
                        arr[nr][nc] = p//4
                        origin[nr][nc] = p//4
                    # 재귀
                    recur(K,idx+1,point+p)
                    # 되돌리기
                    arr[r][c],origin[r][c] = bf,obf
                    for nr,nc in ls:
                        arr[nr][nc] -= p//4
                        origin[nr][nc] == 0
                else:
                    arr[r][c] -= bullets[idx]
                    recur(K,idx+1,point)
                    arr[r][c] += bullets[idx]
                break

def shot(r:int,c:int,idx:int)->tuple[int,list]:
    bullet = bullets[idx]
    now = arr[r][c]
    if now >= 10:
        return (now,[])
    if bullet >= now:
        temp = []
        for way in range(4):
            nr,nc = r+dr[way], c+dc[way]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 0:
                temp.append((nr,nc))
        return (origin[r][c],temp)
    else:
        return (0,[])

N = int(input())
K = int(input())
origin = [list(map(int,input().split())) for _ in range(N)]
arr = copy.deepcopy(origin)
bullets = list(map(int,input().split()))
dr,dc = (1,0,-1,0),(0,1,0,-1)
ans = 0
solution(K,bullets)
print(ans)