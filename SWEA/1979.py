T = int(input())

for i in range(1,T+1):
    N,K = map(int,input().split())
    
    cnt = 0
    puzzle = []
    puzzle1 = []
    for j in range(N):
        puzzle.append(''.join(input().split()))
    #puzzle 가로 세로 변환
    for jj in range(N):
        asdf=''
        for kk in range(N):
            asdf += puzzle[kk][jj]
        puzzle1.append(asdf)
    
    
    #가로 확인
    for k in range(N):
        for ii in range(N-K+1):
            
            if ii == 0:
                if puzzle[k][ii:ii+K+1] == '1'*K+'0':
                    cnt +=1
            elif ii == N-K:
                if puzzle[k][ii-1:ii+K] == '0'+'1'*K:
                    cnt +=1
            else :
                if puzzle[k][ii-1:ii+K+1] == '0'+'1'*K+'0':
                    cnt +=1
    # # 세로 확인
    for k in range(N):
        for ii in range(N-K+1):
            
            if ii == 0:
                if puzzle1[k][ii:ii+K+1] == '1'*K+'0':
                    cnt +=1
            elif ii == N-K:
                if puzzle1[k][ii-1:ii+K] == '0'+'1'*K:
                    cnt +=1
            else :
                if puzzle1[k][ii-1:ii+K+1] == '0'+'1'*K+'0':
                    cnt +=1
    print(f'#{i} {cnt}')