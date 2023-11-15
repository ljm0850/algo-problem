import sys
input = sys.stdin.readline
def make_sum_ls(nums:list[int])->list[int]:
    ls = [0]
    total = 0
    for num in nums:
        total += num
        ls.append(total)
    return ls

N = int(input())
nums = list(map(int,input().split()))
sum_ls = make_sum_ls(nums)
M = int(input())
for _ in range(M):
    s,e = map(int,input().split())
    print(sum_ls[e]-sum_ls[s-1])