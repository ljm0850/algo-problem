def solve(min_num, max_num):
    check = [True]*(max_num-min_num+1)
    i = 2
    while True:
        square_num = i*i
        if square_num > max_num:
            break
        j = min_num // square_num + 1
        if min_num % square_num == 0:
            check[-1] = False

        num = square_num * j
        while num <= max_num:
            check[max_num-num] = False
            j += 1
            num = square_num * j
        i += 1
    ans = 0

    for c in check:
        if c:
            ans += 1
    return ans


min_num, max_num = map(int, input().split())
ans = solve(min_num, max_num)
print(ans)
