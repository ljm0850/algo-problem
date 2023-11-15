import sys
sys.stdin=open('input (1).txt')
import pprint

# n*n 배열
# 빈용기는 0
# n은 100이하



T = int(input())
for tc in range(1,11):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    j_cnt = 0
    solve = []
    for i in range(n):
        j_cnt = 0
        for j in range(n):
            i_cnt = 1
            if arr[i][j] != 0:          #화약품이 있으면 cnt만 올리고 확인한곳은 0으로 변경
                j_cnt +=1
                arr[i][j] = 0
            else :
                if j_cnt != 0:          #그전에 화약품이 있었다면
                    kk = i
                    while arr[kk+1][j-1] != 0:      #윗칸도 확인
                        i_cnt +=1
                        for k in range(j-j_cnt,j):
                            arr[kk+1][k] = 0            #확인한곳 0으로 변경
                        kk += 1      #그 다음줄도 탐색
                    if i_cnt != 1 or j_cnt != 0:
                        solve.append([i_cnt, j_cnt])
                    j_cnt = 0        #초기화 안하면 같은 선반에 또 화약품이 있을경우 숫자가 높게 나옴
    s_len=len(solve)
    for i in range(s_len)[::-1]:            #버블정렬을 이용하여 넓이, 같으면 행을 기준으로 정렬
        for j in range(i):
            if solve[j][0]*solve[j][1] > solve[j+1][0]*solve[j+1][1]:
                solve[j],solve[j+1] = solve[j+1],solve[j]
            elif solve[j][0]*solve[j][1] == solve[j+1][0]*solve[j+1][1]:
                if solve[j][0] > solve[j+1][0]:
                    solve[j], solve[j + 1] = solve[j+1], solve[j]
    print(f'#{tc} {len(solve)}',end=' ')
    for sol in solve:
        print(*sol,end=' ')
    print('')