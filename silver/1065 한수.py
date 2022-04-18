def check():
    cnt = 0
    for i in range(1,N+1):
        target = str(i)
        if len(target) == 1:
            cnt +=1
            continue
        t = int(target[0])-int(target[1])
        for j in range(1,len(target)):
            if int(target[j-1])-int(target[j]) != t:
                break
        else:
            cnt +=1
    return cnt

N = int(input())
print(check())