N,K = map(int,input().split())
temperatureArr = list(map(int,input().split()))
ans = sum(temperatureArr[:K])
value = ans
for i in range(K,N):
    value = value + temperatureArr[i] - temperatureArr[i-K]
    ans = max(ans,value)
print(ans)