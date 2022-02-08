num=[]
maximum = 0
for i in range(9):
    num.append(int(input()))
for j in num:
    if maximum < j:
        maximum = j
print(maximum)
print(num.index(maximum)+1)