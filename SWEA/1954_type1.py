T = int(input())

for i in range(1,T+1):
    N = int(input())
    solve = []
    for j in range(N):
        a=[]
        for k in range(N):
            a.append(0)
        solve.append(a)
    
    for a in range(N):
        for b in range(N):
            # 테두리 완성
            if a == 0 :
                solve[a][b] = b+1
            elif a == N-1 :
                solve[a][b] = 3*N -2 - b
            elif b == N-1 :
                solve[a][b] = N+a
            elif b == 0 :
                solve[a][b] = 4*N -3 -a

            #
            elif N-a> b >= a :
                solve[a][b] = solve[a-1][a-1] + 4*N - 2*(a+1)**2 + 2*(a+1) + b -a
            elif a+b >= N-1 and a>=b:
                solve[a][b] = solve[N-a-1][N-a-1] + 3*(N-1-2*(N-a-1)) +(N-1-a) -b
            
    for a in reversed(range(N)):
        for b in reversed(range(N)):
            if solve[a][b] == 0:
                if b <= (N-1)/2:
                    solve[a][b] = solve[a+1][b] +1
                else :
                    solve[a][b] = solve[a+1][b] -1
    print(f'#{i}')
    
    for s in solve:
        print(*s)