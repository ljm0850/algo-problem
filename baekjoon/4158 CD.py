import sys
input = sys.stdin.readline

while True:
    N,M = map(int,input().split())
    if N == 0 and M == 0:
        break
    cd_case = set()
    ans = 0
    for _ in range(N):
        cd_case.add(int(input()))
    for _ in range(M):
        cd = int(input())
        if cd in cd_case:
            ans += 1
    print(ans)