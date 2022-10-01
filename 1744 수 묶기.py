def solve(arr:list[int]):
    minus_nums = []
    plus_nums = []
    for num in arr:
        if num > 0:
            plus_nums.append(num)
        else:
            minus_nums.append(num)
    minus_nums.sort()
    plus_nums.sort(reverse=True)

    max_value = 0
    for symbol in range(2):
        i = 0
        if symbol == 0:
            narr = minus_nums
            l = len(minus_nums)
        else:
            narr = plus_nums
            l = len(plus_nums)
        while i < l-1:
            now_num,next_num = narr[i],narr[i+1]
            if now_num + next_num <= now_num * next_num:
                max_value += now_num * next_num
                i += 2
            else:
                max_value += now_num
                i += 1
        if i == l-1:
            max_value += narr[i]
    return max_value

N = int(input())
nums = [int(input()) for _ in range(N)]
ans = solve(nums)
print(ans)
