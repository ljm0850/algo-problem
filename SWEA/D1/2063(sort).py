N = int(input())

target = list(map(int,input().split()))
# target.sort()
# print(target[int(N/2)])

for i in reversed(range(N)):
    for j in range(i):
        if target[j] < target[j+1]:
            target[j],target[j+1] = target[j+1],target[j]

print(target[int(N/2)])    