def bubble_sort(ls):
    for i in range(len(ls))[::-1]:
        for j in range(i):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
    return ls

member=[]
total = 0
for _ in range(9):
    temp = int(input())
    member.append(temp)
    total += temp
member = bubble_sort(member)
start,end = 0,-1
total -= 100
while True:
    if member[start] + member[end] == total:
        member.remove(member[start])
        member.remove(member[end])
        break
    elif member[start] + member[end] > total:
        end -=1
    else:
        start +=1
for A in member:
    print(A)