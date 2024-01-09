n = int(input())
nums = list(map(int,input().split()))
record = [1]*(n)
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            record[i] = max(record[i],record[j]+1)
print(max(record))