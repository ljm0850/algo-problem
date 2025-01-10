def solution(X:str)->int:
    num = list(X)
    n = len(num)
    i = n-2
    while i>=0 and num[i] >= num[i+1]:
        i -= 1
    if i == -1:
        return 0
    idx = n-1
    while num[idx] <= num[i]:
        idx -= 1
    num[i],num[idx] = num[idx],num[i]
    num = num[:i+1] + sorted(num[i+1:])
    return int(''.join(num))
X = input()
ans = solution(X)
print(ans)