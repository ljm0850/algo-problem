N = int(input())

numls=list(map(int,input().split()))
max_num = numls[0]
min_num = numls[0]
for i in numls:
    if max_num < i:
        max_num = i
    if min_num > i:
        min_num = i
print(min_num,max_num)