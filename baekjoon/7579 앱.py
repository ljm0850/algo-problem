def solve(N:int,memories:list[int],prices:list[int])->int:
    max_price = sum(prices)+1
    dp = [[0]*max_price for _ in range(N+1)]
    answer = 10000000001
    for idx in range(1,N+1):
        price,memory = prices[idx],memories[idx]
        for now_cost in range(max_price):
            if now_cost < price:
                dp[idx][now_cost] = dp[idx-1][now_cost]
            else:
                dp[idx][now_cost] = max(memory + dp[idx-1][now_cost-price], dp[idx-1][now_cost])
                if M <= dp[idx][now_cost]:
                    answer = min(answer,now_cost)
    return answer

N,M = map(int,input().split())
memories = [0]+list(map(int,input().split()))
prices = [0]+list(map(int,input().split()))
ans = solve(N,memories,prices)
print(ans)
