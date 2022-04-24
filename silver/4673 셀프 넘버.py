ans = [_ for _ in range(10001)]
for i in range(1,10000):
    temp = i
    for ii in str(i):
        temp += int(ii)
    if temp <= 10000:
        ans[temp] = 0
for t in ans:
    if t :
        print(t)