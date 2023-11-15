# 앞 뒤 집과 색이 달라야함
# R G B 세가지 색 사용

def check(i):
    for j in range(3):              # 이번 집의 RGB 선택
        pay = total[i][j]
        temp = []
        for k in range(3):          # 전집
            if k != j:              # 같은색 배제
                temp.append(dp[i-1][k]+pay)
        dp[i][j] = min(temp)

N = int(input())        # 집의 수1000 이하
dp = [[0]*3 for _ in range(N)]
total = [list(map(int,input().split())) for _ in range(N)]
for i in range(3):
    dp[0][i] = total[0][i]
for c in range(1,N):
    check(c)
print(min(dp[N-1]))