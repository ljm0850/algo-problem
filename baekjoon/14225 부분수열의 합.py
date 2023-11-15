def recur(now_idx:int,value:int)->None:
    global total,nums,N
    total.add(value)
    if now_idx == N:    # 범위를 벗어남
        return
    for i in range(now_idx+1,N):# 현재 부분수열에 i번째 수를 추가(값만 더해가는 형식)
        recur(i,value+nums[i])

N = int(input())
nums = list(map(int,input().split()))
total = set()   # 모든 부분수열의 합이 recur함수에 의해 total에 저장됨
for i in range(N):
    recur(i,nums[i])
num = 1
while True:
    if not num in total:
        print(num)
        break
    num +=1