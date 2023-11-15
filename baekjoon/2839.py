N = int(input())
cnt = -1
d = N//5

for i in range(d+1)[::-1]:
    temp = N - 5*i
    if not temp % 3 :
        cnt = i+temp//3
        break
print(cnt)