def sumArr(arr:list[int])->list[int]:
    length = len(arr)
    sumArr = [0]*(length+1)
    for i in range(1,length+1):
        sumArr[i] = sumArr[i-1] + arr[i-1]
    return sumArr

def solution(N,K,nums):
    sumNums = sumArr(nums)
    count = dict()
    ans = 0
    for i in range(1,N+1):
        sumNum = sumNums[i]
        if sumNum == K:
            ans += 1
        ans += count.get(sumNum-K,0)
        count[sumNum] = count.get(sumNum,0) + 1
    return ans

N,K = map(int,input().split())
nums = list(map(int,input().split()))
ans = solution(N,K,nums)
print(ans)