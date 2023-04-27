import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = []
for _ in range(N):
    nums = list(map(int,input().split()))
    temp = [0]
    sum_nums = 0
    for num in nums:
        sum_nums += num
        temp.append(sum_nums)
    arr.append(temp)

K = int(input())
for _ in range(K):
    i,j,x,y = map(int,input().split())
    ans = 0
    for r in range(i-1,x):
        ans += arr[r][y] - arr[r][j-1]
    print(ans)