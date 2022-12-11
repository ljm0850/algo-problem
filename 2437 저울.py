N = int(input())
weights = list(map(int,input().split()))
weights.sort()
ans = 1

for weight in weights:
    if ans < weight:
        break
    ans += weight
print(ans)
