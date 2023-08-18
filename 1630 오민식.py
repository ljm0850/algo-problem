def primeList(N:int)->list[int]:
    check = [True]*(N+1)
    for n in range(2,N//2+1):
        i = 2
        while True:
            num = n*i
            if num > N:
                break
            check[num] = False
            i += 1
        n += 1
    value = []
    for num in range(2,N+1):
        if check[num]:
            value.append(num)
    return value

def max_n(N:int,num:int)->int:
    n = num
    while N >= n:
        n *= num
    return n // num

def solution(N:int,nums:list[int])->int:
    div = 987654321
    value = 1
    for num in nums:
        value = (value*max_n(N,num))%div
    return value

N = int(input())
primeNums = primeList(N)
ans = solution(N,primeNums)
print(ans)