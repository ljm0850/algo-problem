def solve(gap:int):
    if gap == 0:
        return 0
    n = 0
    while gap >= n**2:
        n += 1
    n -= 1
    after_gap = gap - n**2
    ans = 2*n-1 + (after_gap // n)
    if after_gap % n:
        ans += 1
    return ans

monkey, dog = map(int, input().split())
gap = dog-monkey
answer = solve(gap)
print(answer)