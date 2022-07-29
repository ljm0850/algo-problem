import math
def solve(n,m):
    ans = math.comb(m,n)
    return ans

T = int(input())

for tc in range(T):
    N,M = map(int,input().split())
    print(solve(N,M))