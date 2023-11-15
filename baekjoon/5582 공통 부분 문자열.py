str1 = input()
str2 = input()

if len(str1) > len(str2):
    long_str,short_str = str1,str2
else:
    long_str,short_str = str2,str1

answer = 0

dp = [[0]*len(short_str) for _ in range(2)]

for i in range(len(long_str)):
    for j in range(len(short_str)):
        if long_str[i] == short_str[j]:
            if j >= 1:
                dp[i%2][j] = dp[(i+1)%2][j-1] +1
                answer = max(answer,dp[i%2][j])
            else:
                dp[i%2][j] = 1
        else:
            dp[i%2][j] = 0
    answer = max(answer,max(dp[i%2]))

print(answer)
