T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())              #N = 전체 사람 수 K=과제 제출한 사람 수
    study= list(map(int,input().split()))       #과제 한 사람이 누구인지
    print(f'#{tc}',end=' ')
    for i in range(1,N+1):
        if not i in study:
            print(i,end=' ')
    print('')
