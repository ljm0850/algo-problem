def solve(n:list)->str:
    arr = list(map(int,n))
    if sum(arr) % 3 != 0 or not 0 in arr:
        return "-1"
    n.sort(reverse=True)
    return "".join(n)

N = list(input())
ans=solve(N)
print(ans)