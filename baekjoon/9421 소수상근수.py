def primeNumList(n):
    check = [False,False]+[True]*(n-1)
    for num in range(2,(n+1)//2):
        if check[num]:
            for multiNum in range(2*num,n+1,num):
                check[multiNum] = False
    value = list()
    for i in range(2,n+1):
        if check[i]:
            value.append(i)
    return value

def numCheck(num):
    isOk = checkList[num]
    match isOk:
        case 0:
            checkList[num] = -1
            newNum,tempNum = 0,num
            while tempNum:
                newNum += (tempNum%10)**2
                tempNum //= 10
            value = numCheck(newNum)
            checkList[num] = value
            return value
        case 1:
            return 1
        case -1:
            return -1

n = int(input())
primeNums = primeNumList(n)
checkList = [0]*(1000001)
checkList[1] = 1
for num in primeNums:
    if numCheck(num) == 1:
        print(num)