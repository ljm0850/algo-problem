N = int(input())                                  #100이하
nums = list(map(int,input().split()))           #1000 이하의 자연수
max_n = 0
cnt = 0
for n in nums:
    if max_n < n:
        max_n = n
target = [i for i in range(0,max_n+1)]

i = 2                               #인덱스 번호용
div = 2                             #나누고자 하는 값(소수들)
while div**2 <= max_n:
    j = 2
    while div * j <= max_n:             #배수들 제거
        temp = div * j
        target[temp] = -1
        j += 1
    while True:                     #다음 소수 찾기
        i += 1
        if target[i] < 0:
            continue
        div = target[i]
        break
for s in nums:
    if s != 1 and s in target:
        cnt += 1
print(cnt)