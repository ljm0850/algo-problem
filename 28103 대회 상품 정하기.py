N,M,X = map(int,input().split())
prices = list(map(int,input().split()))
default = prices[-1]
X -= default*N
for m in range(M):
    prices[m] -= default
ans = [0]*M

for m in range(M-1):
    price = prices[m]
    if price:
        value = min(X//price,N)
        ans[m] += value
        N -= value
        X -= value*price
ans[-1] = N
print(*ans)