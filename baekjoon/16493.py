import sys
input = sys.stdin.readline

N,M = map(int,input().split())
record = [-1]*(N+1)
record[0] = 0
for _ in range(M):
    day,page = map(int,input().split())
    for i in range(N-day+1)[::-1]:
        if record[i] != -1:
            record[i+day] = max(record[i+day],record[i]+page)
print(max(record))