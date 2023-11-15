def solution(N):
    check = [False]*(N+1)
    check[0] = True
    check[1] = True
    for i in range(2,N+1):
        if check[i-1] == False:
            check[i] = True
        elif i>=3 and check[i-3] == False:
            check[i] = True
    if check[N]:
        return "SK"
    return "CY"

N = int(input())
ans = solution(N)
print(ans)