import sys
sys.stdin=open('input.txt')

for _ in range(10):
    tc=input()
    arr = [list(map(int,input().split())) for _ in range(100)]
    totalls=[]
    totalz = 0
    totalz1 = 0
    for i in range(100):
        totalx = 0
        totaly = 0

        for j in range(100):
            totalx += arr[i][j] #가로
            totaly += arr[j][i] #세로
        totalz += arr[i][i] #대각선
        totalz1 += arr[99-i][99-i] #엇대각선
        totalls.append(totalx)
        totalls.append(totaly)
    totalls.append(totalz)
    totalls.append(totalz1)


    max_num =0
    for max in totalls : #최대값 구하기
        if max_num < max:
            max_num = max
    print(f'#{tc} {max_num}')