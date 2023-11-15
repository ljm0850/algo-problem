from itertools import permutations
N = int(input())
nums = list(map(int,input().split()))
total = permutations(nums,N)
ans = 0
for sequence in total:
    temp = 0
    for num_idx in range(N-1):
        temp += abs(sequence[num_idx]-sequence[num_idx+1])
    ans = max(ans,temp)
print(ans)