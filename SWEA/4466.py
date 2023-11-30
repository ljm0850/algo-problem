import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())              # N개의 과목, K개만 기입
    point = list(map(int,input().split()))
    total = 0
    for i in range(N)[::-1]:                    #버블정렬을 이용하여 큰수가 앞에 오도록
        for j in range(i):
            if point[j] < point[j+1]:
                point[j],point[j+1] = point[j+1],point[j]
    for k in range(K):
        total += point[k]                       #제일앞이 큰수, 큰수부터 필요한 k개 더하기
    print(f'#{tc} {total}')