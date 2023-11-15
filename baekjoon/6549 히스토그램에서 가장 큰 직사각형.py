import sys
input = sys.stdin.readline
def count_area(ls:list[int],idx:int,height:int)->int:
    value = 0
    while ls and height < ls[-1][0]:
        h,before_index = ls.pop()
        index = 0 if not ls else ls[-1][1]+1
        area = h*(idx-index)
        value = max(value,area)
    return value

def solution(arr:list[int])->int:
    N = len(arr)
    answer = 0
    ls = [(arr[0],0)]
    for i in range(1,N):
        height = arr[i]
        if not ls or height >= ls[-1][0]:
            ls.append((height,i))
        else:
            value = count_area(ls,i,height)
            answer = max(answer,value)
            ls.append((height,i))
    value = count_area(ls,N,0)
    answer = max(answer,value)
    return answer

while True:
    nums = list(map(int,input().split()))
    if nums[0] == 0:
        break
    ans = solution(nums[1:])
    print(ans)
