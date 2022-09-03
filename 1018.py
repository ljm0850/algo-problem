N,M = map(int,input().split())      #N,M은 8이상 50이하
chess = ['WBWBWBWB','BWBWBWBW']
arr = []
[arr.append(input()) for _ in range(N)]       #M*N  크기 보드판
best_cnt= 32
for i in range(N-7):        #M*N 보드판을 8*8로 자르면 나오는 수
    for j in range(M-7):
        for ch in range(2): #chess 배열 두가지,
            cnt = 0
            for n in range(8):  #가로줄 8개
                for num in range(8): #세로줄 8개, 세로줄을 이동하여 왼쪽에서 오른쪽으로 검색
                    if arr[i:i+8][n][j:j+8][num] != chess[ch-n%2][num]: #ch-n%2는 줄마다 흑백바꾸려고
                        cnt +=1
            if best_cnt > cnt:
                best_cnt = cnt 
print(best_cnt)