def solve(ls,l):
    if l == M:
        sol.append(ls)
        return
    for num in nums:
        if lscount[num] < count_num[num]:           # 초기 nums에 들어있던 숫자 보다 작은 개수만 사용하게 설계
            lscount[num] += 1
            solve(ls+[num],l+1)
            lscount[num] -= 1

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
count_num = [0]*10001           # nums 안에 index에 해당하는 숫자가 몇개 있는지 기록
temp = []
for num in nums:
    count_num[num] += 1
    if count_num[num] > 1:
        temp.append(num)
for num in temp:            # 반복문 횟수를 줄이기 위해 중복수 제거
    nums.remove(num)

sol = []
lscount = [0]*10001         # 현재 만들고 있는 배열에서 index에 해당하는 숫자가 몇개 있는지 기록용
solve([],0)
for s in sol:
    print(*s)
