x = int(input())
stick = 64
total = 0
cnt = 0
while total != x:
    if stick <= x - total:
        cnt +=1
        total += stick
    stick //= 2
print(cnt)
