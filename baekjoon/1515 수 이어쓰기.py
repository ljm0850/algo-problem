def solution(target:str)->int:
    T = len(target)
    t, num = 0, 1
    while True:
        value = str(num)
        for v in value:
            if v == target[t]:
                t += 1
                if t == T:
                    return num
        num += 1

target = input()
ans = solution(target)
print(ans)