# import sys
# sys.stdin=open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N= int(input())             #농장의 크기 N*N N은 홀수
    arr = []
    total = 0
    arr = [list(map(int,input())) for _ in range(N)]
    temp1=N//2+1                #중앙값
    for i in range(temp1):      #중앙값 전까지
        temp2=arr[i][temp1-i-1:temp1+i]
        for j in temp2:
            total += j
    for ii in range(temp1,N):   #중앙값 이후
        temp3 = arr[ii][temp1-N+ii:temp1+N-ii-1]
        for jj in temp3:
            total +=jj
    print(f'#{tc} {total}')
