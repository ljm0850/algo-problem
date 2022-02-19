arr = [input().split() for _ in range(5)]
cnt = 0
bingo = 0
for _ in range(5):
    if bingo >= 3:
        break
    call = input().split()
    for num in call:
        if bingo >= 3:
            break
        bp =0
        cnt +=1
        for i in range(5):
            if bingo >= 3:
                break
            for j in range(5):
                if bingo >= 3:
                    break
                if arr[i][j] == num:
                    arr[i][j] = 0
                    bp = 1
                    if arr[i] == [0,0,0,0,0]:
                        bingo +=1
                    if arr[0][j] == arr[1][j] == arr[2][j] ==arr[3][j]==arr[4][j]:
                        bingo +=1
                    if i == abs(4-j) :
                        if arr[0][4] == arr[1][3] ==arr[2][2] ==arr[3][1]==arr[4][0]:
                            bingo +=1
print(cnt)