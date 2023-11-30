T=int(input('T를 입력해 주세요'))
for i in range(T):
    solve = 0
    a = map(int,input().split())
    for ii in a:
        if ii % 2 ==1 :
            solve += ii
    print(f'#{i+1} {solve}')