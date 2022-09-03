N,K = map(int,input().split())
numls = list(map(int,input().split()))
max_sum=0
for _ in range(K):
    max_sum += numls[_]
num_sum = max_sum
for i in range(N-K):
    num_sum -= numls[i]
    num_sum += numls[i+K]
    if max_sum < num_sum:
        max_sum = num_sum
print(max_sum)