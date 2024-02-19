N = int(input())
nums = list(map(int,input().split()))
max_cnt,ans = 0,0

for num in nums:
    cnt = 0
    while num:
        if num % 2:
            ans += 1
            num -= 1
        else:
            cnt += 1
            num //= 2
    max_cnt = max(max_cnt,cnt)
print(ans+max_cnt)