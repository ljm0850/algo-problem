def solve(n:int):
    global ans
    for i in range(n):
        ans.append(ans[i]+' '+ans[i])
        ans[i] = " "*n+ans[i]+" "*n

N = int(input())
ans = ["  *  "," * * ","*****"]
k = 0
N //=3
while N != 1:
    k +=1
    N //= 2
for i in range(k):
    solve(3*2**i)
for answer in ans:
    print(answer)