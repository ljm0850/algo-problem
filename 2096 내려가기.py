import sys
N = int(sys.stdin.readline())
dp = [[[0,0] for _ in range(3)] for __ in range(2)]

for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    ii = i % 2
    for j in range(3):
        if j == 0:
            dp[ii][j][0] = max(dp[1-ii][j][0],dp[1-ii][j+1][0])+temp[j]
            dp[ii][j][1] = min(dp[1-ii][j][1],dp[1-ii][j+1][1])+temp[j]
        elif j == 1:
            dp[ii][j][0] = max(dp[1-ii][j][0],dp[1-ii][j-1][0],dp[1-ii][j+1][0])+temp[j]
            dp[ii][j][1] = min(dp[1-ii][j][1],dp[1-ii][j-1][1],dp[1-ii][j+1][1])+temp[j]
        else:
            dp[ii][j][0] = max(dp[1-ii][j][0],dp[1-ii][j-1][0])+temp[j]
            dp[ii][j][1] = min(dp[1-ii][j][1],dp[1-ii][j-1][1])+temp[j]

max_point,min_point = 0,1000000
for target in dp[1-N%2]:
    if target[0] > max_point:
        max_point = target[0]
    if target[1] < min_point:
        min_point = target[1]
print(max_point,min_point)