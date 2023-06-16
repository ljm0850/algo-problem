S = list(input())
T = list(input())
ans = 0
while True:
    if len(S) == len(T):
        if S == T:
            ans = 1
        break
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()
print(ans)
    
