def make_sum_ls(Target:str)->list[int]:
    global check
    T = len(Target)
    ls = [0]
    cnt = 0
    for idx in range(T):
        alpha = Target[idx]
        if not alpha in check:
            cnt += 1
        ls.append(cnt)
    return ls

def make_check(Target:str)->set[str]:
    value = set()
    for idx in range(26):
        if Target[idx]=='1':
            value.add(chr(97+idx))
    return value

def solution(S:str,ls:list[int],k:int)->int:
    value = set()
    L = len(ls)
    for s in range(L):
        for e in range(s+1,L):
            if ls[e]-ls[s] > k:
                break
            value.add(S[s:e])
    return len(value)

S = input()
good_str = input()
k = int(input())
check = make_check(good_str)
sum_ls = make_sum_ls(S)
ans = solution(S,sum_ls,k)
print(ans)