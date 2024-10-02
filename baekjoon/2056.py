import sys
input = sys.stdin.readline

N = int(input())
check = [0]*(N+1)
for node in range(1,N+1):
    time,P,*works = map(int,input().split())
    if P:
        added_time = 0
        for work in works:
            added_time = max(added_time,check[work])
        time += added_time
    check[node] = time
print(max(check))