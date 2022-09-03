nums = list(map(int,input().split()))
i = 1
while True:
    cnt = 0
    for num in nums:
        if not i%num:
            cnt +=1
    if cnt >= 3:
        print(i)
        break
    i += 1