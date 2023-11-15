# 비효울적, 효율적으로 계산 하기 위해선 10번쨰줄 로직을 max,직전값 이용해야함
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int,input().split()))
    ls = [0]
    total = 0
    for num in nums:
        total += num
        ls.append(total)
    ans = -1000001
    for i in range(N+1):
        for j in range(i+1,N+1):
            ans = max(ans,ls[j]-ls[i])
    print(ans)