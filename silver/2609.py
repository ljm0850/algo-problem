num = list(map(int,input().split()))
solve = []
for i in num:
    numls = []
    d = 2
    while d <= i:
        while not i % d :
            numls.append(d)
            i //= d
        d += 1
    solve.append(numls)
temp1=solve[0]
temp2=solve[1]
gcd = 1
for i in temp1:
    if i in temp2:
        gcd *= i
        temp2.remove(i)
print(gcd)
print(num[0]*num[1]//gcd)

