def div(n:int,num:int)->int:
    value = 0
    while n != 0:
        n //= num
        value += n
    return value

n,m = map(int,input().split())
print(min(div(n,2)-div(n-m,2)-div(m,2),div(n,5)-div(n-m,5)-div(m,5)))