def solve(num1:list[int],num2:list[int])->int:
    total = sum(num1) * sum(num2)
    return total
    
nums = input().split()
if len(nums) == 1:
    print(0)
else:
    A,B = list(map(int,nums[0])),list(map(int,nums[1]))
    ans = solve(A,B)
    print(ans)