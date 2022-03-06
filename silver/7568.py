def check(ls,i):
    cnt = 1
    for j in ls:
        if j != ls[i] and j[0] > ls[i][0] and j[1] > ls[i][1]:
            cnt += 1
    return cnt


N = int(input())            #사람수 2이상 50이하
member=[]
for _ in range(N):
    w,h = map(int,input().split())      #몸무게,키 10이상,200이하
    member.append([w,h])
solve = []
for i in range(N):
    temp = check(member,i)
    solve.append(temp)
print(*solve)