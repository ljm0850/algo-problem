def solve(name:str)->str:
    answer = ''
    alpha_cnt = [0]*26
    middle = ''
    for alpha in name:
        alpha_cnt[ord(alpha)-65] +=1
    for cnt in range(26):
        if alpha_cnt[cnt]:
            if alpha_cnt[cnt] %2:
                if not middle:
                    middle = chr(cnt+65)
                else: return "I'm Sorry Hansoo"
            answer += chr(cnt+65) * (alpha_cnt[cnt]//2)
    return answer + middle + answer[::-1]

name = input()
ans = solve(name)
print(ans)