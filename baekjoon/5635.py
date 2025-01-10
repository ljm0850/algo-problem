def isYoung(data1,data2):
    if data1[2] < data2[2]:
        return False
    elif data1[2] > data2[2]:
        return True
    if data1[1] < data2[1]:
        return False
    elif data1[1] > data2[1]:
        return True
    if data1[0] < data2[0]:
        return False
    return True

n = int(input())
first:list[int] = [0,0,1989]
last:list[int] = [0,0,2011]
ans:list[str] = ['']*2
for _ in range(n):
    data = input().split()
    birth = list(map(int,data[1:]))
    if isYoung(birth,first):
        first = birth
        ans[0] = data[0]
    if not isYoung(birth,last):
        last = birth
        ans[1] = data[0]
print(*ans,sep='\n')