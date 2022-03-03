M,N = map(int,input().split())
solve=[2]

for i in range(2,N+1):
    for j in solve:
        if j**2 > i:
            if i != 2:
                solve.append(i)
            break
        if i % j == 0:
            break
    else:
        solve.append(i)

for s in solve:
    if s >= M:
        print(s)

#친구에게 도움 받은 코드
#M, N = map(int, input().split())
# nums = [i for i in range(0,N+1)]
# i=2
# a=2
# while a ** 2 <= N:
#     j=2
#     while a*j<=N:
#         loc = a*j
#         nums[loc] = -1
#         j=j+1
#     while True:
#         i=i+1
#         if nums[i] < 0:
#             continue
#         a = nums[i]
#         break

# for s in range(M,len(nums)):
#     if nums[s] > 1:
#         print(nums[s])