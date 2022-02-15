N= int(input())
paper = []
for _ in range(1,N+1):
    paper.append(list(map(int,input().split())))
max_j=0
max_k=0
for i in paper:
    if max_j < i[0]+i[2]:
        max_j = i[0]+i[2]
    if max_k < i[1]+i[3]:
        max_k = i[1]+i[3]
if max_j < max_k:
    max_j = max_k
arr = [[0]*max_j for _ in range(max_j)]

for i in range(N):
    for j in range(paper[i][0],paper[i][0]+paper[i][2]):
        arr[j][paper[i][1]:paper[i][1]+paper[i][3]] = [i+1]*(paper[i][3])

for i in range(1,N+1):
    total = 0
    for j in arr:
        total += j.count(i)
    print(total)