N = int(input())
data = list(map(int,input().split()))
INF = 1001
record = [INF]*(N)
if N == 1:
    print(0)
    exit()
for i in range(1,min(data[0]+1,N)):
    record[i] = 1
for i in range(1,N):
    if record[i] == INF:
        continue
    cnt = record[i] + 1
    for j in range(1,data[i]+1):
        if i+j >=N:
            break
        record[i+j] = min(record[i+j],cnt)
if record[N-1] == INF:
    print(-1)
else:
    print(record[N-1])
