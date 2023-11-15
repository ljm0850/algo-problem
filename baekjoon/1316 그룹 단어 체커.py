N = int(input())
ans = 0
for _ in range(N):
    target = input()
    check = {}
    cnt = True
    for i in range(len(target)):
        if not check.get(target[i]):
            check[target[i]] = True
        else:
            if target[i-1] != target[i]:
                cnt = False
                break
    if cnt:
        ans += 1
print(ans)