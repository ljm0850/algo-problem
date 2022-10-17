def GCD(n: int, k: int) -> int:
    k_divisor = divisor(k)
    k_prime = set(k_divisor)

    answer = []
    for num in k_prime:
        answer.append(check(n,num,k_divisor[num]))
    value = 1
    for ans in answer:
        if ans:
            value *= ans
    return value

def check(n:int,num:int,cnt:int)->int:
    value = 0
    for i in range(num,n+1):
        if value == cnt:
            return num ** cnt
        while i % num == 0 and value < cnt:
            value += 1
            i //= num

    return num ** value

def divisor(n: int) -> dict:
    divisor = {}
    num = n
    for i in range(2,n+1):
        if i*i > n:
            break
        while num % i == 0:
            num //= i
            divisor[i] = divisor.get(i, 0) + 1
    if num > 1:
        divisor[num] = 1

    return divisor

while True:
    try:
        n, k = map(int, input().split())
        if n == 0 : n = 1
        ans = GCD(n, k)
        print(ans)
    except:
        break