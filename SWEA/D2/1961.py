T= int(input())

for i in range(1,T+1):
    N = int(input())
    puzzle = []
    for j in range(N):
        puzzle.append(input().split())

    print(f'#{i}')
    for k in range(N):
        for kk in range(N):
            print(puzzle[N-kk-1][k],end='')
        print(' ',end='')
        for kk in range(N):
            print(puzzle[N-k-1][N-kk-1],end='')
        print(' ',end='')    
        for kk in range(N):
            print(puzzle[kk][N-k-1],end='')
        print(' ',end='')
        print('')