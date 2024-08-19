N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

inf = 601
record = [[[0]*3 for i in range(M+1)] for _ in range(2)]
for i in range(3):
    record[0][M][i] = inf
    record[1][M][i] = inf

p = 0
for r in range(N):
    np = (p+1)%2
    for c in range(M):
        record[np][c][0] = arr[r][c] + min(record[p][c-1][1],record[p][c-1][2])
        record[np][c][1] = arr[r][c] + min(record[p][c][0],record[p][c][2])
        record[np][c][2] = arr[r][c] + min(record[p][c+1][0],record[p][c+1][1])
    p = np
value = inf
for c in range(M):
    value = min(value,min(record[p][c]))
print(value)