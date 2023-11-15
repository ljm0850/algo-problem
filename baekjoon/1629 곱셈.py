def solve(a,b):
    if b == 1:
        return a % C

    temp = solve(a,b//2)

    if b % 2 :
        return temp * temp * a % C
    else:
        return temp * temp % C

A,B,C = map(int,input().split())
print(solve(A,B))