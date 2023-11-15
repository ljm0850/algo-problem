T= int(input())

for i in range(1,T+1):
    money = int(input())
    cur = [50000,10000,5000,1000,500,100,50,10]
    solve = []
    for j in cur:
        if money // j != 0:
            solve.append(money//j)
            money -= j*(money//j)
        else:
            solve.append(0)
    print(f'#{i}')
    print(*solve)