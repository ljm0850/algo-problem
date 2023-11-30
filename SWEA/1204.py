import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    tc = int(input().strip())
    nums = list(map(int,input().split()))
    check = dict()
    for num in nums:
        check[num] = check.get(num,0) + 1
    ans,maxCnt = 0,0
    for key in check:
        if check[key] > maxCnt:
            maxCnt = check[key]
            ans = key
        elif check[key] == maxCnt and ans < key:
            ans = key
    print(f'#{tc} {ans}')