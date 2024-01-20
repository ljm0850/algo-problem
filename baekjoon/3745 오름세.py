def solution(nums:list[int]):
    record = [0]
    cnt = 0
    for num in nums:
        if record[-1] < num:
            cnt += 1
            record.append(num)
        else:
            idx = binary_search(cnt,num,record)
            record[idx] = num
    return cnt

def binary_search(length:int,num:int,arr:list[int])->int:
    s,e = 0,length
    while s<e:
        m = (s+e)//2
        if arr[m] < num:
            s = m + 1
        else:
            e = m
    return e

ans = list()
while True:
    try:
        N = int(input())
        nums = list(map(int,input().split()))
        ans.append(solution(nums))
    except:
        break
for a in ans:
    print(a)