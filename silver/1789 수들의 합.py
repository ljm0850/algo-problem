S = int(input())
i = 1
while True:
    if (i+1)*i//2 <= S:
        i +=1
    else:
        break
print(i-1)