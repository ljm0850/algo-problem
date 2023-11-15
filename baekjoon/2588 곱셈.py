num1 = int(input())
num2 = int(input())
ans = num1 * num2
while num2:
    mod = num2%10
    print(num1*mod)
    num2 //= 10
print(ans)