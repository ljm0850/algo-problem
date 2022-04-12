N = int(input())
num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))
num1.sort()
num2.sort()
total = 0
for i in range(N):
    total += num1[i] * num2[N-i-1]
print(total)