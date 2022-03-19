#한번에 한,두개단 오르기 가능
#연속된 세 개의 계단 밟으면 안됨
#마지막 계단은 밟아야함

def step(x,cnt):
    global dp
    if x >= n:
        return -111111
    elif cnt == 3:
        return -111111
    if x == n-1:
        return 0
    if dp[x][cnt]:
        return dp[x][cnt]
    dp[x][cnt] = max(step(x+1,cnt+1)+stairs[x+1],step(x+2,1)+stairs[x+2])
    return dp[x][cnt]

n = int(input())
stairs = [int(input()) for _ in range(n)]+[0] * 2
dp = [[0]* 3 for _ in range(n+2)]
print(step(-1,0))