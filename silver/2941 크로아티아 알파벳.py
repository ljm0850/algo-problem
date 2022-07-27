word = list(input())
length = len(word)
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
num = 0
for alpha in croatia:
    l = len(alpha)
    i = 0
    while i < length:
        temp = word[i:i+l]
        target = ''.join(word[i:i+l])
        if target == alpha:
            for j in range(l):
                word[i+j] = str(num)
            num +=1
        i +=1
ans = 0
check = [0]*100
for leng in word:
    if leng.isdigit():
        leng = int(leng)
        if not check[leng]:
            check[leng] = 1
            ans +=1
    else:
        ans +=1
print(ans)