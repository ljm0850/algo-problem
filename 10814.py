N = int(input())
member = [[] for _ in range(201)]
for i in range(N):
    temp = input().split()
    member[int(temp[0])].append(temp)

for i in member:
    if i :
        for j in i:
            print(*j)