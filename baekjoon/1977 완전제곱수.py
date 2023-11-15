def find_start(M:int)->int:
    i = 1
    while i**2 < M:
        i += 1
    return i

M = int(input())
N = int(input())
ans = 0

min_num = find_start(M)
i = min_num
while i**2 <= N:
    target = i ** 2
    i += 1
    ans += target
if ans:
    print(ans)
    print(min_num**2)
else:
    print(-1)