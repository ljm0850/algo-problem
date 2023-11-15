A,B,C = map(int,input().split())
c = str(C)
nums = [True]*(B+1)
for i in range(2,B+1):
    if i**2 > B:
        break
    if nums[i]:
        for j in range(2*i,B+1,i):
            nums[j] = False
cnt = 0
for i in range(A,B+1):
    if nums[i] and c in str(i):
        cnt += 1
print(cnt)