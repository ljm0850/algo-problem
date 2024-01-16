N = int(input())
nums = [0] + list(map(int,input().split()))
ans = list()
stack = list()

for i in range(1,N+1):
    num = nums[i]
    while stack:
        if nums[stack[-1]] < num:
            stack.pop()
        else:
            break
    if stack:
        ans.append(stack[-1])
    else:
        ans.append(0)
    stack.append(i)
print(*ans)