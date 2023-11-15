target = input().split('-')          # 길이는 50이하]
total = 0
for i in range(len(target)):
    temp = target[i].split('+')
    for j in temp:
        if i == 0:
            total += int(j)
        else:
            total -= int(j)
print(total)