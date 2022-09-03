def check(total,length):
    global ans
    if 1<=length <= 6:
        temp = abs(int(total)-N)+len(total.lstrip('0'))
        if int(total) == 0:
            temp +=1
        if temp < ans:
            ans = temp
    if length <=6:
        for num in nums:
            check(total+num,length+1)

nums = ['0','1','2','3','4','5','6','7','8','9']
N = int(input())
M = int(input())
err = []
if M:
    err = input().split()
for er in err:
    nums.remove(er)
ans = abs(N-100)
check('',0)
print(ans)