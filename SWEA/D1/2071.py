T = int(input())
for i in range(T):
    total = 0
    cnt = 0
    a= map(int,input().split())
    for ii in a:
        total += ii
        cnt += 1
    avrg = round(total / cnt)
    print(f'#{i+1} {avrg}')