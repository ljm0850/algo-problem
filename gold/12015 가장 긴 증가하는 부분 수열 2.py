import sys
def solve(arr:list)->int:
    dp = [0]
    cnt = 0
    for num in arr:
        if dp[-1] < num:
            dp.append(num)
            cnt += 1
        else:
            start, end = 0, cnt
            while start < end:
                mid = (start + end) // 2
                if dp[mid] < num:
                    start = mid + 1
                else:
                    end = mid
            dp[end] = num
    return cnt

N = int(sys.stdin.readline())
total_sequence = list(map(int,sys.stdin.readline().split()))
ans = solve(total_sequence)
print(ans)