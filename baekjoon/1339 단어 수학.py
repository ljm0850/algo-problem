def solve(nums:list[str])->int:
    alpha = [[0, chr(65 + _)] for _ in range(26)]

    for num in nums:
        n = len(num)
        for i in range(n):
            idx = ord(num[i]) - 65
            alpha[idx][0] += 10 ** (n - i - 1)
    alpha.sort(reverse=True)
    value = 0
    for i in range(10):
        value += alpha[i][0] * (9 - i)
    return value

N = int(input())
nums = [input() for _ in range(N)]
ans = solve(nums)
print(ans)