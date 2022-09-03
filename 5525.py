# I0I               N = 1
# I0I0I             N = 2
# I0I0I0I           N = 3
# 이중 반복문 힘들듯
N = int(input())                    #100만 이하
M = int(input())    # S의 길이, 100만 이하
S = input()
ans = 0
i = 2
cnt = 0
while i < M:
    if S[i-2] != 'I' or S[i-1] !='O':
        i+=1
        cnt = 0
        continue
    elif S[i] != 'I':
        cnt = 0
    else:
        cnt +=1
        if cnt == N:
            ans +=1
            cnt -= 1
    i += 2
print(ans)
