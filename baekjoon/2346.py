from collections import deque
N = int(input())
arr = list(map(int,input().split()))
nums = deque()
for i in range(N):
    num = arr[i]
    nums.append((num,i+1))
ans = list()
while nums:
    num,i = nums.popleft()
    if num > 0: num -= 1
    nums.rotate(-num)
    ans.append(i)
print(*ans)