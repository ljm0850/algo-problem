def mindGap(str1:str,str2:str)->int:
    if record.get((str1,str2)):
        return record[(str1,str2)]
    value = 0
    for i in range(4):
        if str1[i] != str2[i]:
            value += 1
    record[(str1,str2)] = value
    record[(str2,str1)] = value
    return value

record = dict()
T = int(input())
for _ in range(T):
    N = int(input())
    temp = list(input().split())
    cnt = dict()
    for v in temp:
        cnt[v] = cnt.get(v,0)+1

    target = list()
    flag = False
    for v in cnt:
        if cnt[v] >= 3:
            flag = True
            break
        for _ in range(cnt[v]):
            target.append(v)
    if flag:
        print(0)
        continue
    T = len(target)
    minimumGap = 12
    for p1 in range(T-2):
        for p2 in range(p1+1,T-1):
            v1 = mindGap(target[p1],target[p2])
            for p3 in range(p2+1,T):
                v2 = mindGap(target[p1],target[p3])
                v3 = mindGap(target[p2],target[p3])
                minimumGap = min(v1+v2+v3,minimumGap)
    print(minimumGap)