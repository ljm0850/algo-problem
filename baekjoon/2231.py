num = int(input())
solve = 0
for i in range(num//2,num):
    total = i
    temp = i
    while temp > 0:
        total += temp%10
        temp //= 10
    if total == num:
        solve = i
        break
print(solve)