def solve(A:int,B:int)->int:
    ans = 50
    if len(A) > len(B):
        short,long = B,A
    else:
        short,long = A,B
    s = len(short)
    l = len(long)
    gap = l-s

    for i in range(gap+1):
        target = long[i:i+s]
        cnt = 0
        for j in range(s):
            if target[j] != short[j]:
                cnt +=1
        ans = min(ans,cnt)
    return ans

A,B = input().split()
ans=solve(A,B)
print(ans)