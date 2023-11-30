T = int(input())

for i in range(T):
    target = list(map(int,input().split()))
    max = 0
    min = 10000

    for j in target:
        if j > max :
            max = j
        if j < min :
            min = j
    
    target.remove(max)
    target.remove(min)
    total = 0
    cnt = 0
    for k in target:
        total += k
        cnt += 1
    print(f'#{i+1} {round(total/cnt)}') 