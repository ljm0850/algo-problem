def matrix(X,Y):
    ans = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] = (ans[i][j]+X[i][k] * Y[k][j])%1000000007
    return ans

def solve(n):
    if n == 1:
        return basic
    temp = solve(n//2)
    answer = matrix(temp,temp)
    if n %2 :
        answer = matrix(answer,basic)
    return answer

n = int(input())
basic = [[1,1],[1,0]]
print(solve(n)[0][1])