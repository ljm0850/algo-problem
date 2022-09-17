def solve(target:str)->str:
    ans = ''
    temp = ""
    flag = False
    for alpha in target:
        if alpha == '<':
            ans += temp[::-1]
            flag = True
            temp = alpha
        elif alpha == '>':
            ans += temp+alpha
            temp = ""
            flag = False
        elif alpha == ' ' and not flag:
            ans += temp[::-1]+alpha
            temp = ""
        else:
            temp += alpha
    ans += temp[::-1]
    return ans

target = input()
answer=solve(target)
print(answer)