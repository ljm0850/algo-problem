import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
check = [True] * (N+1)
ans = [0]*Q
for i in range(Q):
    value = int(input())
    num = value
    while num:
        if not check[num]:
            ans[i] = num
        num //= 2
    check[value] = False
print(*ans,sep='\n')