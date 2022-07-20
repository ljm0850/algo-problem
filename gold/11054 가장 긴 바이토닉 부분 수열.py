def solve():
    dp_increase,dp_decrease = [0]*N,[0]*N
    for i in range(N):
        dp_increase[i] = 1
        for j in range(i):
            if target[j] < target[i]:
                dp_increase[i] = max(dp_increase[i],dp_increase[j]+1)

    for i in range(N)[::-1]:
        dp_decrease[i] = 1
        for j in range(i,N)[::-1]:
            if target[j] < target[i]:
                dp_decrease[i] = max(dp_decrease[i],dp_decrease[j]+1)
    total = [0]*N
    for t in range(N):
        total[t] = dp_decrease[t] + dp_increase[t]
    print(max(total)-1)

N = int(input())
target = list(map(int,input().split()))

solve()