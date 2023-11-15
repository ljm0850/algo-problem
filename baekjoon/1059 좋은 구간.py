def solve(group:list[int],n:int)->int:
    for idx in range(len(group)):
        num = group[idx]
        if num >= n:
            max_num = num
            if idx == 0:
                min_num = 1
            else:
                min_num = group[idx-1]+1
            break
    cnt = 0
    for num1 in range(min_num,max_num):
        for num2 in range(num1+1,max_num):
            if num1<=n<=num2:
                cnt += 1
    return cnt

L = int(input())
group = list(map(int,input().split()))
n = int(input())
group.sort()
ans = solve(group,n)
print(ans)