N,K = map(int,input().split())
total = 1
temp = K
while temp>0:
    total *= N
    N -= 1
    temp -= 1
while K > 0:
    total //= K
    K -= 1
print(total)