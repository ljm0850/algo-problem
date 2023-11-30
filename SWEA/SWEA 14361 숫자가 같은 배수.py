def check(target:int,nums:list)->bool:
    cnt = [0]*10
    while target:
        cnt[target%10] += 1
        target //= 10
    for num in nums:
        tempCnt = [0]*10
        while num:
            tempCnt[num%10] += 1
            num //= 10
        for idx in range(10):
            if cnt[idx] < tempCnt[idx]:
                break
        else:
            return True
    return False

T = int(input())
for tc in range(1,T+1):
    num = input()
    n = 10**len(num)
    num = int(num)
    nums = []
    temp = num
    while not temp // n:
        temp += num
        nums.append(temp)
    ans = check(num,nums)
    if ans :
        print(f'#{tc} possible')
    else:
        print(f'#{tc} impossible')

