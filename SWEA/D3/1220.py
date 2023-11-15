import sys
sys.stdin=open('input.txt')
import pprint
#테이블 윗분에 N극 , 아랫 부분에 S극

def transpose(arr):         #전치행렬
    length = len(arr)
    for i in range(length):
        for j in range(length):
            if i > j:
                arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    return arr

for tc in range(1,11):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]        #1은 N극성질을 가짐, 2는 S극 성질을 가짐
    transpose(arr)                                                  #이제부턴 1은 오른쪽, 2는 왼쪽으로 가야함
    cnt = 0
    for i in range(n):
        j = 0
        while j<99:
            if arr[i][j] == 1:                                      #1만 오른쪽으로 붙임
                if arr[i][j+1] != 2:
                    arr[i][j] = 0
                    arr[i][j+1] = 1
            j += 1
        for k in range(n-1):
            if arr[i][k] == 1 and arr[i][k+1] == 2:                 # 1,2 순서로 있으면 cnt 1씩 추가
                cnt +=1
    print(f'#{tc} {cnt}')


