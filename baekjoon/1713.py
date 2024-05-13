N = int(input())
L = int(input())
arr = list(map(int,input().split()))

total = dict()
priority = dict()
result = set()
cnt = 1
for cert in arr:
    total[cert] = total.get(cert,0) + 1
    if len(result) < N and not cert in result:
        result.add(cert)
        priority[cert] = cnt
        cnt += 1
    elif not cert in result:
        minValue,minKey,minPri = 1001,0,101
        for key in result:
            pri = priority[key]
            if total[key] < minValue:
                minKey = key
                minPri = pri
                minValue = total[key]
            elif total[key] == minValue and minPri > pri:
                minPri = pri
                minKey = key
        result.remove(minKey)
        total[minKey] = 0
        result.add(cert)
        priority[cert] = cnt
        cnt += 1
ans = sorted(list(result))
print(*ans)