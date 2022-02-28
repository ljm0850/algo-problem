import datetime
a=datetime.datetime.now()

M,N = map(int,input().split())
solve=[2]

for i in range(2,N+1):
    for j in solve:
        if j**2 > i:
            if i != 2:
                solve.append(i)
            break
        if i % j == 0:
            break
    else:
        solve.append(i)

for s in solve:
    if s >= M:
        print(s)

b=datetime.datetime.now()
print(b-a)