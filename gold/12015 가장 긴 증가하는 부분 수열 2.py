def solve(n:int,nums:list)->tuple:
    dp = [[1,[nums[_]]] for _ in range(n)]

    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[i][0] < dp[j][0]+1:
                    dp[i][0] = dp[j][0] +1
                    dp[i][1] = dp[j][1] + [nums[i]]
    max_cnt = dp[0][0]
    max_sequence = dp[0][1]
    for i in range(1,n):
        if dp[i][0] > max_cnt:
            max_cnt = dp[i][0]
            max_sequence = dp[i][1]
    return (max_cnt,max_sequence)

N = int(input())
target = list(map(int,input().split()))
ans = solve(N,target)
print(ans[0])
print(*ans[1])