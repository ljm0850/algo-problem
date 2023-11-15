def solution(N):
    dp = [0]*(N+1)
    sq = squareNum(N)

    for i in range(1,N+1):
        temp = set()
        for num in sq:
            if num > i:
                break
            temp.add(dp[i-num])
        dp[i] = min(temp) + 1
    return dp[N]

def squareNum(num):
    ls = []
    n = 1
    while True:
        sq = n**2
        if sq > num:
            break
        ls.append(sq)
        n += 1
    return ls

N = int(input())
ans = solution(N)
print(ans)