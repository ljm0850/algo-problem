def check(x):
    if int(x**0.5) == x**0.5:           # 제곱근이 정수라면 1
        return 1

    for i in range(1,x):
        if i**2 > x:
            break
        if int((x-i**2)**0.5) == (x-i**2)**0.5:
            return 2

    for i in range(1,x):
        if i**2 > x:
            break
        for j in range(1,x):
            if i**2 +j ** 2 > x:
                break
            if int((x-i**2-j**2)**0.5) == (x-i**2-j**2)**0.5:
                return 3
    return 4

n = int(input())
print(check(n))