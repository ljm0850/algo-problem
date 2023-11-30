T = int(input())

for i in range(1,T+1):
    N,M = map(int,input().split())
    n = list(map(int,input().split()))
    m = list(map(int,input().split()))
    
    if N <= M :
        maximum = 0
        for j in range(M-N+1):
            ex = 0
            for jj in range(N):
                ex += n[jj]*m[jj+j]
            if maximum < ex:
                maximum = ex
        print(f'#{i} {maximum}')
    
    else:
        maximum = 0
        for j in range(N-M):
            ex = 0
            for jj in range(M):
                ex += n[jj+j]*m[jj]
            if maximum < ex:
                maximum = ex
        print(f'#{i} {maximum}')

