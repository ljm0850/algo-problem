from collections import deque
def solve(num):
    nums = deque()
    for i in range(1,num+1):
        nums.append(i)
    cnt = 0
    while nums:
        if cnt == 0:
            print(nums.popleft(),end=' ')
        else:
            temp = nums.popleft()
            nums.append(temp)
        cnt = (cnt+1)%2

N = int(input())
solve(N)