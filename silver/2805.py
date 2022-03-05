N,M = map(int,input().split())
woods = list(map(int,input().split()))
s = 1
e = max(woods)
while s <= e:
    total = 0
    H = (s+e)//2
    for i in woods:
        if i > H:
            total += i - H
    if total >= M:
        s = H+1
    else:
        e= H-1
print(e)