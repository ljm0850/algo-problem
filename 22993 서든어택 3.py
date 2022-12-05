import sys

def solution():
    N = int(sys.stdin.readline())
    damage = list(map(int,sys.stdin.readline().split()))
    now = damage[0]
    target = damage[1:]
    target.sort(reverse=True)
    while target:
        if now > target[-1]:
            now += target.pop()
        else:
            return "No"
    return "Yes"

ans = solution()
print(ans)