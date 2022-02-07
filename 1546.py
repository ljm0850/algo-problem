N= int(input())
target = list(map(int,input().split()))
maximum = target[0]
total=0
for i in target:
    if maximum < i:
        maximum = i

for j in target:
    total += j/maximum*100
print(total/N)