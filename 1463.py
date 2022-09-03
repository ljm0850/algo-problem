# x가 3의 약수이면 3으로 나눔
# x가 2의 약수이면 23로 나눔
# 1을뻄


x = int(input())
dp = [0] * 1000001
dp[2] = 1


for i in range(3,x+1):
    ls = [dp[i-1]+1]
    if not i % 3:
        ls.append(dp[i//3]+1)
    if not i % 2:
        ls.append(dp[i//2]+1)
    dp[i] = min(ls)
print(dp[x])