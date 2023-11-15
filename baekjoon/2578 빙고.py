def solution():
    global arr
    answer = 0
    cnt = 0
    for _ in range(5):
        nums = input().split()
        for num in nums:
            answer += 1
            r,c = position[num]
            arr[r][c] = '0'
            cnt += check(r,c)
            if cnt >= 3:
                return answer

def check(r,c):
    value = 0
    for nr in range(5):
        if arr[nr][c] != '0':
            break
    else: value+=1
    for nc in range(5):
        if arr[r][nc] != '0':
            break
    else: value+=1
    if r==c:
        for i in range(5):
            if arr[i][i] != '0':
                break
        else:value+=1
    if r+c == 4:
        for i in range(5):
            if arr[i][4-i] !='0':
                break
        else:value+=1
    return value

arr = []
position = {}
for r in range(5):
    nums = input().split()
    arr.append(nums)
    for c in range(5):
        position[nums[c]] = (r,c)

ans = solution()
print(ans)