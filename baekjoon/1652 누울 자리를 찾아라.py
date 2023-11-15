N = int(input())
arr = [input() for _ in range(N)]
rans,cans = 0,0

for i in range(N):
    rcnt,ccnt = 0,0
    for j in range(N):
        if arr[i][j] == '.':
            rcnt += 1
        else:
            rcnt = 0
        if rcnt == 2:
            rans += 1
        if arr[j][i] == '.':
            ccnt += 1
        else:
            ccnt = 0
        if ccnt == 2:
            cans += 1
print(rans,cans)

