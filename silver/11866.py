import sys

N,K = map(int,sys.stdin.readline().split())
nums = [_ for _ in range(1,N+1)]
print('<',end='')
while nums:
    for i in range(K):
        if i != K-1:
            nums.append(nums.pop(0))
        else:
            print(nums.pop(0),end='')
            if nums:
                print(',',end=' ')
print('>')