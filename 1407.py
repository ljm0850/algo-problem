A,B= map(int,input().split())
total = 0

def hm2(x) :
    n = 0
    solve = []
    total = 0
    while 2**n <= x :
        solve.append(x//2**n)
        n +=1
    for i in range(len(solve)-1):
        solve[i] -= solve[i+1]
    for j in range(len(solve)):
        total += 2**j*solve[j]
    return total

print(hm2(B)-hm2(A-1))