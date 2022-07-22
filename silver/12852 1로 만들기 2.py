def solve(end:int)->list():
    dp = [(0,[]) for _ in range(max(N+1,3))]
    dp[1]=(0,[1])
    dp[2]=(1,[1,2])

    for i in range(3,end+1):
        ls = [(dp[i-1][0]+1,dp[i-1][1]+[i])]
        if not i % 3:
            ls.append((dp[i//3][0]+1,dp[i//3][1]+[i]))
        if not i % 2:
            ls.append((dp[i//2][0]+1,dp[i//2][1]+[i]))

        best_cnt = ls[0][0]
        best_path = ls[0][1]
        for cnt,path in ls:
            if best_cnt > cnt:
                best_cnt = cnt
                best_path = path
        dp[i] = (best_cnt,best_path)
    return dp[end]

N = int(input())
ans = solve(N)
print(ans[0])
print(*ans[1][::-1])