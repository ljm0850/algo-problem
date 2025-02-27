def solution(T:int,ls:list[int])->list[int]:
    def createPrimeNumList(maximum:int)->list[int]:
        ls = [True]*(maximum+1)
        for num in range(2,maximum+1):
            if ls[num]== False: continue
            for multiple in range(2*num,maximum+1,num):
                ls[multiple] = False
        primeNumList = list()
        for num in range(2,maximum+1):
            if ls[num]:primeNumList.append(num)
        return primeNumList
     
    maximum = max(ls)
    primeNumList = createPrimeNumList(maximum)
    primeNumSet = set(primeNumList)
    ans = list()
    for num in ls:
        cnt = 0
        for primeNum in primeNumList:
            if primeNum > num // 2: break
            if (num-primeNum) in primeNumSet: cnt += 1
        ans.append(cnt)
    return ans

T = int(input())
numlist = [int(input()) for _ in range(T)]
ans = solution(T,numlist)
print(*ans,sep='\n')