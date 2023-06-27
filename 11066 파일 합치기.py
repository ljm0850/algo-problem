import sys
input = sys.stdin.readline

def sum_arr(N:int,arr:list[int]):
    value = [0] * (N)
    total = 0
    for i in range(N):
        total += arr[i]
        value[i] = total
    return value

def recur(s:int,e:int)->int:
    global dp,sum_ls
    if s == e:
        return 0
    if dp[s][e]:
        return dp[s][e]

    for i in range(s,e):
        a = recur(s,i)
        b = recur(i+1,e)
        c = sum_ls[e] - sum_ls[s-1]
        if dp[s][e]:
            dp[s][e] = min(dp[s][e],a+b+c)
        else:
            dp[s][e] = a+b+c
    return dp[s][e]

T = int(input())
for tc in range(T):
    K = int(input())
    file_size = [0] + list(map(int,input().split()))
    dp = [[0]*(K+1) for _ in range(K+1)]
    sum_ls = sum_arr(K+1,file_size)
    ans = recur(1,K)
    print(ans)