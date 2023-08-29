def recur(now_str:str,L:int)->None:
    global ans
    if len(now_str) == L:
        ans += 1
        return
    for alpha in alphabets:
        if cnt_check[alpha] and now_str[-1] != alpha:
            cnt_check[alpha] -= 1
            recur(now_str+alpha,L)
            cnt_check[alpha] += 1

S = input()
cnt_check = dict()
alphabets = set()
for s in S:
    cnt_check[s] = cnt_check.get(s,0) + 1
    alphabets.add(s)
ans = 0
for alpha in alphabets:
    cnt_check[alpha] -= 1
    recur(alpha,len(S))
    cnt_check[alpha] += 1
print(ans)