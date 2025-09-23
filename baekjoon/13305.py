def solution(N:int,priceDataList:list[int],lengthDataList:list[int])->int:
    def createMinVauleList(N,nums:list[int])->list[int]:
        ls = [nums[0]]*N
        for i in range(1,N):
            ls[i] = min(nums[i],ls[i-1])
        return ls

    minPriceList = createMinVauleList(N,priceDataList)
    L = len(lengthDataList)
    total = 0
    for i in range(L)[::-1]:
        length = lengthDataList[i]
        total += length * minPriceList[i]
    return total

N = int(input())
lengthDataList = list(map(int,input().split()))
priceDataList = list(map(int,input().split()))
ans = solution(N,priceDataList,lengthDataList)
print(ans)