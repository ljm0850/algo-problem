N,K = map(int,input().split())
nums = []
n = N
for _ in range(K):
    nums.append(int(str(n)[::-1]))
    n += N
print(max(nums)) 