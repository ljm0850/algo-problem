import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)
def makeArr(R:int,C:int)->list[list]:
    arr = []
    for _ in range(R):
        temp = []
        target = input()
        for i in range(C):
            if target[i].isdigit():
                temp.append(int(target[i]))
            else:
                temp.append(target[i])
        arr.append(temp)
    return arr

def recur(r:int,c:int,cnt:int)->None:
    num = arr[r][c]
    for way in range(4):
        nr,nc = r+num*dr[way], c+num*dc[way]
        if 0<=nr<R and 0<=nc<C and arr[nr][nc] != 'H' and dp[nr][nc]<=cnt:
            if check[nr][nc] == True:
                print(-1)
                exit()
            check[nr][nc] = True
            dp[nr][nc] = cnt+1
            recur(nr,nc,cnt+1)
            check[nr][nc] = False

R,C = map(int,input().split())
arr = makeArr(R,C)
check = [[False]*C for _ in range(R)]
dp = [[0]*C for _ in range(R)]
check[0][0] = True
dp[0][0] = 1
dr,dc = (1,0,-1,0),(0,1,0,-1)
recur(0,0,1)
ans = 0
for r in range(R):
    ans = max(ans,max(dp[r]))
print(ans)