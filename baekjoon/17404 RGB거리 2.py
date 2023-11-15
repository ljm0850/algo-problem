import sys
def solve(start:int,N:int,cost:list)->int:
    value = 1000001
    dp = [[1000001]*3 for _ in range(2)]
    dp[0][start] = cost[0][start]
    index = 1
    for i in range(1,N):
        target = dp[(index+1)%2]
        dp[index][0] = min(target[1], target[2]) + cost[i][0]
        dp[index][1] = min(target[0], target[2]) + cost[i][1]
        dp[index][2] = min(target[0], target[1]) + cost[i][2]
        index = (index+1)%2

    for j in range(3):
        if j != start and dp[(N-1)%2][j]<value:
           value = dp[(N-1)%2][j]
    return value

N = int(sys.stdin.readline())
cost = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = 1000001
for color in range(3):
    temp = solve(color,N,cost)
    if temp < ans:
        ans = temp
print(ans)