def solution(N:int,tree:list[int])->int:
    ans = 0
    ls = [0]*(N)
    total = 1
    for i in range(N):
        num = tree[i]
        total *= num
        ls[i] = total
    for s1 in range(N-3):
        total = ls[s1]
        for s2 in range(s1+1,N-2):
            v2 = ls[s2] // ls[s1]
            total += v2
            for s3 in range(s2+1,N-1):
                v3 = ls[s3] // ls[s2]
                total += v3
                for s4 in range(s3+1,N):
                    v4 = ls[s4] // ls[s3]
                    total += v4
                    ans = max(total,ans)
                    total -= v4
                total -= v3
            total -= v2
    return ans

N = int(input())
tree = list(map(int,input().split()))
ans = solution(N,tree)
print(ans)