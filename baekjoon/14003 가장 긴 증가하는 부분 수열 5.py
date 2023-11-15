import sys
def solve(n:int,arr:list)->tuple:
    dp,length = [-1000000001],0
    check = [0]*(n)

    for i in range(n):
        num = arr[i]
        if dp[-1] < num:
            dp.append(num)
            length += 1
            check[i] = length
        else:
            s,e = 0,length
            while s < e:
                mid = (s+e)//2
                if dp[mid] < num:
                    s = mid + 1
                else:
                    e = mid
            dp[e] = num
            check[i] = e
    answer = []
    t = length
    for i in range(n-1,-1,-1):
        if check[i] == t:
            t -= 1
            answer.append(arr[i])
    return length,answer[::-1]

N = int(input())
nums = list(map(int,sys.stdin.readline().split()))
l,path = solve(N,nums)
print(l)
print(*path)
