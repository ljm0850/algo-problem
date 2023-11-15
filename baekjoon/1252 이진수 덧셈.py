num1,num2 = input().split()
num1 = int(num1,2)
num2 = int(num2,2)
sum_num = num1 + num2
print(bin(sum_num)[2:])