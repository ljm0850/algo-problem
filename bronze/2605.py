N=int(input())
number = list(map(int,input().split()))
solve=[]
for i in range(N):
    solve.insert(i-number[i],i+1)
print(*solve)