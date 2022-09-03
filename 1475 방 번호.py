nums = [0]*10
N = list(input())

for num in N:
    nums[int(num)] +=1

temp = (nums[6]+nums[9])//2 + (nums[6]+nums[9]) %2
nums[6],nums[9] = temp,temp
print(max(nums))