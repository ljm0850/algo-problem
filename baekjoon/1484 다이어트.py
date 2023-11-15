G = int(input())
ans = []
n1,n2 = 1,2
while n1 < n2:
    N1,N2 = n1*n1, n2*n2
    if N2-N1 == G:
        ans.append(n2)
        n1 += 1
        n2 += 1
    elif N2-N1 > G:
        n1 += 1
    else:
        n2 += 1
if ans:
    for num in ans:print(num)
else:
    print(-1)