def check(i,total):
    global ans
    if total > N:
        return
    if i < 0 :
        if ans < total:
            ans = total
        return
    for num in nums[::-1]:
        check(i-1,total+num*10**i)

N,K = map(int,input().split())
n=len(str(N))-1
nums = list(map(int,input().split()))
nums.sort()
ans = 0
check(n,0)
check(n-1,0)
print(ans)