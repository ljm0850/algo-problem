def solution(coins:list[int],M:int)->int:
    record = [0]*(M+1)
    for coin in coins:
        record[coin] += 1
        for i in range(coin,M+1):
            record[i] += record[i-coin]
    return record[M]

T = int(input())
for tc in range(T):
    N = int(input())
    coins = list(map(int,input().split()))
    M = int(input())
    ans = solution(coins,M)
    print(ans)