import sys
sys.stdin=open('input.txt')

def check(ls,n):                #전치행렬 확인
    global cnt
    for i in range(n//2):
        if ls[i] != ls[-1-i]:
            return
    cnt += 1

for tc in range(1,11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0                 #N길이의 회문이 몇개인지 세는용, 함수에서 증가함
    for i in range(8):
        temp1 = []          #가로(행) 확인용
        temp2 = []          #세로(열) 확인용
        for k in range(N):
            temp1 += arr[i][k]  #초기값, 길이 k만큼 새로운 list 생성
            temp2 += arr[k][i]
        check(temp1,N)          #초기값 확인
        check(temp2,N)
        for kk in range(8-N):   #초기값에서 맨 앞 글자 뺴고 뒷글자 추가
            temp1.pop(0)
            temp2.pop(0)
            temp1.append(arr[i][N+kk])
            temp2.append(arr[N+kk][i])
            check(temp1,N)
            check(temp2,N)
    print(f'#{tc} {cnt}')