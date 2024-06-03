# D,N < 300,000, 지름은 10억 이하의 자연수
def minCheck(arr:list[int])->tuple[list,dict]:
    ls = list()
    cnt = dict()
    minValue = 1000000001 
    for num in arr:
        if num < minValue:
            minValue = num
            ls.append(minValue)
            cnt[minValue] = 1
        else:
            cnt[minValue] += 1
    return ls,cnt

def solution(D,N,oven,pizza):
    minList,cnt = minCheck(oven)
    for length in pizza:
        while minList:
            if length > minList[-1]:
                minList.pop()
            else:
                break
        if minList:
            ovenSize = minList[-1]
            cnt[ovenSize] -= 1
            if cnt[ovenSize] == 0:
                minList.pop()
        else:
            return 0
    value = 1
    for ovenSize in minList:
        value += cnt[ovenSize]
    return value

D,N = map(int,input().split())
oven = list(map(int,input().split()))
pizza = list(map(int,input().split()))
ans = solution(D,N,oven,pizza)
print(ans)