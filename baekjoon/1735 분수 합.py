def div_list(n):
    i = 2
    num_ls = [1]
    while n > 1:
        if not n % i:
            num_ls.append(i)
            n //= i
            continue
        i += 1
    return num_ls

a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())

A = a1*b2 + b1*a2
B = a2*b2

div_nums = div_list(A)

for num in div_nums:
    if not B % num:
        B //= num
        A //= num
print(A,B)