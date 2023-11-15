def solution(n:int)->int:
    value = 0
    a,b = n//5,n%5
    if a == 0 and n%2:
        return -1
    elif b == 0:
        return a
    elif b%2:
        value += a - 1 + (b+5)//2
    else:
        value += a + (b)//2
    return value

n = int(input())
ans = solution(n)
print(ans)